# 1. Pattern extraction : from a file extract only emails
# 2. Pattern Validation : given an email address validate if its a valid email address or not
#  for email if 
                    # 1. only @
                    # 2. after @ there will be domain name 
                    # 3. before @ a set of alpha numneric char
                    # 4. . , _  abc.a_3


import re
# r = re.compile("ab")
# s = "abcdababcdabab"
# l = re.findall(r,s)
# print(l)


                            # Metachar:
                            #     [a-z] : char class : 1 occurance of [a-z] a or b or c or d or ......... or z 
                            #     [0-9] : digit class  [0-9] : 1 occurance 
                            #     [A-Za-z0-9]
                            #     + : atleast one occ should be there if more thats fine 
                            #     * : zero or more occ are allowed
                            #     ^ : start of the string 
                            #     $ : end of the string 
                            #     [0-9]{5}
                            #     [a-z]{2,5}
                            #     ? : optional


# d=input('input your date:- ')
# # d = "11-12-2010"
# r = re.compile("^(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})")
# m =  re.search(r,d)
# # if int(m.group(1))<=31 and int(m.group(2))<=12:
# #     print(m.group())
# # else:
# #     print("Invalid date")


# if int(m.group(2))==2 and int(m.group(3))%4==0:
#     int(m.group())<=29
# elif int(m.group(2))<=12 and int(m.group(2))%2!=0 or int(m.group(2))==7 and m.group(1)<=31:
#     print(m.group())
# elif int(m.group(2))<=12 and int(m.group(2))%2==0 and int(m.group(1))<=30:
#     print(m.group())
# else:
#     print("Invalid date")
