---
layout: post
title:  "Simple Wireshack Dissector for a simple UDP Protocol"
category: tech
---

# Wireshark Dissector for an UDP Protocol
In this post, we'll explore building a simple UDP protocol dissector. Breifly, a dissector is used by Wireshark to identify a protocol's fields in the packets, as well as display, and filter information about packets (e.g. a DNS dissector will identify the URL queried, the TTL, etc.)

I've found a good amount of API documentation and more advanced tutorials but nothing covering the basics like I would have liked when I recently had to build an UDP protocol dissector myself.

This custom dissector will be in written in Lua; dissectors can be written in C++ if performance is needed.

## UDP Protocol 
We're going to invent ourselves a simple UDP protocol to then build a simple dissector around it.

Let's imagine an UDP protocol for worker nodes reporting their health to a controller node.
```
Health Report Protocol
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version(8 bits)| Health(8 bits)|        GroupID(16 bits)       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                      WorkerUUID(128 bits)                     +
|                                                               |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```
We have 4 fields in our protocol:  
+ Version (8-bit unsigned int), expected versions of the protocol (we have only 1 version for now):
    + Version 1: 0x01
+ Health code (8-bit unsigned int), 3 health codes in our version:
    + Healthy State: 0x01
    + High Load State: 0x02
    + Failure State: 0x03
+ GroupID (16-bit unsigned int), the group that the worker is part of
+ WorkerdUUID (128-bit UUID)

## Dissector
Our dissector will be a Lua file that Wireshark will load and use to parse our UDP packet.

### Registering Our Protocol on UDP Port 55055
In our Lua file:
```Lua
--we create our new protocol
local proto_health = Proto.new("health", "Health Protocol")

-- the `dissector()` method is called by Wireshark when parsing our packets
function proto_health.dissector(buffer, pinfo, tree)
   
end

--we register our protocol on UDP port 55055
udp_table = DissectorTable.get("udp.port"):add(55055, proto_health)
```

### Declaring Our Protocol Fields
We first declare our field types and size for the fields in the protocol we invented.

There are
+ (normal) fields: they map to the packet bytes.
+ generated fields: they are derived information from the packet we wish to display in the tree (e.g. the human-readable meaning of a code) and make searchable in the display filter.


```Lua
local proto_health = Proto.new("health", "Health Protocol")

--- --- Our Fields --- ---
-- These are the fields defined in our protocol
-- They will also be searchable in the display filter
-- for `field_version`:
--  type/size of this field (here uint8, a byte).
--  "health.version" to be  used in the display filter to query/search/narrow down a list of packets (e.g. health.version == 1)
--  "Version" is the display name/field label shown when drilling down in a packet
--  `base.DEC` is the representation of the uint8 (we could have used base.HEX)
local field_version = ProtoField.uint8("health.version", "Version", base.DEC)
local field_health = ProtoField.uint8("health.code", "Health Code", base.HEX)
local field_groupid = ProtoField.uint16("health.group", "Group ID", base.HEX)
-- guid field has its own representation
local field_workerguid = ProtoField.guid("health.guid", "Worked ID")

--- Our Generated Fields --- 
-- Generated fields are fields derived from information found in the packet
-- In this case, we want to display a string representation of the health code
generated_health_name = ProtoField.string("health.status", "Health Status")

-- we attach all fields (normal and generated) to our protocol
proto_health.fields = {field_version, field_health, field_groupid,
 field_workerguid, generated_health_name}

function proto_health.dissector(buffer, pinfo, tree)

end

udp_table = DissectorTable.get("udp.port"):add(55055, proto_health)
```


### Dissecting the Protocol

```Lua
local proto_health = Proto.new("health", "Health Protocol")

local field_version = ProtoField.uint8("health.version", "Version", base.DEC)
local field_health = ProtoField.uint8("health.code", "Health Code", base.HEX)
local field_groupid = ProtoField.uint16("health.group", "Group ID", base.HEX)
local field_workerguid = ProtoField.guid("health.guid", "Worked ID")

generated_health_name = ProtoField.string("health.status", "Health Status")

proto_health.fields = {field_version, field_health, field_groupid,
 field_workerguid, generated_health_name}

-- the `dissector()` method is called by Wireshark when parsing our packets
-- `buffer` holds the UDP payload, all the bytes from our protocol
-- `tree` is the structure we see when inspecting/dissecting one particular packet
function proto_health.dissector(buffer, pinfo, tree)
    -- Changing the value in the protocol column (the Wireshark pane that displays a list of packets) 
    pinfo.cols.protocol = "Health Report"

    -- We label the entire UDP payload as being associated with our protocol
    local payload_tree = tree:add( proto_health, buffer() )

    -- For the `version` field, we have:
    -- the position of the first byte (which is 0 here because `version` byte is the first one in the protocol)
    -- how long (in bytes) this field is (1 in our case)
    local version_pos = 0
    local version_len = 1
    -- `version_buffer` holds the range of bytes
    local version_buffer = buffer(version_pos,version_len)
    -- with `add()`, we're associating the range of bytes from `buffer` with our field we declared earlier
    -- this means:
    -- (1) the values is now searchable in the display filter (e.g.we can filter a list of packets with health.version == 1)
    -- (2) Wireshark will create an entry in the packet inspection tree, highlight which part of the packet we're referencing and show a label with our field name and value
    payload_tree:add(field_version, version_buffer)

    local health_pos = version_pos + version_len
    local health_len = 1
    local health_buffer = buffer(health_pos,health_len)
    payload_tree:add(field_health, health_buffer)

    local groupid_pos = health_pos + health_len
    local groupid_len = 2
    local groupid_buffer = buffer(groupid_pos, groupid_len)
    payload_tree:add(field_groupid, groupid_buffer)

    local workerguid_pos = groupid_pos + groupid_len
    local workerguid_len = 16
    local workerguid_buffer = buffer(workerguid_pos,workerguid_len)
    payload_tree:add(field_workerguid, workerguid_buffer)

    -- We build our health code <-> health status table
    local health_code_table = {}
    health_code_table[1] = "Healthy"
    health_code_table[2] = "High Load"
    health_code_table[3] = "Failure"

    -- we remember that `health_buffer` holds a byte range, we interpret this as a uint
    local health_code = health_buffer:uint()
    -- we fetch the string from our table
    local health_string = health_code_table[health_code]
    -- we associate this string as the value for our generated field
    -- it'll also be searchable in the display filter and also appear in the inspection/dissection tree
    -- set_generated() adds square brackets around the field to mark it as generated
    payload_tree:add(generated_health_name, health_string):set_generated()        

end
udp_table = DissectorTable.get("udp.port"):add(55055, proto_health)
```

