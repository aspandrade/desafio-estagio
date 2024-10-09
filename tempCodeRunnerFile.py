#Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;


    
while p == 's':

    palavra = str(input("Digite uma palavra qualquer: ")).strip().lower()

    print(palavra[::-1])
    
    p = str(input("Deseja digitar novamente? [s/n]: ")).lower().strip()
    
        