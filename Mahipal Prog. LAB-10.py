'''
#ques1

n=map(int,input().split())
v=int(input())
l=()
count1=0
count=0
for i in n:
    count+=1
    if i==v:
        count1+=0
    l+=(i,)
print('Tuple:',l)
print('Length:',count)
print('Count of ',v,':',count1)
#index in tuple prints first occurance so 
print('First index of ',v,':',l.index(v))


#ques2
v='aeiou'
def count_vowels(s):
    count=0
    for i in s:
        if i in v:
            count+=1
    print(count)
s=input()
count_vowels(s)


#ques3(1)
name=input().split()
count=0
largest=0
winner=''
l=[]

for i in name:
    count=0

    for j in name:
        if i==j:
            count+=1
            
    if i not in l:
        l.append(i)
        print(i,':',count)

    if largest<count:
        largest=count
        winner=i

print('Winner:',winner)


#ques3(ii)

name=input().split()
largest=0
winner=''
l=[]
dict1={}

for i in name:
    count=0
 
    for j in name:
        if i==j:
            count+=1
            
    if i not in l:
        l.append(i)
        print(i,':',count)
        dict1={'i':'count'}

    if largest<count:
        largest=count
        winner=i
print('Winner:',winner)


#ques4
w=input()
d={}
for i in w:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


#ques5
def simple_interest(p,r,t=1):
    return p*r*t/100
p=int(input())
r=int(input())
print('1 year:',simple_interest(p,r))
print('3 years:',simple_interest(p,r,3))


#ques6
def get_grade(marks):
    if marks>=80:
        return 'A'
    elif marks>=60:
        return 'B'
    elif marks>=40:
        return 'C'
    else:
        return 'F'
n=int(input())
d={}
for i in range(n):
    name,m=input().split()
    g=get_grade(int(m))
    print(name+':',g)
    if g in d:
        d[g]+=1
    else:
        d[g]=1
print('Grade count:')
print(d)


#ques7

t=tuple(map(int,input().split()))
l=()
for i in t:
    if i%2==0:
        l+=(i,)
print(l)


#ques8
n=int(input())
d={}
for i in range(n):
    c,cap=input().split()
    d[c]=cap
x=input()
if x in d:
    print(d[x])
else:
    print('Not found')
    
    
#ques9
n=int(input())
d={}
for i in range(n):
    item,qty=input().split()
    d[item]=int(qty)
q=int(input())
for i in range(q):
    a,item,k=input().split()
    k=int(k)
    if a=='SELL':
        if d[item]>=k:
            d[item]-=k
        else:
            print('Insufficient stock:',item)
    else:
        if item in d:
            d[item]+=k
        else:
            d[item]=k
for i in d:
    print(i,d[i])
    
    
#ques10
def stats(nums):
    return (min(nums),max(nums),sum(nums)/len(nums))
nums=list(map(int,input().split()))
print(stats(nums))
'''