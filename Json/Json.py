import json
fp = open("New.json","r")
content=fp.read() #here our conent in a  json
# print(content)
d=json.loads(content) #here json.loads(content) that contant change into a python file.
# print(d['glossary']['title'])
# print(d)

        #after change json into python then we change or modify that
                #and also do our work what we want.


j=json.dumps(d,indent=3) #here json.dumps(filename) convert the python file ino json
                        # and the indent is change the step of json file we use here 3 steps of json

# print(j)


fp1=open('newjson.json','w')
fp1.write(j)
fp1.close()
fp.close()