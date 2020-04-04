'''
program pangkat
'''

# cara pertama
def pangkat(num1,num2):
    number = 1
    for _ in range(num2):
        number *= num1
    return number

# cara kedua
def pangkat1(x,y):
    if y ==0:
        return 1
    else:
        return x*pangkat(x,y-1)

print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))
        
print(pangkat1(2,2))
print(pangkat1(3,3))
print(pangkat1(10,5))