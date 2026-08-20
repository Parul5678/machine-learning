print('hello world')
print(10 + 20)
print(10 * 20)
print("parul's pc")
name = 'parul'
print(name + ' malhotra')
print(name[2:4])
print(name[-1])

#list
characters = ['harry', 'ron', 'draco', 'hermoine']
print(characters)

houses = ['gryfinndor', 'ravenclaw', 'slytherin', 'hufflepuff']
mix = [characters, houses]

print(mix)
#tupple

tup = ('harry', 'ron', 'draco', 'hermoine')
print(type(tup))

tup2 = (34, [2,4,5,8])
print(tup2)

#set
house_set = {'gryfinndor', 'ravenclaw', 'slytherin', 'hufflepuff', 'gryfinndor'}
print(house_set)

set2 = set() #empty set
print(set2)

#dictonary
data = {0:24,1:56,2:78,3:54,4:67} #keys are set and values are list
print(data[2])
keys = {'hello', 'world'}
values = [0,1]
dict1 = dict(zip(keys, values))
b = 5
a = 5
print(id(a))

c = 6 +8j
print(c)
a1 = 2
b1 = 3
c1 = complex(a1,b1)
print(c1)
greater = b<a
is_it = True
k = int(True)
a < 10 and b > 1 #true and true
a < 10 and b > 1 #true and true
