str1 = "パトカー"
str2 = "タクシー"

i = 0
j = 0
k = 0
while(k<(len(str1)+len(str2))):
    if k % 2 == 0:
        print(str1[i],end="")
        i+=1
    else:
        print(str2[j],end="")
        j+=1
    k+=1    

print()