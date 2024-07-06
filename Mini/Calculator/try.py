n = int(input("Numbers: "))
num = list(map(float, input().split()))
print(num)
add = sum(num)
print('sum:', add)
mult = 1
for i in num:
    mult = mult*i
print('multiplication: ', mult)
diff = 0
for i in num:
    diff = i - diff
    print('difference:', diff)

def division(a, b):
    divisor = 0
    dividend = input(f"please select Dividend among {int(a)} and {int(b)} : ")
    if dividend =="":
        print("This is error Input : ")
        division(a,b)
    dividend=float(dividend)
    if dividend == a:
        divisor = b
    elif dividend ==b:
        divisor =a
    else:
        print("Please enter correct value")
    div = dividend / divisor
    mod = dividend % divisor
    print(f'Quotient of {dividend} and {divisor} is: {div}')
    print(f'Remainder of {dividend} and {divisor} is: {mod}')