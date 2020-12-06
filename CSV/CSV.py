import csv


#reader     [this gives a list]
#dict reader    {this gives a dictonary here key is a column name and the value is a row}


#writer [this is written in list]
#dict writer {this write in dict}
# fp=open("csv file.csv","r")
# reader= csv.reader(fp)  #here this gives in list
# reader= csv.DictReader(fp)  #here this gives a dict
# print(reader)
# print(next(reader))
# print(next(reader))
# print(next(reader))
# print(next(reader))
# print(next(reader))
# # print(next(reader))


# fp=open("csv file.csv","w")         #here if i go with w mode then all data which is present v=before are deleted
# fp=open("csv file.csv","a+")        #so here we go throgh the append + (a+) that add the data in the end of before data
# writer=csv.writer(fp,lineterminator="\n")
# writer.writerow(['poy','poy@gmail.com','6531546545'])
# writer.writerow(['mno','mno@gmail.com','6531546545'])
# writer.writerow(['gjhj','gjhj@gmail.com','6531546545'])
# fp.close()
# help(csv)