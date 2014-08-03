
def sum_squares(n):
    total = 0
    for i in range(n+1):
        total += i * i
    return total

print sum_squares(10)

def square_sum(n):
    total = 0
    for i in range(n+1):
        total += i
    return total * total

print square_sum(10)

print square_sum(10) - sum_squares(10) 

print square_sum(100) - sum_squares(100) 


