# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def factorial_calc(x):
    fac = 1
    for i in range(x):
        i += 1
        fac = fac * i # User code goes here
    return fac


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    print(factorial_calc(5))

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #v = input("Value to increment: ")
    #print(inc(int(v)))
