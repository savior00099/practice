def main():
    text = input("input: ")
    l = ['a', 'A', 'E', 'I', 'i', 'O', 'o', 'U', 'u']
    out = ""

def shorten(word)
    try:
        if word[0] in l:
            out += word[0]
        else:
            for i in range(len(word)):
                if word[i] in l:
                    out += word[i]
                    break
if __name__ == "__main__":
    main()                

