import sys

file=sys.argv[1]
names=sys.argv[2]
dict={}
name_list=names.split(",")

students=open(file,"r")

listed_students=[]
for i in students:
    i=i.replace("\n","")
    i=i.split(":")
    dict[i[0]]=i[1]

for i in name_list:
    try:
        print(f"Name:{i} ,University: {dict[i]}",end="")
    except:
        print(f"No record of {i} was found!")

    


    



