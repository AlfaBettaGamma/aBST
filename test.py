from aBST import aBST

A = aBST(4)
for i in range(50):
    print(A.AddKey(i + 10))
print(A.Tree)
print(A.FindKeyIndex(245))
print(A.AddKey(226))