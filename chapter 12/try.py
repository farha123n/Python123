a=input("Enter a number")
while(True):
    a=input("Enter a number")
    print("press q to quite")
    if a == 'q':
        break

    try:
        a=int(a)
        if a>6:
            print("number is greater than 6")


    except Exception as e:
        print(f"you entered aa error that is {e}")

print("thanks for playing")