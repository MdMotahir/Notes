from collections import Counter
# l = [10,10,20,30,40,50,60,70] # here counter work  like a count function and give ans in a dicionary form
# c = Counter(l)
# print(c)
# print(c.get(70)) #here we use .get function for a proper key and value in a dictionary
#                 # here c is a dictionary and so get work like c.get(key) and gives the value of that proper key.





# l1 = [10,10,20,30,40,50,60,70,80]
# c1 = Counter(l1)

# l2 = [90,90,10,20,20,20,30,30,40,50,60,70]
# c2 = Counter(l2)

# print(c1,c2)    #here we get two dictionary by get function

# c1.update(c2) #here in c1 the values of c2 and c1 is added in one dictionary.
# print(c1)

# c1.subtract(c2) #here in c1 the values of c2 is substracted by c1. like in c1 the values of 90 is 0 but in c2 the values of 90 is 2
#                 # if we subsract then we get 0-2=-2 so in final dictionary we get the values of 90 is -2.
# print(c1)



from collections import ChainMap
import itertools

d1 = {1:1,2:4,3:9,4:16}
d2 = {5:25,6:36}
d3 = {7:49,8:64,9:81,10:100}

i = itertools.chain(d1,d2,d3)       # here we itrable at a time in many dictioary by useing itertools
# print(list(i))                # and also we dont do many things by this this is besically use for iterable.

j=ChainMap(d1,d2,d3) # here we make another tuple in which we get all of the dictionary in this we iterable and also do oher opperation
# print(j)
# for i,k in j.items():
#     print(i,k)


from collections import deque


# d = deque()
# d.appendleft(10)
# print(d)
# d.insert(1,20)
# d.insert(0,90) #here is the first one is the position of the second one like 90 is added in 0th position
# print(d)

# help(deque) #here its beter to take help of deque 

                                # deferance between list and linklist  

                    # List :
                    #     append => add element at last 
                    #     indexing and slicing 
                    #     pop => remove the elemnt from last 
                        
                    #     Costly operations :
                    #         insert => at start or in middle 
                    #         delete => from start or from middle 
                            
                    # Linklist :
                    #     insert => at start or in middle 
                    #     delete => from start or from middle 
                            
                    #     Costly :
                    #         append => add element at last 
                    #         indexing and slicing 
                    #         pop => remove the elemnt from last