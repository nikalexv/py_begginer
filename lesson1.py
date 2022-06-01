#1
s = 0
for i in range(88888889):
    s += i
print('#1', (s), sep='\n', end = '\n\n')

#2
list1 = [3, 4, 56, 100, 2, 2, 3]
print('#2', round(sum(list1)/len(list1),3), sep='\n', end='\n\n')

#3
st1 = 'asdxfghyxyx'
st2 = ''
for c in st1:
    if c == 'x':
        st2 += 'y'
    else:
        st2 += c 
print('#3', st2, sep='\n', end='\n\n')
      
#4
p = 1
list2 = [3, 4, 56, 100, 15, 2, 20, 30]
for i in list2:
    if i % 3 == 0 and i % 5 == 0:
        p *= i
print('#4', p, sep='\n', end='\n\n')

#5
print('#5', st1.replace('x','y'), sep='\n')

