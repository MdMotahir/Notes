import pdb
def linear_search(l,key):
    for i in l:
        if i==key:
            return True
    else:
        return False

pdb.set_trace()
l=[10,20,30,40,50,60,80]
key=50
results=linear_search(l,key)
print(results)