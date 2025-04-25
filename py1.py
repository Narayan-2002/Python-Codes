# Sum of all digits of any numbers
print("\t\t\tSum of all digits of any numbers\n")
a=int(input('enter a number: '))
sum=0
print(f"the sum of the number {a} is: ")
while a>0:
    digit=a%10
    sum+=digit
    a//=10
print(sum)

#Sum of all even digits of any number
print("\n\t\t\tSum of all even digits of any number\n")
a=int(input("enter a number: "))
sum=0
print(f"sum of all even digits on this number {a} is: ")
while a>0:
   digit=a%10
   if digit%2==0:
      sum+=digit
   a//=10
print(sum)

# Sum of all odd digits of any number
print("\n\t\t\tSum of all odd digits of any number\n")
a=int(input("enter a number: "))
sum=0
print(f"sum of all odd digits on this number {a} is: ")
while a>0:
   digit=a%10
   if digit%2!=0:
      sum+=digit
   a//=10
print(sum)

#Sum of all prime digits
import math
print("\n\t\t\tSum of all prime digits\n")
a=int(input("enter a number: "))
sum=0
print(f"sum of all prime digits on this number {a} is: ")
while a>0:
   digit=a%10
   if digit in [2,3,5,7]:
     sum+=digit
   a//=10 
print(sum)

# Difference between average of all even digits except divisible by
# 4 and avearge of all odd digits except divisble by 3
print("\n\t\t\tDifference between average of all even digits except divisible\n\t\t\tby 4 and avearge of all odd digits except divisble by 3\n") 
a=int(input("enter a number: "))
ce,co,se,so=0,0,0,0
print(f"diference between the average of even number and odd number present in the number {a} is: ")
while a>0:
   digit=a%10
   if digit in [2,6,8]:
      ce+=1
      se+=digit
   elif digit in [1,5,7,9]:
      co+=1
      so+=digit
   a//=10
dif=se/ce-so/co
print(dif)

# Find kth digit from frontside or back side of any digits number
# and find its poistional value
print("\n\t\t\tFind kth digit from frontside or back side of any digits number \n\t\t\tand find its positional value\n")
a=int(input("enter a number: "))
k=int(input("enter kth value: "))
i=1
print(f"{k}th postion digits of this number {a} of positional value is: ")
while a>0:
   digit=a%10
   if k==i:
      for j in range(1,k):
         digit=digit*10
      break
   a//=10
   i+=1
print(digit)
# Sum of product of consecutive digits of any digit number
print("\n\t\t\tSum of product of consecutive digits of any digit number\n")
a = input("Enter a number: ")
sum= 0
for i in range(len(a) - 1):
    product = int(a[i]) * int(a[i + 1])  
    sum+= product  
print("Sum of product of consecutive digits:", sum)

# Sum of product of consecutive even digits of any digit number
print("\n\t\t\tSum of product of consecutive even digits of any digit number\n")
num = input("Enter a number: ")
sum_of_products = 0
digits = [int(d) for d in num]
for i in range(len(digits) - 1):
    if digits[i] % 2 == 0 and digits[i + 1] % 2 == 0:
        sum_of_products += digits[i] * digits[i + 1]
print("Sum of product of consecutive even digits:", sum_of_products)

# Sum of product of consecutive odd digits of any digit number
print("\n\t\t\tSum of product of consecutive odd digits of any digit number\n")
num = input("Enter a number: ")
sum_of_products = 0
for i in range(len(num) - 1):
    if int(num[i]) % 2 == 1 and int(num[i + 1]) % 2 == 1:
        sum_of_products += int(num[i]) * int(num[i + 1])
print("Sum of product of consecutive odd digits:", sum_of_products)


# Sum of product of consecutive prime digits of any digit number
print("\n\t\t\tSum of product of consecutive prime digits of any digit number\n")
num = input("Enter a number: ")
prime_digits = {'2', '3', '5', '7'}
sum_of_products = 0
for i in range(len(num) - 1):
    if num[i] in prime_digits and num[i + 1] in prime_digits:
        sum_of_products += int(num[i]) * int(num[i + 1])
print("Sum of product of consecutive prime digits:", sum_of_products)

# Difference between Sum of product of consecutive even digits
# except 2 and 6 and Sum of product of consecutive odd digits
# except 3 and 7 of any digit number
print("\n\t\t\tDifference between Sum of product of consecutive even digits\n\t\t\texcept 2 and 6 and Sum of product of consecutive odd digits\n\t\t\texcept 3 and 7 of any digit number\n")
num = input("Enter a number: ")
even_product_sum = 0
odd_product_sum = 0
even_exclude = {'2', '6'}
odd_exclude = {'3', '7'}
for i in range(len(num) - 1):
    digit1 = num[i]
    digit2 = num[i + 1]    
    if digit1.isdigit() and digit2.isdigit():
        d1 = int(digit1)
        d2 = int(digit2)      
        if d1 % 2 == 0 and d2 % 2 == 0 and digit1 not in even_exclude and digit2 not in even_exclude:
            even_product_sum += d1 * d2       
        if d1 % 2 == 1 and d2 % 2 == 1 and digit1 not in odd_exclude and digit2 not in odd_exclude:
            odd_product_sum += d1 * d2
difference = abs(even_product_sum - odd_product_sum)
print("Difference:", difference)