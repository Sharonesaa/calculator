
class Calculator:
    def add(self):
        counter = int(input("How many numbers will you enter? = "))
        total = 0
        for n in range(counter):
            number = int(input("Enter a number = "))
            total += number
        print(total)

    def sub(self):
        counter = int(input("How many numbers will you enter? = "))
        total = 0
        for n in range(counter):
            number = int(input("Enter a number = "))
            if total == 0:
                total = number
            else:
                total -= number
        print(total)
   
    def mult(self):
        counter = int(input("How many numbers will you enter? = "))
        total = 1
        for n in range(counter):
            number = int(input("Enter a number = "))
            total *= number
        print(total)

    def div(self):
        counter = int(input("How many numbers will you enter? = "))
        total = 0
        for n in range(counter):
            number = int(input("Enter a number = "))
            if total == 0:
                total = number
            else:
                total /= number
        print(total)
    
# calculadora = Calculator()
# calculadora.sum()
# calculadora.sub()
# calculadora.mult()
# calculadora.div() 
