# Meu primeiro projeto Python
#
print("Hello word!")

# Quando quiser guardar um String (não precisa declar variavel)

nome = "Diogo Lacerda"
idade = 19

# /n quebra de linha 
# +str é coversão de variavel
print("Seu nome é:" +nome,",", "e você tem " +str(idade),"anos")

print(f"Seu nome é:" +nome,",", "e você tem {idade} anos")

print(f"Seu nome é:" +nome,",", "é você tem {}".format(idade),"anos")

#forma simples
print("Meu nome é {} e tenho {} anos".format(nome,idade))
