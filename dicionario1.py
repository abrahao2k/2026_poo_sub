aluno = ["Ana Beatriz", "Informática", 3, 89]
            #  0             1         2   3

dic = { "nome"  : "Ana Beatriz",
        "curso" : "Informática",
        "serie" : 3,
        "ira"   : 89}

       #chaves  : valores
       #keys    : values

print(dic)
print(dic["nome"])

dic["turno"] = "Manhã" # acrescenta novas informações ao dic
print(dic)

del(dic["serie"]) # remover uma informação
print(dic)