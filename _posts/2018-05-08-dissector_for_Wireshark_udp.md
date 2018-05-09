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

# Colors

## 





