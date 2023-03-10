from docx import Document as dc
import os

so = dc("sistema.docx")
at = dc("arquiteturaPC.docx")

while(True):
    print("""
    Opções:
        1--- Me fale sobre o assunto de Sistemas Operacionais(SO)
        2--- Me fale sobre o assunto de Arquitetura de Computadores
        3--- Sair

    """)

    opcao = input('Digite uma opção: ')
    os.system('cls||clear')
    if(opcao == '1'): 
        for paragrafo in so.paragraphs:
            print(f"""
Veja abaixo um pouco sobre o assunto de SISTEMAS OPERACIONAIS:

    {paragrafo.text}
            """)
            
    elif(opcao == '2'):
        for paragrafo in at.paragraphs:
            print(f"""
Veja abaixo um pouco sobre o assunto de ARQUITETURA DE COMPUTADORES:

    {paragrafo.text}
            """)
            
    elif (opcao == '3' or opcao == 'sair' or opcao == 'exit' or opcao == 'fechar'):
        print('Fim!!!')
        break
    else: 
        print('Não é uma opção válida')