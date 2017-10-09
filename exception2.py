import sys
try:
    numerator = int(input("Enter the numerator..."))
    denominator = int(input("Enter the denominator..."))
    result = numerator/denominator
    print(result)
except ValueError:
    print("I said number... :(")
    sys.exit()
except ZeroDivisionError:
    print("You can't divide by 0 though...?")
    sys.exit()
print(
    "Your num was {}, denom was {} and the result is ......{}"
    .format(numerator, denominator, result))
