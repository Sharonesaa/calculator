from Calculadora_1 import Calculator
class Menu():
    def option(self):
        operations = Calculator()
        while True:
            print('''\n
            1- addition.
            2-subtraction.
            3-multiplication.
            4-division.
            ''')
            opcion = int(input("Choose an option = "))
            if opcion == 1:
                operations.add()
            elif opcion == 2:
                operations.sub()
            elif opcion == 3:
                operations.mult()
            elif opcion == 4:
                operations.div() 

menu = Menu()
menu.option() 