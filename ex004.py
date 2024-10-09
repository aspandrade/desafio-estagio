#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

percentual_sp = (sp*100) / total
percentual_rj = (rj*100) / total
percentual_mg = (mg*100) / total
percentual_es = (es*100) / total
percentual_outros = (outros*100) / total

print(f"Percentual de representação de SP: {percentual_sp:.2f}%")

print(f"Percentual de representação do RJ: {percentual_rj:.2f}%")

print(f"Percentual de representação de MG: {percentual_mg:.2f}%")

print(f"Percentual de representação de ES: {percentual_es:.2f}%")

print(f"Outros: {percentual_outros:.2f}%")

