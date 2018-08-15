# work-with-wordlists
some python3 scripts to merge and create wordlists  
wordlists are always in the format that each word is separated by a new line    

todo:  
- make scripts run faster for big wordlists

usage:  
these scripts don't accept parameters from console, you have to edit the .py file according to your needs  
charset = set of characters or strings used  
pwlen = length of the password you want to crack or max length of password you want to crack  
you always need to create or have the .txt file you want to write/read in the same directory as the script. Standard name is wordlist.txt

powersetwl.py:   
creates a wordlist containing the powerset of a given charset with a fixed length. You probably have to manually edit the length("pwlen":default = 3) and the charset(default = all upper and lowercase letters + numbers 0-9), also create the file wordlist.txt in the same folder as powersetwl.py since the output will be written to this file.  
e.G.: charset = ['a', 'b', 'c', 'd']; pwlen=3 -> abc abd acd bcd 


powersetwlupuntil.py:  
creates a wordlist containing powersets of a given charset up until a fixed length. For further usage see powersetwl.py  
e.G.: charset = ['a', 'b', 'c' ]; pwlen = 3 -> a b c ab ac bc abc

flallcofcharswl.py:  
creates a wordlist containing all combinations of a charset(default=all lower and upercase letters + numbers 0-9) of a fixed length(pwlen)  
e.G.: charset = ['a', 'b', 'c' ]; pwlen = 3 -> aaa aab aac aba abb abc aca acb acc baa bab bac bba bbb bbc bca bcb bcc caa cab cac
cba cbb cbc cca ccb ccc



wltocharset.py:  
takes a wordlist(needs to be named wordlist.txt) and gives out a ready to use charset list to the console which you can use in the other provided scripts that work with charsets
