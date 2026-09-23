from time import sleep

while True:
    escolha = input('''\n\nescolha como quer manipular a string:
    1- strip (tirar os espaços do texto)
    2- lower (todas as letras minúsculas)
    3- upper (todas as letras maiúsculas)
    4- title (cada primeira letra das palavras maiúscula)
    5- replace (mudar alguma parte do texto)
    6- split (separar cada palavra numa lista)
    7- join (adicionar itens numa string)
    8- count (contar quantos itens 'x' aparece no texto)
    9- startswith (verificar se a string começa com um valor específico)
    10- endswith (verificar se a string termina com um valor específico)
    11- find (informa a posição de um caractere)
    12- isalpha (verifica se a string contém apenas letras)
    13- isdigit (verifica se a digitação contém apenas dígitos)
    14- isalnum (verifica se a digitação contém apenas letras e números)
    15- isspace (verifica se a digitação há espaços em branco)
    16- isupper (verifica se a digitação contém apenas letras maiúsculas)
    17- islower (verifica se a digitação contém apenas letras minúsculas)
    18- zfill (adiciona caracteres (0) no início da digitação até chegar no comprimento desejado)
    19- sair
    \n''')
    sleep(0.3)

#questão 1
    if escolha == '1':
    #letra a
        nome_cliente = input('\ndigite o nome de um cliente: ')
        print(nome_cliente.strip())
        sleep(0.7)

    #letra b
        termo = input('\ndigite um termo para busca: ')
        print(termo.strip())
        sleep(0.7)


#questão 2
    elif escolha == '2':
    #letra a
        comando = input('\ninsira um comando: ')
        print(comando.lower())
        sleep(0.7)
        if comando.lower() == 'sair':
            verificar = input('\ndeseja mesmo sair? (S/N)\n').lower()
            if verificar == 's':
                print('\nencerrando o programa...')
                sleep(0.5)
                break

            else:
                sleep(0.7)
                continue

    #letra b
        email = input('\ninsira um endereço de email: ')
        print(f'seu email com todas letras minúsculas fica assim: {email.lower()}')
        sleep(0.7)


#questão 3
    elif escolha == '3':
    #letra a
        codigo = input('\ndigite o código de um produto: ')
        print(codigo.upper())
        sleep(0.7)

    #letra b
        sigla = input('\ndigite a sigla de um estado: ')
        print(sigla.upper())
        sleep(0.7)


#questão 4
    elif escolha == '4':
    #letra a
        nome_completo = input('\ndigite o nome completo: ')
        print(nome_completo.title())
        sleep(0.7)

    #letra b
        nome_evento = input('\ndigite o nome de um evento: ')
        print(nome_evento.title())
        sleep(0.7)


#questão 5
    elif escolha == '5':
    #letra a
        telefone = input('\ndigite um número de telefone: ')
        print(telefone.replace('-', ''))
        sleep(0.7)

    #letra b
        valor = input('\ndigite um valor: ')
        print(valor.replace(',', '.'))
        sleep(0.7)


#questão 6
    elif escolha == '6':
    #letra a
        dados = input('\ninforme seu nome, idade e cidade: ').replace(',', '').replace('.', '')
        print(dados.split())
        sleep(0.7)

    #letra b
        palavras = input('\ndigite palavras-chave: ').replace(',', '')
        print(palavras.split())
        sleep(0.7)


#questão 7
    elif escolha == '7':
    #letra a 
        integrantes = ['fel', 'clacla', 'johnny', 'raposo']
        print(', '.join(integrantes))
        sleep(0.7)

    #letra b
        opcoes_percorridas = ['entrar', 'cadastrar', 'digitar']
        print('>'.join(opcoes_percorridas))
        sleep(0.7)


#questão 8
    elif escolha == '8':
    #letra a
        frase = input('\ndigite um texto: ')
        print(f'a letra "a" aparece {frase.count('a')} vezes na frase')
        sleep(0.7)

    #letra b
        anotacao = input('\ninsira uma anotação: ')
        print(f'a palavra "erro" ocorre {anotacao.count('erro')} vezes na frase')
        sleep(0.7)


#questão 9
    elif escolha == '9':
    #letra a
        comando2 = input('\ndigite um comando: ')
        if comando2.startswith('/') == True:
            print(f'o comando {comando2} é um comando especial')
            sleep(0.7)
        else:
            print(f'o comando {comando2} é um comando normal')
            sleep(0.7)

    #letra b
        produto = input('\ndigite o código de um produto: ')
        if produto.startswith('PROD') == True:
            print(f'o produto de código {produto} começa com prefixo "PROD-"')
            sleep(0.7)
        else:
            print(f'o produto de código {produto} não começa com prefixo "PROD-"')
            sleep(0.7)


