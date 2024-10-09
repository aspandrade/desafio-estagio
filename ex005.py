#Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;


p = 's'
    
try:
    while p == 's':
        
        palavra = str(input("Digite uma palavra qualquer: ")).strip().lower()

        print(palavra[::-1])
        
        p = str(input("Deseja digitar novamente? [s/n]: ")).lower().strip()
        
        p = p[0]
        
    if p == 'n':
        print("Ok, obrigado por usar nosso sistema!")
        print("="*20)
        print("progama encerrado.")
        print("="*20)
except:
    print("ERRO! Digite uma opção válida.")

    
    
        