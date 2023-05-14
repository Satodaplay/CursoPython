def suma(**Kwargs):

    total = 0

    for clave, valor in Kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total

suma(x=3, y=5, z=2)