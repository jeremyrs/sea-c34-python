num = int(raw_input("what number in the Fibonacci Sequence do you want to see?"))
n = num
def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci_sequence(n-1) + fibonacci_sequence(n-2))
print fibonacci_sequence(num)


def lucas_number(x)
    if x == 0:
        return 2
    elif x == 1:
        return 1
    else:
        return (lucas_number(x-1) + lucas_number(x-2))
    print lucas_number()

def sum_series(a)
    if a == fibonacci:
        return fibonacci_sequence()
    elif a == lucas:
        return lucas_number()






