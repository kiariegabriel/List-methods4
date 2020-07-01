l=eval(input('Enter a list\n'))
m=eval(input('Enter a list\n'))
n=[]
for i in range(len(l)):
	n.append(l[i]+m[i])
print(n)