# Open lied.txt in Python
lied = open("hfst_1/opdrachten/lied.txt", "r")
# Vorm lied om naar lijst, vervang witregels '\n' door spaties ' ' 
lied = lied.read().replace('\n', ' ') 
# Test inhoud van lied
print(lied)

""" Begin eigen code hier """
dic = {}
for woord in lied.split():
    if woord in dic.keys():
        dic[woord] = dic[woord]+1
    else:
        dic[woord] = 1
print(dic)        
