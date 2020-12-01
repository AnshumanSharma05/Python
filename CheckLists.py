#CheckLists
#Check if 2 lists are same.
L1=['A','B','C','D','E']
L2=['A','B','Cc','D','E']
result=True
for i,name in enumerate(L1):
    print("Iteration ", i," : ",name,",",L2[i])
    if name != L2[i]:
        result=False
        break
print("-------------------------------------------------")
print("Values in both lists are %s"%('same' if result else 'Not same'))