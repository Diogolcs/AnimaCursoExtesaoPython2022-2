#AULA_1
# Meu primeiro projeto Python
#
#print("Hello word!")

# Quando quiser guardar um String (não precisa declar variavel)

#nome = "Diogo Lacerda"
#idade = 19

# /n quebra de linha 
# +str é coversão de variavel
#print("Seu nome é:" +nome,",", "e você tem " +str(idade),"anos\n")


#print(f"Seu nome é:" +nome,",", "é você tem {}".format(idade),"anos\n")

#forma simples
#print("Meu nome é {} e tenho {} anos".format(nome,idade))


# comando input(): quero permitir que 
# o usuário digite algo...
#nome = input("Digite seu nome: \n")

#genero = input("Qual o seu genero: \n")

#idade = int(input("Digite sua idade: "))

#print(f"Seu nome é: {nome}, e sua idade é {idade}\n")
#-----------------------------------------------------------------------------------------------

#  AULA_2

#print("o dobro da sua idade é {}".format(idade*2))
#Estrutura condicional
#== é comparação
#if  idade < 18: print("Você não pode beber") 
  
#else: print("Você pode beber, CUIDADO!! \n")  ,print("Você deve prestar serviço militar")
#_______________________________________________________________________________________________
 

#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."
     
#nome = input("Infomr seu nome: ")
#nota = float(input("Digite sua nota: "))


#if (nota==10):
#  print(f"{nome}, você é o bichao mesmo...")
#elif (nota<10 and nota >=6):
#  print (f"{nome} você pode melhorar")
#else: 
#   print("Reprovado!!")


#Exemplo de laço
# print("Maneira rústica")
#  print("1")
# print("2")
# print("3")
# print("4")
# print("5")
# print("6")
# print("7")
# print("8")
# print("9")
# print("10\n")


# numero = 1
# print(numero)
# numero = numero + 1
# print (numero)

print("Aula 3 - 09/11/22\n")

#Exibir de 1 a a 10
contador = 1

#while(contador <=10):
#  print(contador)
#  contador = contador+1

#Laço for

fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#Lista

frutas = ["morango", "laranja", "pêra"]

#quero exibir apenas a 3 fruta(0,1,2)

print(frutas)

print(frutas[2])

#exibir quantas frutas tem na lista
print(len(frutas))

#Quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas)) #lengh = tamanho
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

i=0
while(i<4):
  print(frutas[i])
  i = i + 1

 
print("Exemplo das frutas com FOR")
for fruta in frutas:
  print(frutas)
