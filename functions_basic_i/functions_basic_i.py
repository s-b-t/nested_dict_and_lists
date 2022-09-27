#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# I predict that the output will be 5 as there has been
# nothing that has been assigned to the function except
# a return of 5.


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Similar to challenge 1, there's not a whole lot of info being
# given to the function. There's also an undefined variable
# which should actually produce an error instead of anything
# meaningful.


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# We've only successfully returned the value of 5, 'return 10' has nowhere to go because
# 'return' being used the first time should exit the code and give us 5 and ignore the 
# 'return 10'. Output should be 5.


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Even though it says print(10), our function is being returned with 5. Yet again,
# when the return call happens, the code exits with that result and should ignore 
# print(10) and instead give us an output of 5 because the function that's being
# printed has that return call attached to it. I am guessing that the computer ignores
# print(10) because it is stuck inside the function that is being returned a value of 5.
# If print(10) were outside of the function, then the computer likely wouldn't ignore it.


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# There are no arguments attached to x or number_of_great_lakes. In other words, empty.
# I predict we will get an output of 5 and None (or error??) right below it. The computer tells us
# that 5 should be printed even though it means nothing, but then is followed by an empty
# set of information that cannot return a meaningful value.


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# I predict the output will be 8. I was wrong on this one, but don't fully understand why.


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# In our return statement it seems as if b and c are being converted to strings but with
# no f-string attached to it in our print statement. Because the numbers are becoming strings,
# 'real math' will not take place but instead, pull the strings together producing an
# unexpected value of 25.


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# First, it will print 100. Then, print 10? 


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# First, it will print 7. Then, it should print 14? Return 3 does not seem like it
# will go anywhere either and therefore the code block will stop after return 14?
# I was partially wrong on this and am assuming 21 is printed as well, simply because
# what is happening is in the first line of the last print statement, we are returning a 7
# from the if statement, as well as returning a 14 from the else statement and adding them 
# together separately but in the same print statement.


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Our only return we can worry about seems like it will be the first one, b+c.
# Because b and c become defined in the print statement first the return will be successful, 
# and the code block should stop and ignore return 10. 
# My prediction is that the output will become 8.


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# First, it will print 500. Then, 300 because we redifined b? Then, 500? Then, 500 again?
# Okay, I was slightly off. My only logical explanation based on seeing the output is that
# because the third print(b) statement is all of a sudden outside of the function,
# that's when b fully becomes 300? Not quite sure I understand how the last print(b)
# statement = 500 after redefining the variable to 300 inside the function and then
# outside the function became 300. Then on the same code block changed back to 500?
# This one through me in for a loop!


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# First, 500 will be printed. Then, based on previous challenge next print has to be 500 again.
# After that, 300 is being passed back to b with the return call.
# Then, because of this, the rest of our print statements should 
# all become 300 as the output? 
# Okay... these are tricky! This one through me in for another loop.


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Still not quite understanding how when declaring b as 300, we are still printing 500
# until b steps outside of the function? My educated guess is because even though it states
# b is 300, upon RETURNing b finally, that's when it can become 300. Then, because b has been
# returned as 300, the rest of the code block will execute b accordingly and when b is set 
# equal to the function itself. 


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# The easy prediction is 1, 2, 3 -- which I know is wrong. Having a tough time
# wrapping my head around the true output of 1, 3, 2. 


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# 1, 10, 5, 10 -- Got a few of them correct, just still having a tough time with the
# order that these return statements are making the output display in (like where the 3
# pops in second, instead of the 10 that I predicted.)