#questão 10
    elif escolha == '10':
    #letra a
        arquivo = input('\ndigite o nome de um arquivo: ')
        if arquivo.endswith('.csv') == True:
            print('o nome do arquivo termina com ".csv"')
            sleep(0.7)
        else:
            print('o nome do arquivo não termina com ".csv"')
            sleep(0.7)

    #letra b
        email_instituicional = input('\ndigite o email institucional: ')
        if email_instituicional.endswith('@ufrpe.br') == True:
            print('o email termina com "@ufrpe.br"')
            sleep(0.7)
        else:
            print('o email não termina com "@ufrpe.br"')
            sleep(0.7)

        
#questão 11
    elif escolha == '11':
    #letra a
        email2 = input('\ndigite um email: ')
        print(f'o "@" aparece na posição {email2.find('@')}')
        sleep(0.7)

    #letra b
        comando3 = input('\ndigite um comando: ')
        print(f'o "." aparece na posição {comando3.find('.')}')
        sleep(0.7)


#questão 12
    elif escolha == '12':
    #letra a
        primeiro_nome = input('\ndigite um primeiro nome: ')
        if primeiro_nome.isalpha() == True:
            print(f'o nome {primeiro_nome} contém apenas letras')
            sleep(0.7)
        else:
            print(f'o nome {primeiro_nome} não contém apenas letras')
            sleep(0.7)

    #letra b
        categoria = input('\ndigite uma categoria: ')
        if categoria.isalpha() == True:
            print(f'a categoria {categoria} contém apenas letras')
            sleep(0.7)
        else:
            print(f'a categoria {categoria} não contém apenas letras')
            sleep(0.7)

#questão 13
    elif escolha == '13':
    #letra a
        opcao_menu = input('\ndigite uma opção escolhida em um menu: ')
        if opcao_menu.isdigit() == True:
            print(f'a opção {int(opcao_menu)} contém apenas dígitos')
            sleep(0.7)
        else:
            print('a opção escolhida não contém apenas dígitos')
            sleep(0.7)

    #letra b
        idade = input('\ndigite uma idade: ')
        if idade.isdigit() == True:
            print('a idade digitada contém apenas números')
            sleep(0.7)
        else:
            print('a idade digitada não contém apenas números')
            sleep(0.7)

#questão 14
    elif escolha == '14':
    #letra a
        codigo_acesso = input('\ndigite um código de acesso: ')
        if codigo_acesso.isalnum() == True:
            print('o código de acesso digitado contém apenas letras e números, sem símbolos ou espaços')
            sleep(0.7)
        else:
            print('o código de acesso digitado não contém apenas letras e números')
            sleep(0.7)

    #letra b
        identificador = input('\ndigite um identificador de um produto: ')
        if identificador.isalnum() == True:
            print('OK, o identificador é alfanumérico')
            sleep(0.7)
        else:
            print('identificador não aceito, não é alfanumérico')
            sleep(0.7)


#questão 15
    elif escolha == '15':
    #letra a
        observacao = input('\ndigite um campo de observação: ')
        if observacao.isspace() == True:
            print('a digitação só contém espaços em branco')
            sleep(0.7)
        else:
            print('a digitação não contém apenas espaços em branco')
            sleep(0.7)

    #letra b
        resposta = input('\ndigite uma resposta: ')
        if resposta.isspace() == True:
            print('a resposta está vazia')
            sleep(0.7)
        else:
            print('OK, a resposta não está vazia')
            sleep(0.7)


#questão 16
    elif escolha == '16':
    #letra a
        sigla2 = input('\ndigite uma sigla: ')
        if sigla2.isupper() == True:
            print('todas as letras digitadas são maiúsculas!')
            sleep(0.7)
        else:
            print('nem todas as letras digitadas são maiúsculas')
            sleep(0.7)

    #letra b
        codigo_categoria = input('\ndigite o código de uma categoria: ')
        if codigo_categoria.isupper() == True:
            print('o formato digitado está correto')
            sleep(0.7)
        else:
            print('o formato digitado está incorreto')
            sleep(0.7)


#questão 17
    elif escolha == '17':
    #letra a
        comando4 = input('\ndigite um comando: ')
        if comando4.islower() == True:
            print('o formato está correto para ser executado')
            sleep(0.7)
        else:
            print('o formato está incorreto')
            sleep(0.7)

    #letra b
        nome_usuario = input('\ndigite o nome de usuário: ')
        if nome_usuario.islower() == True:
            print('o nome de usuário está todo minúsculo')
            sleep(0.7)
        else:
            print('o usuário contém letras maiúsculas')
            sleep(0.7)


#questão 18
    elif escolha == '18':
    #letra a
        senha = input('\ndigite uma senha de atendimento: ')
        print(f'o número da sua senha no formato ideal é: {senha.zfill(5)}')
        sleep(0.7)

    #letra b
        nota = input('\ninsira um número de uma nota ou pedido: ')
        print(f'o número do pedido no formato ideal é: {nota.zfill(8)}')
        sleep(0.7)

#saída 
    elif escolha == '19':
        sair = input('deseja mesmo sair?(S/N) ').lower()
        if sair == 's':
            print('\nencerrando o programa...')
            sleep(0.7)
            break
        else:
            sleep(0.5)
            continue
        

    else:
        print('\nopção inválida, tente novamente')
        sleep(0.5)