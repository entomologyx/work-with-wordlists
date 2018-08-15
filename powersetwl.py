#this script is used to write to wordlist.txt(needs to be manually created in same folder as powersetwl.py) a powerset of all  #combinations of a charset
import itertools


charset = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h' ,'i' , 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
      'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2' , '3', '4', '5', '6', '7', '8', '9', '0']
            
def main():
    pwlen = 3
    combinations = list(itertools.combinations(charset, pwlen)) #create all possible tuples of specific length 
    file = open("wordlist.txt", "w")
    for i in combinations:
        file.write(''.join(i)+"\n") #merges and writes them to wordlist.txt
    file.close()

if __name__ == '__main__':
    main()

