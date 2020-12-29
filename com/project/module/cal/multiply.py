class mul:
    def mul1(self):
        num = int(input("enter a number: "))
        i = 1
        while i < 11:
            n = i * num
            print(f"{num} * {i} = ", n)
            i += 1



t = mul()
t.mul1()