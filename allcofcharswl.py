# this script is used to create a wordlist of the powersets of a charset up until a specific length(pwlen). 
import itertools
from itertools import product
charset = ['a', 'b', 'c', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def main():
    pwlen = 2
    combinations = []

    file = open("wordlist.txt", "w")


    for i in range(pwlen+1):
        combinations.append(list(product(charset, repeat=i)))
    
    for j in range(len(combinations)):
        for k in combinations[j]:
            try:
                file.write(''.join(k) + "\n")  # merges and writes them to wordlist.txt
            except TypeError:
                pass
    file.close()
if __name__ == '__main__':
    main()

