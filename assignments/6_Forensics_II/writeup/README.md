# Writeup 6 - Forensics

Name: Iniyan Chezhian
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Iniyan Chezhian

## Assignment Writeup

### Part 1 (45 Pts)

I started by opening netlog.pcap in Wireshark. The hint is to look at TCP.

The IP's on source and destination used for TCP are:
185.199.110.153 (unpublished GitHub Pages site)
142.93.136.81 (http://1337bank.money/)
159.203.113.181 (doesn't load - times out)

I just tried each one of these in the browser.

1. The hacked site is 1337bank.money, so this is 142.93.136.81.

2. We can assume they were using hacking tools. This might be something like a port scanner. Then they might have been trying to do some malicious FTP stuff, since there is a lot of that.

3. The hacker seems to be 159.203.113.181. There is a lot of stuff between that and the 1337bank address. Doing a whois on this gives me that they are DigitalOcean, LLC at 101 Ave of the Americas, 10th Floor, New York, NY 10013 US. They are connecting from New York.

4. There are FTP from the hacker IP all seem to be on port 20.

5. I see that the FTP on port 20 is for a file called find_me.jpeg.

I did File, Export, HTTP in Wireshark. Then this gave me a file that when opened in Firefox seems to be umdctf.io website.

Then I just did export Bytes. This gave me a file, but it wasn't all that useful.

Then I tried to do Follow TCP Stream. First I tried the default ASCII file to save and run through exiftool; this gave nothing. Then I saved the file as Raw. This gave me lots of information in exiftool.

a) JPEG

b) According to GPS Position, 
34° 57' 29.14"S, 54° 56' 16.28"W
This is Rambla General Jose Artigas, 20100 Punta del Este, Departamento de Maldonado, Uruguay; according to Google Maps.

c) 2018:12:23 17:16:24

d) Apple iPhone 8

e) 4.5m below sea level


6. Besides find_me.jpb, the only other file for FTP packets is greetz.fpff

7. It seems that port 20 should be blocked, this is where they stole a file from. When someone like the hackers makes many hits on the server, that's a red flag. Perhaps a Website Security Service could provide them with assistnace in blocking hackers when noticed.



### Part 2 (55 Pts)

I started with the given code. I was able to add author, which is just a string. Adding the timestamp was added by converting to int, then using datetime to format the output to a readable format instead of Unix time.

i. According to the timestamp I formatted, 2019-3-27 4:15:05. This is March 3 2019 at 4:15:05.

ii. According to the author, it was fl1nch.
