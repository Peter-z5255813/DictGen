# DictGen
*By Peter Chen*
*A 2020/2021 project*

### *A personal project to create smarter dictionaries for offensive security purposes*


**DISCLAIMER**: This project is purely out of personal interest and is independent to my academic studies. Progress on this project may seem sporadic or inconsistent at times as I balance both work, studies and other commitments.

## Overview

Throughout my journey in offensive security, I have had hands on experiences with many well-designed and powerful tools in a variety of domains. Inspired by their craftsmanship and design, I myself have launched this project in order to work towards such high standards and provide additional experimental, alternatives to the community.

One of the tools I used quite often in Web Application testing were brute-forcers, in a variety of flavours and forms. *Dictionary Attacks* on *Username/Passwords* peaked my interest as passwords are often targeted for being the weakest point in the link; a combination of predictible human nature and the ignorance or negligence for a more complex, albeit, securer solution, are a fatal pairing for many security systems.

From my time in the field, the methodology for an attack did not differ. Once a login page was identified, a penetration tester would typically use a pre-existing dictionary and run a short pre-written python script to run the attack (or run a specialised tool such as *Burp Suite's Intruder*), often taking multiple hours at a time, depending on the given interface. 

Time is the main deterrent in these attacks. Although large and battle-proven dictionaries such as the infamous `rockyou.txt` contain 14,341,564 unique passwords, it is time consuming waiting around for all 14 million results to pass through, even considering other factors such as *Rate limiting* and *Network delays*. This leads onto the second unsolvable problem, to which dictionary attacks are not guaranteed methods of entry, making it frustrating for penetration testers.

My project is intended to alleviate the first problem of time. Through spending some short time performing reconnaissance on target individuals, `DictGen` intends to create 'targeted' dictionaries, featuring potential passwords that are tailored for the individual at hand. If these provided credentials are correct, this could dramatically reduce the time for an attack down to minute metrics, more reasonable and realistic for penetration testers. Despite this, I must acknowledge that this is not a guaranteed method to gain user access, thus alternative exploitation methods must be considered as contingencies.

## Design
<TODO>
- This section tends to update with every commit so for now i'll leave it as is
- Coming soon!
</TODO>

## Goals
***This section is subject to change over time***

I plan to have a working 1.0 version consisting of:
* Generation of dictionaries in text files for both usernames and passwords
* Takes in a wide range of entities.
* Offers basic/common password permutations.
* Offers basic/common username permutations

Once this version is released, I still intend to constantly expand and pursue other concepts which may offer increased performance or quality of life updates:

* Inbuilt HTTP based brute-force support
* Statistics reporting on generation
* Redundant or duplicate entity removal
* Additional permutation methods

I plan to test this software against certain username/password systems, either personally owned or completely consenting parties in order to test and improve the system at hand
