from time import sleep

print('SEJA BEM VINDO AO BANK NEW HORIZON !!')
nome = str(input('Por favor informe o seu nome: '))

resp = int(input('Sr {} o senhor(a) possui cadastro no banco new horizon ? [0]não [1]sim: '.format(nome)))

if resp == 0:
    x = int(input('sr(a) {} gostaria de realizar o cadastro [0]não [1]sim: '.format(nome)))
    while x == 0:
        print('Sr(a) {} agradeçemos o contato, mas não poderemos continuar !!'.format(nome))
        break
    while x == 1:
        str(input('Ok sr(a) {} por favor informe o seu nome completo: '.format(nome)))
        str(input('Informe o seu bairro: '))
        str(input('Informe a cidade onde reside: '))
        str(input('Informe o seu endereço residencial: '))
        int(input('Informe o ddd: '))
        float(input('Informe o numero de telefone: '))
        str(input('Informe o seu sexo: '))
        str(input('Informe a sua nacionalidade: '))
        str(input('Informe a cidade do seu nascimento: '))
        str(input('Informe o estado de nascimento: '))

        doc = int(input('sr(a) {} escolha um documento para informar '
                        '[0]RG [1] CPF \ninforme a sua escolha:'.format(nome)))
        while doc == 0:
            cpf = float(input('Sr(a) {} informe aqui o numero do seu RG (Somente numeros): '.format(nome)))
            break
        while doc == 1:
            rg = float(input('Sr(a) {} informe aqui o numero do seu CPF (somente numeros):  '.format(nome)))
            break
        while doc >= 2:
            print('Opção invalida !')
            break
        if doc <= 1:

            t = int(input('sr(a) {} informe o tipo de conta que gostaria de abrir,'
                          '[1] conta corrente [2] conta poupança [3] conta salário: '))
            if t == 1:
                print('Sr {} em um instante estaremos abrindo a sua conta corrente !'.format(nome))
                print('Sr {} a sua Agencia é 1440 e sua conta corrente é a 12259-8 .'.format(nome))
            if t == 2:
                print('Sr {} em um instante estaremos abrindo a sua conta poupança !'.format(nome))
                print('Sr {} a sua Agencia é 1440 e sua conta poupança é a 12259-8 .'.format(nome))
            if t == 3:
                print('Sr {} em um instante estaremos abrindo a sua conta sálario !'.format(nome))
                print('Sr {} a sua Agencia é 1440 e sua conta Sálario é a 12259-8 .'.format(nome))
            print('Agradeçemos volte sempre !')
            break

