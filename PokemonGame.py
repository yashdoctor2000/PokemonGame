x=int(input("Enter the how many pokemon card you want to train "))
a=[]
for i in range(x):
    b= int(input("Enter the "+str(i+1)+" Card number "))
    a.append(b)
max_num=a[0]
min_num=a[0]
for i in range(len(a)):
    max_num=max(max_num,a[i])
    min_num=min(min_num,a[i])
    print(min_num,max_num)