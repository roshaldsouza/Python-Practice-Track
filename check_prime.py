def check_prime(num):
    for i in range(2,num // 2):
        if num % i == 0:
            return "Not prime"
        else:
            return "prime"
num = int(input("enter a number "))
res = check_prime(num)
print(res) 