if resp == 1:
    y = int(input('Ok sr(a) {} qual seria o seu cadastro [1] cliente ou [2] funcionario: '.format(nome)))
    if y == 2:
        us = str(input('Informe o seu usuario: '))
        sh = int(input('Sr(a) {} informe a sua senha: '.format(us)))
        if sh != 123456:
            print('Sr {} a sua senha esta errada !\nACESSO RECUSADO!!'.format(nome))
        else:
            print('Sr {} seja bem vindo !'.format(nome))
            sv = int(input('Sr {} informe o tipo de serviço que será executado.\n[1]correção no sistema'
                           '\n[2]correção no hardware\n[3]Manutenção na rede'
                           '\npor favor informe a opção escolhida:'.format(nome)))
            if sv == 1:
                print('Acesso liberado para manutenção no sistema !!'.format(nome))
            if sv == 2:
                print('Acesso liberado para correção do hardware !!'.format(nome))
            if sv == 3:
                print('Acesso liberado a manutenção de Rede !!')

    elif y == 1:
        card = int(input('Sr(a) {} gostaria de iniciar com o cartão ou sem o cartão '
                         '[1]Com cartão [2]Sem cartão:'.format(nome)))
        if card == 1:
            print('Sr(a) {}, ok Vamos continuar o acesso com o cartão !'.format(nome))
        elif card == 2:
            print('Sr(a) {}, ok Vamos continuar sem o Cartão !!'.format(nome))
        else:
            print('Sr(a) {},Esta opção escolhida é invalida !!'.format(nome))

        fun = int(input('Seja bem vindo(a) sr(a) {} o que gostaria de realizar?\n[1]Saque [2]Deposito '
                        '[3]Consultar Câmbio [4]Emprestimo [5]Tranferencia [6]Saldo '
                        '[7]Extrato\n[8]Consultar conta\n[9]Solitações\Informativos \n[10]Pagamento de contas'
                        '\nsr(a) {} Informe a sua escolha: '.format(nome, nome)))
        si = int(input('Informe a sua senha de 6 digitos:'))
        if si == 123456:
            if fun == 1:
                vc = float(input('Informe o valor em reais que voce tem na sua conta hoje R$ '))
                vs = float(input('Informe o valor que gostaria de sacar da sua conta R$ '))
                if vs <= 1000.00:
                    sub = vc - vs
                    print('sr(a) {} valor de saque foi R$ {} e atualmente consta '
                          'R$ {} na sua conta bancaria.'.format(nome, vs, sub))
                    print('Obrigado, volte sempre !!')
                if vs >= 1000.01:
                    print('Saldo recussado.\nO valor escolido foi de R$ {} maior que R${} '.format(vs, 1000.00))
                    print('Obrigado, volte sempre !!')
            elif fun == 6:
                input('Informe o seu nome completo:')
                print('Sr(a) {} o saldo na sua conta é de R${}'.format(nome, 1000.00))
                i = int(input('Sr(a) {} Gostaria de imprimir [1]sim ou [2]não: '.format(nome)))
                if i == 1:
                    print('o saldo de sua conta esta sendo impresso.......')
                elif i == 2:
                    print('Obrigado, Volte sempre!!!')
            elif fun == 7:
                print('Sr(a) {} o extrato da sua conte é de R${} e não '
                      'houve movimentação até a data atual.'.format(nome, 1000.00))
            elif fun == 2:
                d = float(input('sr(a) {} Informe o valor que voce deseja adicionar a sua conta R$ '.format(nome)))
                valoc = float(input('Sr(a) {} Informe o valor em reais'
                                    ' que voce já tinha na sua conta hoje R$ '.format(nome)))
                soma = d + valoc
                print('Sr(a) {} o valor na sua conta atual é de R$ {}'.format(nome, soma))
                print('Obrigado, volte sempre !!')
            elif fun == 3:
                r = float(input('sr {} iremos consultar o cambio do dolar!'
                                '\ninforme o valor em reais que o senhor tem hoje R$ '.format(nome)))
                cal = (r / 5.71)
                print('Sr {} o valor em dolar será de $ {:.2f}\nMuito obrigado!!'.format(nome, cal))
                b = int(input('Sr{} gostaria de imprimir [1] SIM [2]NÃO:'.format(nome)))
                if b == 1:
                    print('O Seu recibo esta sendo impresso! ')
                if b == 2:
                    print('Agradeçemos, volte sempre !!')
                while b != 1:
                    print('Opção invalida !!')
                    break
                while b == 1:
                    print('Opção invalida !!')
                    break
            elif fun == 4:
                valorr = float(input('Sr {} favor informar o valor do emprestimo requerido R$ '.format(nome)))
                div = float(input('Sr{} informe em quantas vezes gostaria de dividir o valor:'.format(nome)))
                cal = (div * 0.102) + div
                print('Sr{} pagara R$ {} por {} meses sendo que há 1,2% de juros por mes ! '.format(nome, cal, div))
                print('Obrigado, volte sempre !!')
            elif fun == 8:
                print('Ok sr(a) {} a sua Agencia é a 1440\na sua conta é 12259-8 \nE o seu tipo de '
                      'conta é corrente !'.format(nome))
            elif fun == 9:
                str(input('Sr {} faça a sua solicitação em texto: '.format(nome)))
            elif fun == 5:
                ty = int(input('Informe o tipo de tranferencia [1]ted [2]doc [3]transferencia [4]pix : '))
                if ty == 1 or 2 or 3:
                    str(input('Informe o banco destinadario:'))
                    float(input('Informe a conta bancaria sem digidos:'))
                    int(input('Informe a agencia sem digito:'))
                    float(input('Informe o valor de transferencia R$ '))
                    str(input('Informe o nome do destinatario:'))
                    print('Nas operações de TED ou DOC Será cobrada uma taxa de R$ 10 por operações !')
                    print('OK,tranferencia concluida com sucesso !!\nVolte sempre!!')
                elif ty == 4:
                    str(input('Transferencia PIX,Informe o nome do destinatario:'))
                    n = float(input('Informe o tipo de documento [5]Rg ou [6]Cpf: '))
                    while n == 5:
                        input('Informe o numero do ser RG:')
                    while n == 6:
                        input('Informe o numero do seu CPF:')
                        break
                    else:
                        print('Opção invalida !!')
            elif fun == 10:
                print('Iremos iniciar o pagamento de contas !!')
                o = int(input('Informe o tipo de pagamento \n[1] BOLETO \n[2]CODIGO DE BARRAS:'))
                if o == 1:
                    input('Digite o BOLETO BANCARIO:\n')
                    input('Informe o valor R$ ')
                    sleep(2)
                    print('PAGAMENTO REALIZADO COM SUCESSO!!')
                if o == 2:
                    input('Digite o CODIGO DE BARRAS bancario:\n')
                    input('Informe o valor R$ ')
                    sleep(2)
                    print('PAGAMENTO REALIZADO COM SUCESSO!!')
        else:
            print('Opção invalida!!\nTente novamente!!')
    else:
        print('Opção invalida!!\nTente novamente!!')
while resp >= 2:
    print('Opção invalida!!\nTente novamente!!')
    break
