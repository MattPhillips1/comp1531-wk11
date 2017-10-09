# code for the file investment.py
# python program to calculate simple interest


def calculate_simple_interest(p, n, r):
    i = p*n*r/100
    return i


# python program that calculates annual compound interest
def calculate_compound_interest(p, n, r):
    i = p * (1.0 + r/100) ** n
    return i
