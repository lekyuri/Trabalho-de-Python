
sexo = input("digite seu genero: (h) para homem e (m)para mulher: ")

if sexo == "h":
   
    altura = float(input("DIGITE SUA ALTURA: "))
    
    peso = (altura * 72.7) -58
    
    print(f"Um HOMEM com a altura de: {altura}m, o peso ideal seria de: {peso:.2f}kg")

else:
    sexo == "m"
    
    altura = float(input("Informe sua Altura: "))
    
    peso = (altura * 62.1)- 44.7
    
    print(f"Uma MULHER com altura de: {altura}m, o peso ideal seria de: {peso:.2f} ")

