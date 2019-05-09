# Crypto II Writeup

Name: Benjamin Chen
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Benjamin Chen

## Assignment Writeup

### Part 1 (70 Pts)

Flag: CMSC389R-{m3ss@g3_!n_A_b0ttl3}


### Part 2 (30 Pts)

![ecb](ecb.bmp)

![cbc](cbc.bmp)



1) In the ecb picture, the general shape of the image can still be determined, even if the colors are off.  In the cbc picture, no distinguishable image can be found, the colors are completely randomized.

2) ecb is less secure, as information can be gathered from the image even after encryption.  ecb uses the same encryption for each pixel, so pixels with the same image will be encrypted in the same fashion. While with cbc, each pixel bases its encryption off the previous pixels, so that each pixel encryption is different from the previous one.
