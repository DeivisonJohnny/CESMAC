import os 

estoqueP = []
categorias = []
result = []
while True:
    nameP = input("Qual o nome do produto? ")
    if (nameP in estoqueP):
        print("O produto ja esta cadastrado\n")
    else:
        print("Nome valido \n") 
        estoqueP.append(nameP)
        result.append('Nome do produto: ' + nameP)
        
        if (len(categorias) > 0):
            for i in range(len(categorias)):
                print(categorias[i])
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
            
        while True:
            try:
                qtd = int(input('Digite qual o número do estoque inicial em unidade: ')) 
                if(qtd < 0):
                    print("Digite um valor positivo, por favor!!!")
                else:
                    result.append(f"Seu estoque inicial é de: {qtd}")
                    break
            except ValueError:
                print("Valor invalido, tente novamente")


    for i in range(len(result)):
        print(f"""
                {result[i]}
                """)
    print(categorias, estoqueP)
    cont = input("Gostaria de continuar cadastrando? [y/x]")
    if(cont != 'y'):
        break
    os.system('cls || clean')
