import random

with open("./NewsAggregatorDataSet/newsCorpora.csv") as f:
    lines = f.read().split("\n")

articles = []
for line in lines:
    words = line.split("\t")
    if words[0] != "":
        if words[3] == "Reuters" or words[3] == "Huffington Post" or words[3] == "Businessweek" or words[3] =="Contactmusic.com" or words[3] == "Daily Mail":
            if words[4] == "b" or words[4] == "t" or words[4] == "e" or words[4] == "m":
                articles.append([words[4], words[1]])

random.shuffle(articles)
print(len(articles))
n = int(len(articles) * 0.8)
m = int(len(articles) * 0.1)
k = int(len(articles) * 0.1)
with open("train.txt", "w") as f:
    print(n)
    for i in range(n):
        f.write("{0}\t{1}\n".format(articles[i][0], \
        articles[i][1].rstrip("...")))
with open("valid.txt", "w") as f:
    print(m)
    for i in range(n, m+n):
        f.write("{0}\t{1}\n".format(articles[i][0], \
        articles[i][1].rstrip("...")))
with open("test.txt", "w") as f:
    print(k)
    for i in range(m, k+m):
        f.write("{0}\t{1}\n".format(articles[i][0], \
        articles[i][1].rstrip("...")))