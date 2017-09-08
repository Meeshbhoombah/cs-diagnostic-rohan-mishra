# input start number and finish number
#
# for every # between the start number and finish number:
#     if a # is / by 3
#         print fizz
#     if a # is / by 5
#         print buzz
#     if a # is / by 3 or 5
#         print fizzbuzz
#     otherwise
#         print the number


def fizzbuzz(x, y):
    for i in range(x, y + 1):
        if ((i % 3 == 0) and (i % 5 == 0)) and i != 0:
            print "fizzbuzz"
        elif i % 3 == 0 and i != 0:
            print "fizz"
        elif i % 5 == 0 and i != 0:
            print "buzz"
        else:
            print i


fizzbuzz(0, 15)
