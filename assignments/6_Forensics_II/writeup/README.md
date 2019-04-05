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

5. I see that the FTP on port 20 is fora file called find_me.jpeg.

I did File, Export, HTTP in Wireshark. Then this gave me a file that when opened in Firefox seems to be umdctf.io website.

Then I just did export Bytes. This gave me a file, but it wasn't all that useful.

Then I tried to do Follow TCP Stream. First I tried the default ASCII file to save and run through exiftool; this gave nothing. Then I saved the file as Raw. This gave me lots of information in exiftool.

a) JPEG

b) According to GPS Position, 
34° 57' 29.14"S, 54° 56' 16.28"W
This is Rambla General Jose Artigas, 20100 Punta del Este, Departamento de Maldonado, Uruguay; according to Google Maps.

c) When was this photo taken? Provide a timestamp in your answer.

d) What kind of camera took this photo?

e) 4.5m below sea level


### Part 2 (55 Pts)

*Replace this text with your repsonse to our prompt for part 2!*
