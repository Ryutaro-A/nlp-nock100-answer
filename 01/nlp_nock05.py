def n_gram(n, list):
    words = []
    # 単語n-gram
    print("単語{0}-gram".format(n))
    for i in range(len(list)-n+1):
        print(" ".join(list[i:i+2]))

    print()
    
    # 文字n-gram
    print("文字{0}-gram".format(n))
    for i in list:
        print("{0} : ".format(i), end="")
        for j in range(len(i)-n+1):
            if (len(i)-n+1) < 1:
                break
            print("\"{0}\" ".format(i[j:j+2]), end="")
        print()

str = "I am an NLPer"
n_gram(2, str.split())

