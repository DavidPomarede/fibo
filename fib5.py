from functools import lru_cache
@lru_cache(maxsize = 220)
def fibonacci(n):
    # check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise TypeError("n must be a positive int")

    if n == 1:
        return 1
    elif n ==2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# if you do it like this, numbers converge on the golden ratio
for n in range(1, 54):
    print(fibonacci(n+1) / fibonacci(n))

# now it's just displaying the ascii char

numbers = [17, 38, 79] 
  
for number in numbers: 
      
    # Convert ASCII-based number to character. 
    letter = chr(number) 
    print("Character of ASCII value", number, "is ", letter)



# bored now

a, b = 10, 20
  
if a != b: 
    if a > b: 
        print("a is greater than b") 
    else: 
        print("b is greater than a") 
else: 
    print("Both a and b are equal") 


# functions


# Here x is a new reference to same list lst 
def myFun(x): 
   x[0] = 20
  
# Driver Code (Note that lst is modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun(lst); 
print(lst)  



