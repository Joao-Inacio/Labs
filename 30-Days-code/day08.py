n = int(input())

lista: dict = {}

for _ in range(0, n):
    key, value = input().strip().split()
    lista[key] = value

while True:
    try:
        name = str(input())
        if name in lista:
            print(f"{name}={lista[name]}")
        else:
            print("Not found")
    except EOFError:
        break
        

