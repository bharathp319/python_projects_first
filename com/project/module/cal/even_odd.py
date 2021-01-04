def even_odd():

    even = []
    odd = []
    num = int(input("enter a number: "))
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    print(even, odd)

even_odd()