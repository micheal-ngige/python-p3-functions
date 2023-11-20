#!/usr/bin/env python3

def greet_programmer():
    print( "Hello, programmer!" )

def greet(name):
    print("Hello, " + name + "!")

greet("Guido")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    
    
greet_with_default()

def add(num1, num2):
    result = num1 + num2
    print(result)
    return result


sum_result = add(45, 55)


print(f"The sum is: {sum_result}")
  

def halve(number):
    result = number / 2
    print(result)
    return result


halved_value = halve(100)


print(f"The halved value is: {halved_value}")


