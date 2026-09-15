#Number
print(2 * 3)
print(2 ** 3)
print(0.2 + 0.1)
print(3 * 0.1)

universe_age = 14_000_000_000
print(universe_age)

fav_num = 114514
print("My favorite number is " + str(fav_num) + ".")
print(f"My favorite number is {fav_num}.") 

#zakozakozakozakozakozakozakozakozakozakozakozakozakozako

#Zen of Python
import this

#List []
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[-1])
message = f'My first bicycle was a {bicycles[2].title()}.'
print(message)

names = ['Liu Bei', 'Guan Yu', 'Zhang Fei']
print(names[0])
print(names[1])
print(names[-1])
print(f'{names[0]} 还是个忠厚人啊')

names = ['Liu Bei', 'Guan Yu', 'Zhang Fei']
names[0] = 'Cao Cao'
print(names)
names.append('Sun Quan')
print(names)
names.insert(1, 'Zhuge Liang')
print(names)
del names[0]
print(names)
poped_names = names.pop()
print(poped_names)
print(f'Poped name is {poped_names}.')
erdi = names.pop(1)
print(f'My {erdi} id unstoppable.')
names.remove('Zhang Fei')
print(names)

names = ['Liu Bei', 'Guan Yu', 'Zhang Fei']
sandi = 'Zhang Fei'
names.remove(sandi)
print(f'\n{sandi} lost Xuzhou.')
print(f'len(names) = {len(names)}')





