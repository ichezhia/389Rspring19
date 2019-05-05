# Crypto II Writeup

Name: Iniyan Chezhian
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Iniyan Chezhian

## Assignment Writeup

### Part 1 (70 Pts)
I started by running the following:
`gpg --decrypt message.txt.gpg`

This gave me some text about the imported key, which is: `2CDD23F9C7D32E64`

Then I did:
`gpg --decrypt message.txt.gpg`

This gave me a lot of text in the message, I was told to mention this flag: `CMSC389R-{m3ss@g3_!n_A_b0ttl3}`

Following the instructions from the previous file, I created a signature.txt file and ran this command:

`gpg --clearsign signature.txt`

This created the `signature.txt.asc` file. This file is included in this directory.

### Part 2 (30 Pts)
I ran the given 2 commands, which made a new image file each. Then `bash fix.sh` ran the given script. Both files made, along with the original are included in this directory.

Both images seem to be grainier greyed out versions of the original image. cbc is more grainier, looking like a TV screen that is when you are on a channel that does not exist. ecb is somewhat recognizable in terms of the original image.

Judging from the image, ecb is less secure, and cbc is more secure. The cbc image completely conceals the original image, while with ecb I can still make out the original. From online sources, I see that ECB is a simpler raw cipher and each block is encrypted independently; while CBC is cipher block chaining where each block is chained together and each encrypted block is XOR'd with the last encrypted block.

An analogy that I can think of is that ECB is like a hash, while CBC reminds me of a blockchain.
