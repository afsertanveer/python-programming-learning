number=[1,2,3,4,5]
number.append(6)
number.insert(0,-1)
print(number)
number.remove(-1)
print(number)
print(1 in number)
print(10 in number)
print(len(number))
numbers= [5, 1, 30,20]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers2 = numbers.copy();

numbers2.append(100);
print(numbers,numbers2)