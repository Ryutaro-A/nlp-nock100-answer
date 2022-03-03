def n_gram(n, list, words):
    # 文字n-gram
    for i in list:
        for j in range(len(i)-n+1):
            if (len(i)-n+1) < 1:
                break
            words.append("{0}".format(i[j:j+2]))

str1 = "paraparaparadise"
str2 = "paragraph"
X = []
Y = []
n_gram(2, str1.split(), X)
X = set(X)
n_gram(2, str2.split(), Y)
Y = set(Y)
print("和集合 : {0}".format(X | Y))
print("積集合 : {0}".format(X & Y))
print("差集合 : {0}".format(X - Y))

Z = X | Y
if 'se' in Z:
    print("seを含む")
else:
    print("seを含まない")

