# this script is used to create a wordlist of all the combinations of a charset of a specific length. 
import itertools
from itertools import product
charset = ['a', 'b', 'c','e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

pwlen = 3
def main():

    combinations = []

    file = open("wordlist.txt", "w")
    combinations = list(product(charset, repeat=pwlen))

    for i in combinations:
        file.write(''.join(i) + "\n")  # merges and writes them to wordlist.txt



    file.close()
if __name__ == '__main__':
    main()
