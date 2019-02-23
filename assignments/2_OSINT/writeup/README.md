# Writeup 2 - OSINT

Name: Iniyan Chezhian
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Iniyan Chezhian

## Assignment Writeup

### Part 1 (45 pts)

1
Elizabeth Moffet
I got this from Twitter.

2
Works at Elite Banking (also called 13/37th National Bank)
Banking CEO
Their website URL is: http://1337bank.money

3

email:v0idcache@protonmail.com
Found this from Googleling "v0idcache".

https://twitter.com/v0idcache
Found from inteltechniques.com

http://videobam.com/users/v0idcache
https://storybird.com/members/v0idcache
https://www.fashiolista.com/style/v0idcache
Found from usersearch.org

https://github.com/v0idcache

4
DigitalOcean, LLC
142.93.136.81
1337bank.money
Digital Ocean is in New York, but the website 1337bank.money and IP 142.93.136.81 are in Canada.

Amsterdam, Netherlands
This is what I get from https://www.iplocation.net/

5
http://1337bank.money/robots.txt
I found this by just trying the URL.

http://1337bank.money/secret_directory
I found this from the robots.txt

http://1337bank.money:1337/
I found this by trying the URL. It tells me the password is Fail, but I was unable to use this anywhere.

6

http and ssh are open, these are 80 and 22 respectively

PORT     STATE  SERVICE
21/tcp   closed ftp
22/tcp   open   ssh
23/tcp   closed telnet
80/tcp   open   http
110/tcp  closed pop3
143/tcp  closed imap
443/tcp  closed https
3389/tcp closed ms-wbt-server

This was all done using nmap.

1337 also works. I tried this by typing in the URL. So this is another http port.

7
The SSH is running Ubunutu.
SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.2 
I found this from accessing the ssh at http://1337bank.money:22/

The http is using Werkzeug/0.14.1 Python/3.7.2
I found this from https://centralops.net/co/DomainDossier.aspx

Also, both can be found from pentest-tools.com

8
CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}
I found this at: https://www.reddit.com/user/v0idcache/comments/atc1f7/x/

CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}
I found this at: https://centralops.net/co/DomainDossier.aspx

CMSC389R-{h1ding_fil3s_in_r0bots_L0L}
I found this at: http://1337bank.money/secret_directory

CMSC389R-{h1dd3n_1n_plain_5ight} 
I found this in the html of the website 1337bank.money

Extra information that I found, but could not use.
fl1nch
AB4300.txt
https://pastebin.com/WghDuAr7


### Part 2 (75 pts)

My code works by going through the possible passwords. At first I tried to point the output to another text file, but this was unnecesary and I instead chose to look for the string "Fail" in the data. If there was no "Fail" then the password worked.

The password that I got to work was linkinpark.

(source code is in this directory)


### Notes
I got blocked from HIBP during this assignment:
"You have been blocked from accessing this resource on Have I Been Pwned"
