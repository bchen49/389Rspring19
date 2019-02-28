# Writeup 3 - Operational Security and Social Engineering

Name: Benjamin Chen
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Benjamin Chen

## Assignment Writeup

### Part 1 (40 pts)

-For the mother's maiden name, perhaps there is an old record where the mother's name is needed. If I say that the mother's name does not seem to be connected with Moffet's name, perhaps she'll ask me to try using her mother's maiden name.

-A similar technique can be used to extract the birth city, albiet these two pieces of information should not be asked for one after another. I can request say that her current address does not match with any user in my database, and ask for any previous addresses to see if they appear.

-The browser can be extracted by directing her to a fake link. When the link doesn't work I can say, "what browser are you using?", and just say that it only works on another browser.

-The name of her first pet could be extracted by playing a dog sound effect, and pretending like I was having trouble controlling my first pet. I could use this as a tangent and ask her if she has any tips from her first pet owning experience. 

-As for the pin number, I would probably pretend to be another branch of the bank asking to verify her pin number


### Part 2 (60 pts)

1) The first vulnerability is the open port 1337, the port does not seem to provide any useful service and only serves as an entry point for an attacker. I recommend closing this port as it is the one I used to gain entry to your website.

2) Related to your ports, I think it would be wise to install some sort of firewall to protect the ports that must be open. These ports are particularly vulnerable to the telnet attacks. 

3) The third vulnerability that I think you should look into immediately is updating your passwords. Your password was found using a brute force method by iterating through the leaked list of passwords from rockyou.  I recommend using a more secure password, one that would be difficult, if not impossible to brute force.