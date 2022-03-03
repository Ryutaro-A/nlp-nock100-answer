def cipher(sentence):
    list = []
    for i in sentence:
        if i.islower():
            list.append(chr(219-ord(i)))
        else:
            list.append(i)
    return "".join(list)

def main():
    str = "I Am An Engineer"
    print(cipher(str))

if __name__ == '__main__':
    main()