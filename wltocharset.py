def main():
    with open('wordlist.txt') as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in open('wordlist.txt')]
    print(lines)

if __name__ == '__main__':
    main()
