auto_list = ['ford', 'audi', 'bmw', 'opel', 'reno', 'lada']

auto_dict = {'ford': 'America', 'audi': 'Germany', 'bmw': 'Germany', 'opel': 'Germany', 'reno': 'France', 'lada': 'Russia'}

auto_set = {'ford', 'audi', 'bmw', 'opel', 'reno', 'lada'}

print(type(auto_list), auto_list, sep='\n', end='\n\n')
print(type(auto_dict), auto_dict, sep='\n', end='\n\n')
print(type(auto_set), auto_set, sep='\n', end='\n\n')
#print(auto_dict['lada'])

print('Поиск элемента lada в списке:', auto_list.index('lada'))

for i in auto_dict.keys():
    if i == 'lada':
        print('Поиск элемента lada в словаре:',auto_dict[i])
        break

if 'lada' in auto_set:
    print('Поиск элемента lada в множестве:',True)

#Списки удобнее использовать, если необходима упорядоченность 
#элементов и возможность изменять последовательность на месте.

#Если порядок не важен и требуется работа с табличными данными,
#которые можно изменять на месте, то словари в этом случае предпочтительны. 

#Если порядок не важен и данные на месте изменять не требуется, то
#для работы с элементами подходят множества. Также подходят для работы с 
#математическими операциями над множествами.
