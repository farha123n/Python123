from logging import exception


try:
    a= int(input("enter a value"))
    a=1/a
except ValueError as e:
    print("enter a valid value")
except ZeroDivisionError as e:
    print("enter somthing without zero")
print("thank you")
