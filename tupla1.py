# NÃO MODIFICA AO LONGO DO PROGRAMA
# TUPLA

cores = ('azul', 'verde', 'preto', 'cinza')
          #  0       1        2        3

print(cores)
print(cores[0])

#cores[0] = 'branco'  #não aceita modificar

listacores = list(cores) # converte tupla em lista

listacores[0] = 'branco'
print(listacores)
