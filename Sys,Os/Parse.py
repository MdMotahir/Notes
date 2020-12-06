import sys
# print(sys.argv)
sys.argv

# num1=int(sys.argv[1])
# num2=int(sys.argv[2])
# fs=open("sys_output.txt",'w')
# sys.stdout=fs           #here stdout is a attribut for output
# fp=open("sys_error.txt",'w') #here 1st one is file name where our error in store
# sys.stderr=fp       #here stderr is a attribut for error
# # print(25/15)
# print(0/10)
# print(10/0)

# print('hi python')


# print(sys.platform) #here we have os is win32 to know this we use sys.plateform

import os
print(os.listdir()) #in this directory we get all file
# print(os.getcwd())      #show the corrent directory where i generaly work.ArithmeticError
# print(os.chdir('name')) #by useing this we change the directory so in name field we appy the name of directory which we want o change.


            #so by importing os we can change our directory and import the file.

print(os.system("new.py")) #here we executeing any file from any python file
