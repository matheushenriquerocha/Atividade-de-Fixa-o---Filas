class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, elemento):
        self.itens.append(elemento)

    def desenfileirar(self):
        if not self.vazia():
            return self.itens.pop(0)
        return None
    
    def vazia(self):
        return len(self.itens) == 0
    
    def tamanho(self):
        return len(self.itens)
    
    def inverter(self):
        # inverte a fila usando apenas recursos da lista
        self.itens.reverse() # opção 1
        # self.itens = self.itens[::-1] # opção 2

fila = Fila()

# adicionando elementos
numeros = [5, 15, 25, 35, 45, 55, 65, 75]
for n in numeros:
    fila.enfileirar(n)

print("Fila Original:", fila.itens)

# invertendo
fila.inverter()

print("Fila Invertida:", fila.itens)