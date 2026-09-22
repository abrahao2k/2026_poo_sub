'''11. crie uma função que escreve por extenso qualquer
número entre 1 e 100. ex.: extenso(23) >> "vinte e três" '''

def extenso(n):
    
    if n == 100 : return "cem"
    
    unidades = ["","um","dois","três","quatro","cinco","seis","sete",
                #0  #1     #2    #3...
                "oito", "nove"]
    
    especiais = {10:"dez", 11:"onze", 12:"doze", 13:"treze",
                 14:"quatorze", 15:"quinze", 16:"dezesseis",
                 17:"dezessete",18:"dezoito",19:"dezenove"}
    
    dezenas = ["", "", "vinte","trinta","quarenta","cinquenta",
               #0  #1    #2      #3...
               "sessenta","setenta","oitenta","noventa"]
    
    if n < 10 : return unidades[n]  # de 1 a 9
    
    if n < 20 : return especiais[n] # de 10 a 19
    
    dezena  = n // 10  # pega a dezena
    unidade = n %  10  # pega o resto (unidade)
    
    if unidade == 0 : return dezenas[dezena]
    
    return dezenas[dezena] + " e " + unidades[unidade]

#################################################################

for x in range(1,101):
    print( extenso(x) )