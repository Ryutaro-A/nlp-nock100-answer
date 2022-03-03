str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = str.split()
map = {}

for i, word in enumerate(list):
    if i == 1 and i == 5 and i == 6 and i == 6 and i == 7 and i == 8 and i == 9 and i == 15 and i == 16 and i == 19:
        map[word[0]] = list.index(word)
    else:
        map[word[:2]] = list.index(word)

for key in map.keys():
    print("{0} : {1}".format(key, map[key]))
