dummy_proto = Proto("dummy","Dummy Protocol")

function dummy_proto.dissector(buffer,pinfo,tree)
    pinfo.cols.protocol = "Dummy Protocol"
    local subtree = tree:add(dummy_proto,buffer(),"It worked, dummy protocol loaded!")
end

DissectorTable.get("udp.port"):add(5006,dummy_proto)