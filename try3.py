try:
    print(calango)
    total = "gato" + 35
    import controle
    print("Tudo OK")

except TypeError:
    print("Tipo de dado incorreto. Verifique.")
    
except ModuleNotFoundError:
    print("Módulo a ser importado não foi localizado.")

except:
    print("Deu erro.")
    raise

finally:
    print("Obrigado por usar esse programa.")