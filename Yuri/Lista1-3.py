
salario_hora = float(input("Informe quanto voce ganhar por hora: "))
horas_mes = int(input("Entre com a quantidade de horas trabalhada no mes: "))

salario_bruto = salario_hora * horas_mes
print(f"+ salario bruto: {salario_bruto:.2f}R$")

ir = (11/100)* salario_bruto
print(f"- IR (11%): {ir:.2f}R$") 

inss = (8/100)* salario_bruto
print(f"- INSS(8%): {inss:.2f}R$")

sindicato = (5/100)* salario_bruto
print(f"- Sindicato (5%): {sindicato:.2f}R$")

liquido = salario_bruto - ir - inss - sindicato
print(f"=Salário Liquido: {liquido:.2f}")
                                                                                                                                           