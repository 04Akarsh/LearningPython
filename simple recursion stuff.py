#FINDING FACTORIAL WITH RECURSION
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1) * n #bruh confusing stuff
n = int(input('Ayo enter the number to find factorial: '))

print(fact(n))

#Compute compound interest with recursion
def get_total_balance(amount, rate, years):
    # THE STOP SIGN 
    if years == 0:
        return amount  # The race is over, just return the final money.

    # THE WORK 
    # We do ONE year of math right now.
    new_amount = amount * (1 + rate / 100)

    # THE HAND-OFF (The Recursion) 
    # We call the function AGAIN, but with the NEW amount 
    # and ONE LESS year to process.
    return get_total_balance(new_amount, rate, years - 1)
amount = int(input('input principle amount: '))
rate = int(input('input num of year: '))
years = int(input('input rate of interest: '))
print(int(get_total_balance(amount,rate,years)))
