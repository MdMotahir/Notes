# multi=lambda x,y: x*y
# print(multi(5,6))


# num=[24,62,25,49]
# even=map(lambda x: x%2==0,num)
# print(list(even))

# st=["my",'python']

# cap=map(lambda x: str.upper(x),st)
# print(cap)
# print(list(cap))

# num=[24,62,25,49]
# print(sorted(num,reverse=True))


                                                                # sorting

# marks=[('English', 95), ('Science', 95), ('Maths', 90), ('Social sciences', 88)]
# print(sorted(marks,key=lambda x: x[1]))
# print(sorted(marks,key=lambda x: x[0]))

                                                            
                                                            #even/odd and filter

# num=[24,62,25,49]
# evan=filter(lambda x: x%2==0,num)
# print(list(evan))
# odd=filter(lambda x: x%2!=0,num)
# print(list(odd))

                                                    
                                                        #filter according to length

# con=["india",'us','uk','france']
# cont_two=filter(lambda x: len(x)<=2,con)
# print(list(cont_two))


                                                    # reduce a expression using lambda 

# from functools import reduce
# num=[24,62,25,49]
# total=reduce(lambda x,y:x+y, num)
# print(total)

# num=[24,62,25,49]
# maxium=max(num)
# maxium_value=reduce(lambda x,y: min(x,y),num)
# print(maxium)
# print(maxium_value)
# minium=min(num)
# print(maxium,minium)


                                                        # this is for if and else
# max_val=reduce(lambda x,y: x if x>y else y, num)
# print(max_val)


# scores=[[1,35,80],[2,32,75],[3,30,82],[5,37,60]]
# abv_avg=35
# new_marks=map(lambda x: x[2]+2 if x[1]>abv_avg else x[2]-2,scores)
# print(list(new_marks))


                                                            # lambda on dictionary

# sales=[{'country':'india','sales':150.04},{'country':'china','sales':200},{'country':'uk','sales':185.05},{'country':'russia','sales':170.04}]

# country=map(lambda x: x['country'],sales)
# print(list(country))
# sale=map(lambda x: x['sales'],sales)
# print(list(sale))

                                                                # using filter in dictionary by lambda 
# sales=[{'country':'india','sales':150.04},{'country':'china','sales':200},{'country':'uk','sales':185.05},{'country':'russia','sales':170.04}]
# indiia_sales=filter(lambda x: x["country"]=='india',sales)
# print(list(indiia_sales))
# highest_p=filter(lambda x: x['sales']>180,sales)
# print(list(highest_p))


                                                            # passing multiples list useing lambda

# l1=[20,25,30,35,40]
# l2=[50,55,60,65,70]
# list_addition=map(lambda x,y: x+y,l1,l2)
# print(list(list_addition))


# a=[20,25,30,35,40] 
# xyz= map(lambda x:'same' if a == 100 else ('same as 50' if a == 50 else 'not same'),a)
# print(list(xyz))