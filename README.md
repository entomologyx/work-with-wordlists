# work-with-wordlists
some python scripts to merge and create wordlists

usage:

powersetwl.py: creates a wordlist containing the powerset of a given charset with a fixed length. You probably have to manually edit the length("pwlen":default = 3) and the charset(default = all upper and lowercase letters + numbers 0-9), also create the file wordlist.txt in the same folder as powersetwl.py since the output will be written to this file.
e.G.: charset = ['a', 'b', 'c', 'd']; pwlen=3 -> abc abd acd bcd 
