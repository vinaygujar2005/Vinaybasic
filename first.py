name=[]
sub1=[]
sub2=[]
sub3=[]
sub4=[]
sub5=[]
attan=[]
n=int(input("enter the number"))
for i in range(n+1):
    name1=input("enter the name")
    sub1a=int(input("enter the marks sub1: "))
    sub2b=int(input("enter the marks of sub2: "))
    sub3c=int(input("enter the marks of sub3: "))
    sub4d=int(input("enter the marks of sub4: "))
    sub5e=int(input("enter the marks of sub5: "))
    name.append(name1)
    sub1.append(sub1a)
    sub2.append(sub2b)
    sub3.append(sub3c)
    sub4.append(sub4d)
    sub5.append(sub5e)
print(name)
print(sub1)
print(sub2)
print(sub3)
print(sub4)
print(sub5)
allinfo=[name,sub1,sub2,sub3,sub4,sub5]
print(allinfo)
stu1info=[]
stu2info=[]
for i in allinfo:
    stu1info.append(i[0])
    stu2info.append(i[1])
print(stu1info)
print(stu2info)