### Results
We see Wireshark shows us our the our fields, and protcol name:
![Packet Fields](/assets/dissector/dissector_result_1.png)

We can filter packets by field value:
![Filter Field](/assets/dissector/dissector_query_code.png)

We can also filter packets generated field value:
![Fitler Generated Field](/assets/dissector/dissector_query_status_string.png)



### Capture File of Our Protocol
Here's the [capture file](/assets/dissector/health_protocol_capture.pcap) of 3 packets from our Health Report protocol.

### Dissector Code With All Comments
[Download it](/assets/dissector/dissector.lua)
```Lua
--we create our new protocol
local proto_health = Proto.new("health", "Health Protocol")

--- --- Our Fields --- ---
-- These are the fields defined in our protocol
-- They will also be searchable in the display filter
-- for `field_version`:
--  type/size of this field (here uint8, a byte).
--  "health.version" to be  used in the display filter to query/search/narrow down a list of packets (e.g. health.version == 1)
--  "Version" is the display name/field label shown when drilling down in a packet
--  `base.DEC` is the representation of the uint8 (we could have used base.HEX)
local field_version = ProtoField.uint8("health.version", "Version", base.DEC)
local field_health = ProtoField.uint8("health.code", "Health Code", base.HEX)
local field_groupid = ProtoField.uint16("health.group", "Group ID", base.HEX)
-- guid field has its own representation
local field_workerguid = ProtoField.guid("health.guid", "Worked ID")

--- Our Generated Fields --- 
-- Generated fields are fields derived from information found in the packet
-- In this case, we want to display a string representation of the health code
generated_health_name = ProtoField.string("health.status", "Health Status")

-- we attach all fields (normal and generated) to our protocol
proto_health.fields = {field_version, field_health, field_groupid,
 field_workerguid, generated_health_name}

-- the `dissector()` method is called by Wireshark when parsing our packets
-- `buffer` holds the UDP payload, all the bytes from our protocol
-- `tree` is the structure we see when inspecting/dissecting one particular packet
function proto_health.dissector(buffer, pinfo, tree)
    -- Changing the value in the protocol column (the Wireshark pane that displays a list of packets) 
    pinfo.cols.protocol = "Health Report"

    -- We label the entire UDP payload as being associated with our protocol
    local payload_tree = tree:add( proto_health, buffer() )

    -- For the `version` field, we have:
    -- the position of the first byte (which is 0 here because `version` byte is the first one in the protocol)
    -- how long (in bytes) this field is (1 in our case)
    local version_pos = 0
    local version_len = 1
    -- `version_buffer` holds the range of bytes
    local version_buffer = buffer(version_pos,version_len)
    -- with `add()`, we're associating the range of bytes from `buffer` with our field we declared earlier
    -- this means:
    -- (1) the values is now searchable in the display filter (e.g.we can filter a list of packets with health.version == 1)
    -- (2) Wireshark will create an entry in the packet inspection tree, highlight which part of the packet we're referencing and show a label with our field name and value
    payload_tree:add(field_version, version_buffer)

    local health_pos = version_pos + version_len
    local health_len = 1
    local health_buffer = buffer(health_pos,health_len)
    payload_tree:add(field_health, health_buffer)

    local groupid_pos = health_pos + health_len
    local groupid_len = 2
    local groupid_buffer = buffer(groupid_pos, groupid_len)
    payload_tree:add(field_groupid, groupid_buffer)

    local workerguid_pos = groupid_pos + groupid_len
    local workerguid_len = 16
    local workerguid_buffer = buffer(workerguid_pos,workerguid_len)
    payload_tree:add(field_workerguid, workerguid_buffer)

    -- We build our health code <-> health status table
    local health_code_table = {}
    health_code_table[1] = "Healthy"
    health_code_table[2] = "High Load"
    health_code_table[3] = "Failure"

    -- we remember that `health_buffer` holds a byte range, we interpret this as a uint
    local health_code = health_buffer:uint()
    -- we fetch the string from our table
    local health_string = health_code_table[health_code]
    -- we associate this string as the value for our generated field
    -- it'll also be searchable in the display filter and also appear in the inspection/dissection tree
    -- set_generated() adds square brackets around the field to mark it as generated
    payload_tree:add(generated_health_name, health_string):set_generated()        

end

--we register our protocol on UDP port 55055
udp_table = DissectorTable.get("udp.port"):add(55055, proto_health)
```