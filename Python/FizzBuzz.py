#The FizzBuzz problem is a common coding challenge where you print numbers from 1 to n, 
# but for multiples of 3, print "Fizz" instead of the number, for multiples of 5, print "Buzz", 
# and for multiples of both 3 and 5, print "FizzBuzz".

for i in range(0,16):
    if (i%3==0 and i%5==0):
        print(i, "FizzBuzz")
    elif(i%5==0):
        print(i, "Buzz")
    elif(i%3==0):
        print(i, "Fizz")
    