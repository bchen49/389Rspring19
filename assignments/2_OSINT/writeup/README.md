# Writeup 2 - OSINT

Name: Benjamin Chen
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Benjamin Chen

## Assignment Writeup

### Part 1 (45 pts)

1) v0idcache's name is Elizabeth Moffet

2) She works at 13/37th National bank. This is the link to their website: http://1337bank.money/

3) Her Twitter account is v0idcache. This was found simply by searching v0idcache on Twitter search. 

Her email is v0idcache@protonmail.com which was found on the her company website. The link to the website was found in her twitter profile.

She has contact with a user called Dev0id_cache on Twitter, who seems to be interested in pursuing a relationship with her.

4) Using centralops, the IP address for the company site is found to be 142.93.136.81, using an ip address locator, the server hosting the site is located in The Netherlands

5) There is a directory called /secret_directory on the website as seen on the robots.txt file. By inspecting the home page of the site a flag can be found, with the text {h1dd3n_1n_plain_5ight}

6) Ports 22 and 80 are open. OpenSSH utilizes port 22, while Werkzeug httpd utilizes port 80. This was found by searching the website's IP address on shodan. Port 1337 was found to be open on t1shopper, utilized by miceandmen.

7) The website is running on Linux, this was found out by searching the website on netcraft

Extra)
"CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5"}" Flag found on dnsdumpster

"CMSC389R-{"h1dd3n_1n_plain_5ight"}" Flag found by inspecting the website

### Part 2 (75 pts)

Using OSINT I'm able to find almost all the information needed to perform an attack on the server.  Given the domain name I can find out the IP address, and find exactly which ports are being utilized by the site.  With a username, IP address, and port, all that's left ot gain access is the password.  In this case it is a brute force method, where I use telnet to send login requests, given the username and a list of passwords from rockyou.txt.  I try each password until a successful login is made
