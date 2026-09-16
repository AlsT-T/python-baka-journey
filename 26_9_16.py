#管理列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
print(sorted(cars))
print(sorted(cars, reverse = True))
cars.sort(reverse = True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
#reverse() method is not sorting the list, it just reverses the order of the list.
#sort(reverse = True) method is sorting the list in reverse order.
print(len(cars))

travels = ['Xiamen', 'Dali', 'Guilin', 'Zhangjiajie', 'Shanghai']
print(travels)
print(sorted(travels))
print(sorted(travels, reverse = True))
print(travels)
travels.reverse()
print(travels)
print(len(travels))

#for循环
waifu = ['Kisaki', 'Hina', 'Hoshino', 'Seia', 'Alice']
for waifu in waifu:
    print(waifu) #注意缩进

waifu = ['Kisaki', 'Hina', 'Hoshino', 'Seia', 'Alice']
for my_waifu in waifu:
    print(f'My waifu is {my_waifu}.')
    print(f'{my_waifu} is my waifu.\n') #若本行未缩进，只会再循环结束后运行一次
#\n每次循环后插入一个空行
print('All waifus are my waifus.')

foods = ['Ma Po Tofu', 'Chongqing Hotpot', 'Beijing Roast Duck', 'Guangzhou Dim Sum']
for food in foods: #如果都用food作为循环变量名，for循环结束后，food的值会是foods列表的最后一个元素
    print(f'I love {food}')
print(f'My favorite food is {foods[0]}') 

for value in range(1, 5):
    print(value) #range()函数生成一个数字序列，默认从0开始，直到指定的数字前一位结束

nums = list(range(1, 6))
print(nums)

even_nums = list(range(2, 11, 2)) #range()函数的第三个参数表示步长
print(even_nums)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))
print(list(range(1, 11))) #list()函数将range()函数生成的数字序列转换为列表

#List Comprehesion 列表推导式
squares = [value ** 2 for value in range(1, 11)]
print(squares)

print(sum(list(range(1, 101))))
print(sum(list(range(1, 101, 2))))
print(list(range(3, 31, 3)))

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

waifus = ['Kisaki', 'Hina', 'Hoshino', 'Seia', 'Alice']
print(waifus[1:3])
print(waifus[2:])
print(waifus[:4])
print(waifus[-3:])
print(f'\nHere are my waifus:')
for waifu in waifus[:3]:
    print(waifu.title())

waifus = ['Kisaki', 'Hina', 'Hoshino', 'Seia', 'Alice']
wifes = waifus[:]
print(f'\nMy waifus are:')
print(wifes)
waifus.append('Rossi')
wifes.append('Suzuran')
print(f'\nMy waifus are:')
print(waifus)
print(f'\nMy wifes are:')
print(wifes)


