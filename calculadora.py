while True:
    print('')
    print('*********************************')
    print('*Calculadora Minimalista*')
    print('*********************************')
    print('')

    n1 = float(input('informe o primeiro valor: '))

    while True:
        op = input('Informe a operação (+, -, *, /): ')
        if op == '+' or op == '-' or op == '*' or op == '/':
            break
    n2 = float(input('Informe o segundo número:'))
    if op == '+':
        print('Resultado =' , n1 + n2)

        cont = input('Deseja Continuar? (s/n):')
        if cont!= 's':
            break
    elif op == '-':
        print('Resultado = ', n1 - n2)

        cont = input('Deseja Continuar?(s/n): ')
        if cont != 's':
            break
    elif op == '*':
        print('Resultado =', n1 * n2)
        cont = input('Deseja Continuar? (s/n):')
        if cont != 's':
            break
    elif op == '/':
        print('Resultado=', n1 / n2)
        cont = input('Deseja continuar? (s/n):')
        if cont != 's':
            break

