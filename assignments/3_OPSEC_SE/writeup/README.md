# Writeup 3 - Operational Security and Social Engineering

Name: Iniyan Chezhian
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Iniyan Chezhian

## Assignment Writeup

### Part 1 (40 pts)

#### Synopsis

Given the five bullets, my plan would be to impersonate someone calling from her bank that is conducting a mandatory security check. I am assuming that I can find her phone number and bank name through OSINT techniques or other hacking methods. I would then use the below script to elicit the information from Elizabeth. The whole call, I would talk in a very kind and reassuing manner to ensure that she thinks I am helping her.

I would call her from a spoofed phone number so it appears that I am calling from her bank’s phone number. I would find this number online by visiting her bank’s website.

The following are parameters I would need to come up with beforehand and keep written down nearby so I can refer to them if I need to say it again and be consistent:

•	*my_fake_name*

•	*her_bank_name*

#### Script

> Hello Elizabeth, this is {*my_fake_name*} calling from {*her_bank_name*}. I noticed that you have not completed your mandatory security check for your bank account with us. Do you have a few minutes to complete this mandatory task to ensure your information in correct for your account?

*(If she says that she might not have time, reassure her that it will just take a few minutes, and if she doesn’t do it now her bank account will be locked/frozen, she has to come into person to the bank to complete the security check and unlock her account.)*

> Great, I basically need to confirm that you really are Elizabeth Moffet.

> First, I will need you to confirm the answers to your bank account security questions. Could you verify with me your …

> … mother’s maiden name?

> … the city you were born in?

> … the name of your first pet?

*(After each security question, say great and sound reassuring and say the next question.)*

> Excellent, now I need you to confirm your account’s ATM pin number.

> Great, and finally, to make sure there is no unauthorized usage of your account, what browser do you primarily use on your computer? This will help us raise a flag if we see any suspicious activity.

> Great, so now your account’s mandatory security check is complete. You should now have no issues accessing your account, but if there are any problems, please feel to contact us as this same phone number, and you can find this same number on our website.

> Is there anything else with your account that I can help you with today?

> Thank you for choosing {*her_bank_name*} and have a great day!

### Part 2 (60 pts)

The following are three vulnerabilities for 1337Bank’s website.

#### Open Ports

Your website has several open ports. Specifically, port 22 is open for ssh and port 1337 is open for html. This is essentially like leaving a door open on your website. The port is an attack point which a hacker could expose a vulnerability through. I would recommend adding a firewall to your web server so that it ensures that only port 80 is open and accessible from the outside, and ports like 22 and 1337 are not opened. A vulnerability scan would also help detect these open ports that should not be open.

#### Robots.txt and HTML Source

Your website’s robot.txt exposed a hidden link on the website that may have contained potential login information. Furthermore, the HTML source had a comment which may have contained potential login information. It seems that there was no proofreading done on the person who built the website. In the future, it is a good idea to hire someone to do a vulnerability scan on the website. This should find things such as hidden pages and comments in source code that is publicly viewable and should not be.

#### Passwords

Your v0idcache password was too simple and easily crackable. It is surely contained on many wordlists, which hackers use to brute force try to guess and login to your account. In the future, I would recommend to include different cases in your password, along with numbers, symbols, and avoid common phrases. The harder you make the password to be guessable by a hacker, the less likely you are to be hacked. Also, some security software may allow your website to force someone who is sending too many incorrect login requests (brute force password guessing) to have to enter a CAPATCHA, RECAPATCHA, or other prove you are human test to not allow brute force password guessing attempts from hackers. Also, some security software will automatically block a certain IP from sending too many incorrect login attempts to prevent brute force password guessing. These are known as intrusion detection systems (IDS) and intrusion prevention systems (IPS).
