'''
program balik element list
'''
# cara pertama
def balikposisi(x):
    y = []
    length = len(x)
    for item in range(length):
        y.append(x[(length-item-1)])
    return y

# cara kedua
def balikposisi1(mylist):
    hasil = []
    for i in range(len(mylist)):
        hasil.insert(0,mylist[i])
    return hasil

print(balikposisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikposisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikposisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))

print(balikposisi1([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikposisi1(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikposisi1(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))