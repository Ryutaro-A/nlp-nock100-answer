import random

str = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
list1 = str.split()

list2 = []

for i in list1:
    if len(i) <= 4:
        continue
    list2.append(i[0] + "".join(random.sample(i[1:len(i)-1], len(i)-2)) + i[len(i)-1])

sentence = " ".join(list2)
print(sentence)
