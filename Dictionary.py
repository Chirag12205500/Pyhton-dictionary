dict = {'one': 1, 'two': 2}
print(dict)
print(dict["one"])
#priint(dict['three])
month = {'jan': 1, 'feb': 2, 'march': 3}
print(month)
print(type(month))
print(month.get('feb'))
mydict = {"game": "chess", "dish": "chicken", "place": "home"}
print(mydict.get('game'))
print(mydict['dish'])
a = {'1':"one", '2': "two"}
print(a.get('1'))
(a['1']) = "xyz"
print(a)

a = [1, 2, 3]
a[0] = 100
print(a)

d = dict([('one', 1), ('two', 2)])
print(type(d))
print(d)

a = {'one': 1, 'two': 2, 'three': 3}
del a['two']
print(a)

list1 = [10,20,30]
result = zip(list1)
print(result)

list2 = [40,30,20]
list3 = ["Ten", "Twenty", "Thirty"]
dict1 = dict(zip(list2,list3))
print(dict1)
print(dict)
print(sorted(dict1))
print(sorted(dict1.items()))

data1 = input("data1:")
data2 = input("data2:")
list1 = data1.split(",")
list2 = data2.split(",")
mydict = dict(zip(list1,list2))
print("list1:",list1)
print("list2:",list2)
print("dictionary:",sorted(mydict.items()))

#Program to create a dictionary from 2 lists
data1 = input("data1:")
data2 = input("data2:")
L1 = data1.split(",")
L2 = data2.split(",")
d1 = {}
if(len(L1) == len(L2)):
    for i in range(len(L1)):
        d1[L1[i]] = L2[i]
    print(sorted(d1.items()))
else:
    print("length should be equal")

dict1 = {1:"one", 2:"two"}
print(5 in dict1)
print(5 not in dict1)

data1 = input("data:")
data2 = input("data2:")
L1 = data1.split(",")
L2 = data2.split(",")
dict1 = dict(zip(L1,L2))
for key, value in sorted(dict1.items()):
    print(key,value)





