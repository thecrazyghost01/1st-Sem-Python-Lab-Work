'''
#1
n=input()
rev=''
for i in n:
    rev=i+rev
print(rev)


#2
n=input()
rev=''
count=0
for i in  n:
    rev=i+rev
for j in rev:
    if j!=' ':
        count+=1
    elif j==' ':
        break
print(count)


#3 inbuilt
sentence=input()
word=input()
if word in sentence:
    print('Yes')
else:
    print('No')
print(sentence.count(word))

#3 non-inbuilt
sentence=input()+' '
word=input()
wnew=''
count=0
for i in sentence:
    if i!=' ':
        wnew+=i
    else:
        if wnew==word:
            count+=1
            wnew=''
if count>0:
    print('Yes')
    print(count)
else:
    print('No')


#4
n=input().lower()
main='abcdefghijklmnopqrstuvwxyz'
mnew=''
for i in n:
    if i in main and i not in mnew:
        mnew+=i
if len(mnew)==len(main):
    print('Pangram')
else:
    print('Not a Pangram')


#5
s=input('Enter the String:')
shift=int(input('Enter the Shift:'))







'''
#6
































