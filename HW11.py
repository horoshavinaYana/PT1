# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 


a=int (input ("введите трехзначное число - "))
sum=0
while a!=0:
    sum+=a%10
    a//=10
print (sum)