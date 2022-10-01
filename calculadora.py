while True:
    print('')
    print('*'*30)
    print(f'{"*Calculadora Minimalista*":^30}')
    print('*'*30)
    print('')
    # Para melhor organização, formate a string utilizando print(f"")
   
    n1 = float(input('informe o primeiro valor: '))

    while True:
        op = input('Informe a operação (+, -, *, /): ')
        if op == '+' or op == '-' or op == '*' or op == '/':
            break
    #    else:
           # print(f"Erro de digitação. Tente novamente!")
    ''' hahah é interessante informar ao usuário! '''
    
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

