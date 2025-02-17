#1st
total_price = int(input('Общая стоимость часов: '))
print(int((total_price-96*48)/6))

#2nd
country = input().split()
for i in country: print(i.title())



#3rd
prises = input().split()
sum_price = int(prises[0]) + int(prises[1])
print(sum_price)



#4th
print(1+1*7**4)


#5th
#print((round((float(input())) * 0.19), 2))

sales = float(input())
sales = sales*0.19
print('%.2f'% sales)

#print(round(float(input()) * 0.19, 2)) - shorter variant


#6th
import math
mass = int(input())*0.453592
leg = int(input())*0.0254
print(math.ceil((mass/(leg**2))*100)/100)

#7th
print(1000000*0.1) # one million sq decimetres * 1/10 decimetres

from os.path import split

#8th
data_list = input().split()
print(int(data_list[1])//(int(data_list[0])+1))

#9th
bulls_num = int(input())
tribe_num = int(input())
print(bulls_num % tribe_num)


#10th
import math
metre = int(input()) / 1609.344
print(math.floor(metre)) #final task