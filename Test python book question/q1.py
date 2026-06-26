# Q1.1
print("Thank You God!") #Output: Thank You God!

# Q1.2
x = "Pinky"
print("Believe in yourself", x) #Output: Believe in yourself Pinky

# Q1.3
print("3 raised to power 4 = ", 3**4 ) #Output: 3 raised to power 4 =  81

# Q1.4
m = 10
n = 20
print(m, "+", n, "=", m+n) #Output: 10 + 20 = 30

# Q1.5
print(2+4,6/3,90*8) #Output: 6 2 720

# Q1.6
x = input() #Input: 12
print(x) #Output: the value entered by the user here 12

# Q1.7
x1 = int(input("Enter an integer number ")) #Input: 23
print(x1) #Output:The value entered by the user here 23

# Q1.8
# x = input() #Input: 12
# x1 = int(input('Enter an integer number')) # input: 23
# print(x1 + x) #Output: Error
# 
# Q1.9
# val = int(input('Enter a floating value: ')) #input: 23.7
# Output : Error
# 
# Q1.10
int1 = float(input('Enter a floating value: ')) #input: 23
print(int1) #Output: 23.0

# Q1.11
import string
for i in range(5):
    print(repr(i).rjust(5)) #Output: 0 1 2 3 4 in seprate lines

# Q1.12
"12".zfill(5) #Output: 00012

# Q1.13
print('{0:.3f}'.format(5.7416)) #Output: 5.742

# Q1.14
print('{0:.6f}'.format(5.9456)) #Output: 5.945600

# Q1.15
# print('{4:.3f}'.format(8.2496)) #Output: Error

# Q1.16
print('{0:9.3f}'.format(9.1011)) #Output: 9.101

# Q1.17
for x in ['Sunny','Monty']:
    print('Hi "{} !"'.format(x)) #Output: Hi Sunny! <new line> Hi Monty!
# 
# Q1.18
print('{0:3d},{2:6.1f},{1:4d}'.format(1,2,3.0)) #Output:'  1,   3.0,   2'
# 
# Q1.19
print('{0:3},{1:5},{2:6}'.format('Hello1','Bye2',3)) #Output: Hello1, Bye2,     3

# Q1.20
count = {
    'Unit':1,
    'Tenth':10,
    'Hundedth':100
}
for key, value in count.items():
    print('{0:10} ==> {1:10d}'.format(key,value)) #Output: Unit       ==>          1<newline>Tenth      ==>         10<newline>Hundedth   ==>        100
