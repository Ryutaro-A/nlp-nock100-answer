import MeCab

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
with open("neko.txt") as f:
    sentence = f.read()

sent = mecab.parse(sentence)
with open("neko.txt.mecab", "w") as f:
    f.write(sent)
