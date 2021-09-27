executando = True
while executando:
    try:
        altura = float(input('Qual a sua altura (0.00)? '))
        peso = float(input('Qual o seu peso (00.00)? '))
        if peso < altura:
            print('Peso deve ser maior do que altura\n')
        elif altura and peso < 0:
            print('Peso e altura devem ser maiores do que zero (0)!\n')
        elif altura > 2.55:
            print('Altura deve ser menor que 2.55')
        else:
            imc = peso / (altura**2)
            print(f'\nIMC: {imc:.2f}')
            if imc < 18.5:
                print('Magreza, abaixo do peso.')
            elif 18.5 <= imc < 25:
                print('Normal, dentro do peso.')
            elif 25 <= imc < 30:
                print('Sobrepeso, acima do peso.')
            elif 30 <= imc < 35:
                print('Obesidade, muito acima do peso.')
            elif 35 <= imc < 40:
                print('Obesidade mórbida, extremamente acima do peso.')
            else:
                print('Obesidade grave, fatalmente acima do peso.')
            executando = False
    except ValueError:
        print(f'Peso e altura devem ser númericos!')

