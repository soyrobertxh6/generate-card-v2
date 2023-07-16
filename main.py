print("Hola Gracias por probar generate-card v2")
print("ScriptbyRobertx")
print("Recuerda que las tarjetas de credito son aleatorias.")
print("Gracias.")

import random

for x in range(20): 
    
    n = [random.randint(0, 9) for _ in range(13)]

    n.insert(4, "-")
    n.insert(9, "-")
    n.insert(14, "-")

    codigo_verificacion = [random.randint(0, 9) for _ in range(3)]

    tarjeta_credito = "".join([str(i) for i in n] + [str(i) for i in codigo_verificacion])
    print("Tarjeta de Crédito:", tarjeta_credito)