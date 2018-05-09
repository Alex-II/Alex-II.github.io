# Wireshack Dissector



It's assumed:
+ Python 3 is installed and you know how to run Python 3 scripts
+ Wireshark is somewhat familiar to you: you've played with it, you have an understanding of its basic features 
+ If you're using Linux, you know how to install things with your package manager (yum, apt, dnf, or whatever) or your Software Center (or equivalent)
+ You can use the Windows command prompt or Linux terminal
+ You're willing, able and understand the consequences of installing applications that will require elevated privileges on your operating system

# Setting Up Packet Sniffing

## Testing Our Setup

## Installing Wireshark
If you already know how to get Wireshark or already have Wireshark, skip this.

### Windows
On Windows, we go to [Wireshark's official](https://www.wireshark.org/download.html); I'm going to assume you're using the 64-bit installer.

When the installer prompts for what to install:
+ *Choose Components* Step: the defaults are fine
+ *Packet Capture* Step: We **don't need WinPcap** but you may install it if you want to.
+ Other steps: as you wish

### MacOS

### Linux
Each distro is somehow always a special snowflake but generally your package manager should have Wireshark.

On Fedora, it goes something like this
```
sudo apt-get update
sudo apt-get install wireshark
 ```

 or 

 ```
sudo apt-get install wireshark

 ```

So, go ahead and Google



## Our Python UDP Test
This Python script [test_udp_send.py](/assets/dissector/test_udp_send.py]):  
1. Binds to UDP on some port (open the script and change the port if it's already used)
2. Starts another process to send itself an UDP packet
3. Prints the contents it has received over UDP

We'll use it :
+ to confirm networking, Python 3, the OS, etc. is working as expected; it's easier to catch and identify glitches with a small script
+ later, to confirm we can capture traffic correctly

Run the Python script with Python 3, you should see something like this in Windows:

```
c:\tmp>python3 test_udp_send.py  
received payload: b'this message should fit an UDP payload of 1024 bytes' 
```

or in Linux/macOS something like:

```
alex@ubuntu:~$ python3 test_udp_send.py
received payload: b'this message should fit an UDP payload of 1024 bytes'
```
### Issues

---
+ If you see somthing like  
 ```
OSError: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions
```
it's probably because the UDP port 5006 is already used by another application.  
**Open the script, change the port number to something else and remember the new port you've set. When you see port 5006, remember you've changed it**

---
+ If you're getting Python syntax errors, you may be using the Python 2 interpreter to run this Python 3 script.

## Setting Up Packet Sniffing (Linux/MacOS)



## Setting Up Packet Sniffing (Windows)
For packet sniffing under Windows we'll use RawCap (should work fine if you're using Windows 7 or higher).

To make sure we can sniff traffic; we'll:
1. Download RawCap
2. Start (by double-cliking the exe) RawCap sniffing on 127.0.0.1 and save the captured packets to a file
3. Run the *test_udp_send.py* script to generate traffic
4. Stop RawCap with Ctrl+C (to allow it to flush to disk)

### 1. Download RawCap
Note that you're about to download an executable that needs elevated privileges to run correctly, from a website not as well-known as Wireshark's.. so be aware of that risk.  
For the download, visit the [RawCap](http://www.netresec.com/?page=RawCap) website.

### 2. Start RawCap sniffing
Once you've downloaded the **RawCap.exe** executable, just double-click the executable to run it (and again, you'll need to run it with elevated privileges).

RawCap should open the command prompt:
+ select the *127.0.0.1* interface to sniff
+ select a filename/filepath for the traffic capture file: whatever you want, you'll need to load this file into Wireshark later  

RawCap should start capturing at this point.

### 3. Run test_udp_send.py to generate traffic
Time to run the *test_udp_send.py* script to generate traffic which should be captured by RawCap this time.

### 4. Stop RawCap
After running the script, stop RawCap by using Ctrl+C (don't just close the window as it won't write the capture file to disk).

## Viewing the *pcap* file in Wireshark
Let's verify we've captured correctly: open up Wireshark, and load the capture file we've just created.

Here's the test packet in Wireshark:
![wireshark_test_packet.png](/assets/dissector/wireshark_test_packet.png)

Gotten so far? Great, the setup should be ready for building and testing a Wireshark protocol dissector (remember how we're doing all this for that?)



# Our Custom Protocol



# Our Dissector

# Resources


