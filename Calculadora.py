class CalculadoraBasica:
    #otra forma
    # def __init__(self, cifra1, cifra2):
    #     self.cifra1 = cifra1
    #     self.cifra2= cifra2
    #     self.resultado = 0

    def __init__(self):
         self.cifra1 = 0
         self.cifra2= 0
         self.resultado = 0

    def sumar(self):
        cifra1 = int(input('Digite la primera cifra: '))
        cifra2 = int(input('Digite la segunda cifra: '))
        resultado = cifra1 + cifra2
        print('El resultado de la suma de: ',cifra1, '+',cifra2, '=',int(resultado))

    def restar(self):
        cifra1 = int(input('Digite la primera cifra: '))
        cifra2 = int(input('Digite la segunda cifra: '))
        resultado = cifra1 - cifra2
        print('El resultado de la resta de: ', cifra1, '-', cifra2, '=', int(resultado))
        pass

    def multi(self):
        cifra1 = int(input('Digite la primera cifra: '))
        cifra2 = int(input('Digite la segunda cifra: '))
        resultado = cifra1 * cifra2
        print('El resultado de la multiplicacion de: ', cifra1, '*', cifra2, '=', int(resultado))
        pass

    def div(self):
        cifra1 = int(input('Digite la primera cifra: '))
        cifra2 = int(input('Digite la segunda cifra: '))
        resultado = cifra1 / cifra2
        print('El resultado de la division de: ', cifra1, '/', cifra2, '=', int(resultado))


r=1
while r==1:
    print ('1. Sumar')
    print ('2. Restar')
    print ('3. Multiplicar')
    print ('4. Dividir')
    operacion= input('Digite la opcion que desea: ')

    #otra forma
    # cifra1 = int(input('Digite la primera cifra: '))
    # cifra2 = int(input('Digite la segunda cifra: '))

    #calculadora= CalculadoraBasica(cifra1,cifra2)
    calculadora = CalculadoraBasica()

    if operacion == '1':
        calculadora.sumar()
    elif operacion == '2' :
        calculadora.restar()
    elif operacion == '3':
        calculadora.multi()
    elif operacion == '4':
        calculadora.div()
    else:
        print('La opcion no es valida')

    r = int (input('Digite 1. Seguir, 0.Salir '))





