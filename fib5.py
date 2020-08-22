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



numbers = [17, 38, 79] 
  
for number in numbers: 
      
    # Convert ASCII-based number to character. 
    letter = chr(number) 
    print("Character of ASCII value", number, "is ", letter)







