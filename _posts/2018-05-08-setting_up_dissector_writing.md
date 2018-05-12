---
layout: post
title:  "Setting Up for Dissector Writing"
category: tech
---

Some minimal information you need to know in order to write Wireshark dissectors.

I'm assuming your Wireshark dissectors are written in Lua.

# Installing Wireshark

## Windows, MacOS
On Windows and MacOS, we go to [Wireshark's official](https://www.wireshark.org/download.html); I'm going to assume you're using the 64-bit installer.

I haven't had good experience with WinPcap so I didn't install that component. 

## Linux
Each distro is somehow always a special snowflake but generally your GUI software / application manager should have it.
If you're using a terminal package manager (apt,yum,dnf, etc), know that Wireshark also has a non-GUI version so keep that in mind (sometimes the GUI version is called *wireshark-qt*).

Wireshark should have a GUI and have this Lua menu here:
![wireshark_lua_menu.png](/assets/dissector/wireshark_lua_menu.png)

If it doesn't, you might not be able to add your Lua dissector.

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
# Dry Run
Let's give it a try:
1. Place [this dummy Lua dissector](/assets/dissector/dummy.lua) in either the *personal plugins* or *global plugins* folder
2. Open [this dummy pcap file](/assets/dissector/dummy.pcap) in Wireshark
3. Reload the Lua plug-ins with Ctrl+Shift+L or *Analyze->Reload Lua Plugins*

Should look like this:
![/assets/dissector/wireshark_dummy_lua_loaded.png](/assets/dissector/wireshark_dummy_lua_loaded.png)

# Packet Capture
## Windows
If you need to capture packets, I've had a good experience with RawCap. WinPcap has all sorts of limitations, especially on capturing on localhost (and apparently, problems with capturing some wireless interfaces).

Be aware that RawCap will require elevated privileges on your machine and that's a security issue. If you trust RawCap won't do anything bad (like I do), go get [RawCap](http://www.netresec.com/?page=RawCap).

## Linux/MacOS
Wireshark should be good enough for packet capture in Linux.

# Cool Tool Mention: Protocol ASCII Representation
I enjoyed using the [Protocol](http://www.luismg.com/protocol/) CLI to create an ASCII representations of packets.

In terms of ease, out of this command:
```python
python3 protocol "Field1: 16, Field2: 8, Field3:42"
```
You get this:
```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|             Field1            |     Field2    |               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+               +
|                             Field3                            |
+   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   |
+-+-+
```



