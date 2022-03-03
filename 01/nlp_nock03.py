import re

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = str.replace(",", "").split()
num_list = []

for i in list:
    num_list.append(len(i))

num_list.sort(reverse=True)
for i in num_list:
    print(i)
