---
layout: post
title:  "Simple Wireshack Dissector for a simple UDP Protocol"
category: wip
---

# Simple Wireshack Dissector for a simple UDP Protocol

We'll explore on how to create a dissector for an UDP protocol.
We'll write in Lua, perf C/C++

Reminds  http://wsgd.free.fr/faq.html

We assume:
+ Wireshark is somewhat familiar to you: you've played with it a bit and you have an understanding of its basic features 
+ You can edit files Lua files in a Lua-friendly editor (at least syntax highlight is recommended)

# What Can a Dissector Do?



## Pertinent Fields in a Packet

## Query Filter



# Installing Wireshark
## Windows
On Windows, we go to [Wireshark's official](https://www.wireshark.org/download.html); I'm going to assume you're using the 64-bit installer.

When the installer prompts for what to install:
+ *Choose Components* Step: the defaults are fine
+ *Packet Capture* Step: We **don't need WinPcap** but you may install it if you want to.
+ Other steps: as you wish

## MacOS

????

## Linux
Each distro is somehow always a special snowflake but generally your package manager should have Wireshark.   
Know that Wireshark also has a non-GUI version so keep in mind you might have installed the wrong one.

A properly-installed Wireshark will have a GUI and have this Lua menu here:
![wireshark_lua_menu.png](/assets/dissector/wireshark_lua_menu.png)

**Issues:**

---
+ On Fedora, no Lua menu  

You probably need to also install *wireshark-devel*

```
sudo dnf install wireshark-devel
 ```

# Lua Editor
The editor is up to you, the smarter the better generally.

I'm using [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/) with a Lua plugin.

Find your IDE or editor of your choice that supports, at a minimum, Lua syntax highlight.

# Loading Dissectors into Wireshark
Wireshark will load dissectors from specific folders/directories.

To find out which, open Wireshark, go to Help -> About -> Folders.  
You might need to create these folders if they don't exist.

For example, on Windows, I place my Lua-written dissectors in **Personal Plugins**:
```
Personal Lua Plugins		C:\Users\alex\AppData\Roaming\Wireshark\plugins
```

Let's give it a try:
1. Place [this dummy Lua dissector](/assets/dissector/dummy.lua) in either the *personal plugins* or *global plugins* folder
2. Open [this dummy pcap file](/assets/dissector/dummy.pcap) pcap file in Wireshark
3. Reload the Lua plug-ins with Ctrl+Shift+L or *Analyze->Reload Lua Plugins*

Should look like this:
![/assets/dissector/wireshark_dummy_lua_loaded.png](/assets/dissector/wireshark_dummy_lua_loaded.png)

4. Go ahead and remove the dummy.lua file

# Dissector for an UDP Protocol
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

### Registering Our Protocol on UDP Port 65065
In our Lua file:
```Lua
--we create our new protocol
local proto_health = Proto.new("health", "Health Protocol")

--the `dissector()` method is called by Wireshark when parsing our packets
function proto_health.dissector(buf, pinfo, tree)
end

--we register our protocol on UDP port 65065 
udp_table = DissectorTable.get("udp.port"):add(65065, proto_health)
```

### Declaring Our Protocol Fields
We first declare our field types and size for the fields in the protocol we invented.

```Lua
local proto_health = Proto.new("health", "Health Protocol")

--- --- Our Fields --- ---
-- for `field_version`:
--  type/size of this field (here uint8, a byte).
--  "health.version" is used in the display filter to query/seach/narrow down a list of packets (e.g. health.version == 1)
--  "Version" is the display name when drilling down in the packet
--  `base.DEC` is the repsentation of the uint8 (we could have used base.HEX)
field_version = ProtoField.uint8("health.version", "Version", base.DEC)

-- we get to use more of the convenience Field constructors
field_health = ProtoField.uint8("health.health", "Health", base.HEX)
field_groupid = ProtoField.uint16("health.group", "Group ID", base.HEX)
-- GUID has its own representation
field_workerguid = ProtoField.guid("health.guid", "Worked ID")

function proto_health.dissector(buf, pinfo, tree)
    --
end

udp_table = DissectorTable.get("udp.port"):add(65065, proto_health)
```

### Mapping Fields to Packet Bytes
We've declared our fields type/size but now we need to tell Wireshark where they are in the packet.
```Lua
local proto_health = Proto.new("health", "Health Protocol")
field_version = ProtoField.uint8("health.version", "Version", base.DEC)
field_health = ProtoField.uint8("health.health", "Health", base.HEX)
field_groupid = ProtoField.uint16("health.group", "Group ID", base.HEX)
field_workerguid = ProtoField.guid("health.guid", "Worked ID")

-- `buffer` holds the UDP payload, all the bytes from our protocol
-- `tree` is the structure we see when dissecting one particular packet
function proto_health.dissector(buffer, pinfo, tree)
    
end

udp_table = DissectorTable.get("udp.port"):add(65065, proto_health)
```

