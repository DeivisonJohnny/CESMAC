import os 

estoqueP = []
categorias = []
result = []
while True:
    nameP = input("Qual o nome do produto? ")
    if (nameP in estoqueP):
        print("O produto ja esta cadastrado\n")
    else:
        estoqueP.append(nameP)
        result.append('Nome do produto: ' + nameP)
        
        if (len(categorias) > 0):
            for i in range(len(categorias)):
                print("\n",categorias[i])
            cate = input("""
                Qual categoria você gostaria de cadastrar este produto?
                """).lower()
            if (cate in categorias):
                print('Categoria cadastrada')
                result.append('Categoria cadastrada: '+ cate)
            else:
                while True:
                    for i in range(len(categorias)):
                        print(categorias[i])
                    cateError = input('Escolha novamente a categoria: ').lower()
                    if(cateError in categorias):
                        break
                    else:
                        print('Foi cadastrado uma nova categoria', cateError)
                        result.append('Categoria cadastrada: '+ cateError)

                        break
        else:
            print("Ainda não existe nenhuma categoria no sistema")
            newCate = input("Digite um nome de uma nova categoria? ")
            categorias.append(newCate.lower())
            result.append(f"Categoria cadastrada: {newCate}")
            
        # Passo 4° Estrutura de repetição    

        while True:
            try:
                qtd = int(input('Digite qual o número do estoque inicial em unidade: ')) 
                if(qtd < 0):
                    print("Digite um valor positivo, por favor!!!")
                else:
                    if(qtd > 0):
                        print(f"O valor digitado foi {qtd}")
                        confQtd = input(f"Você confirma o valor inicial de {qtd} no estoque [y/x]").lower()
                        # Passo 3° estrutura de decisão/condicionais
                        if(confQtd == 'y'):
                            break
                        # Passo 3° estrutura de decisão/condicionais
                        if(confQtd != 'y'):
                            sm = input("Você gostaria de adicionar, ou retirar? [1 - adicionar, 2 - retirar]")
                            # Passo 3° estrutura de decisão/condicionais
                            if(sm == '1' or sm =='adicionar'):
                                print(f"Este é o seu estoque digitado: {qtd}")
                                try:
                                    smd = int(input(f"Quanto voce gostaria de tirar {qtd} + "))

                                    # Passo 2° Operações aritméticas

                                    res = qtd + smd
                                    result.append("Estoque Total", f"{res}")
                                    print(f" O estoque inicial ficou {res}")
                                    break
                                except ValueError:
                                    print("Digite numeros inteiros")
                            else:
                                print("Digite um valor válido")
                            if(sm == '2' or sm =='retirar'): #continuar a partir daqui
                                print(f"Este é o seu estoque digitado: {qtd}")
                                try:
                                    sb = int(input(f"Quanto voce gostaria de tirar {qtd} - "))

                                    # Passo 2° Operações aritméticas

                                    res = qtd - sb
                                    result.append("Estoque Total " + f"{res}")
                                    print(f"O estoque inicial ficou {res}")
                                    break
                                except ValueError:
                                    print("Digite numeros inteiros")
                            else:
                                print("Digite um valor válido")
            except ValueError:
                print("Valor invalido, tente novamente")


    for i in range(len(result)):
        print(f"""
                {result[i]}
                """)
    cont = input("Gostaria de continuar cadastrando? [y/x]").lower()
    if(cont != 'y'):
        break
    os.system('cls || clean')
