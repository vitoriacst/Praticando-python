n1 = int(input("write a value: "))
print(type(n1))
# the primitive type must be declared during variable declaration

n1 = int(input("write a number: "))
n2 = int(input("write a number: "))
sum = n1 + n2
# print('a soma entre',n1,'e',n2,'vale:',sum)
print('a soma entre {} e {} vale {} '.format(n1,n2,sum))
#usando o .format no print