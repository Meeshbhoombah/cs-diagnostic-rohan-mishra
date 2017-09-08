def fibonacci(num=10):
    twoStepsPrior = 2
    stepPrior = 3

    for step in range(num + 1):
        if step > 0 and step > 3:
            number = twoStepsPrior + stepPrior
            print number
            twoStepsPrior = stepPrior
            stepPrior = number
        elif step > 0:
            print step


userInput = input("Enter a number for the fibonacci sequence: \n")
fibonacci(userInput)

# PROBLEM 10 #
# idk
