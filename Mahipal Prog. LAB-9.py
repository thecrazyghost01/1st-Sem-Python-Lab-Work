#ques1
'''
n=map(int,input().split())
e=[]
o=[]
for i in n:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print('Even:',e)
print('Odd:',o)


#ques2

n=(input().split())
l=[]
for i in n:
    if len(i)>3:
        l.append(i)
print(l)


#ques3

n=input().split()
w=0
t=0
b=0
l=[]
count=0
o=0
for i in n:
    count+=1
    if i=='W' or i=='w':
        w+=1
    elif i=='4' or i=='6':
        b+=int(i)
        t+=int(i)
        o+=int(i)
    else:
        t+=int(i)
        o+=int(i)
    if count%6==0:
        l.append(o)
        o=0
if o>0:
    l.append(o)
print('Total Runs:',t)
print('Wickets:',w)
print('Boundaries:',b)
print('Runs per over:',l)


#ques4

n=map(int,input().split())
s=999999999999999999999999999999999999
l=0
for i in n:
    if i>l:
        l=i
    if i<s:
        s=i
print('Largest:',l)
print('Smallest:',s)


#ques5

n=list(input().split())
longest=n[0]
for i in n:
    if len(i)>len(longest):
        longest=i
print(longest)


#ques6(imp)

item=list(input().split())
price=list(map(int,input().split()))
n=input().split()
t=0
order=[]
for i in n:
    if i not in order:
        order.append(i)
for i in item:
    if i in order:
        ocount=0
        for j in n:
            if i==j:
                ocount+=1
        p=price[item.index(i)]*ocount
        print(i, "x", ocount, "=", p)
        t+=p
print("Total:",t)


#ques7

n=input().split()
revn=''
for i in n:
    rev=''
    for j in i:
        rev=j+rev
    revn+=rev+' '
print(revn)


#ques8

n=input().split()
dig='1234567890'
l=[]
for i in n:
    for j in i:
        if j in dig:
            l.append(int(j))
sum1=0
for k in l:
    sum1+=k
print(l)
print('Sum:',sum1)


#ques9

n=int(input())
l=[]

for i in range(n):
    name=input().lower().split()
    name1=name[0]+'.'+name[1]

    count=0
    for j in l:
        if name1 in j:
            count+=1

    if count==0:
        l.append(f"{name1}@jklu.edu.in")
    else:
        l.append(f"{name1}{count+1}@jklu.edu.in")

for i in l:
    print(i)

#ques10

n=map(int,input().split())
count=0
l=[]
for i in n:
    if i==0:
        count+=1
    else:
        l.append(i)
for i in range(count):
    l.append(0)
print(l)
'''