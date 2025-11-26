class Fila:
    def __init__(self):
        self.itens = []

    # adiciona elemento no final
    def enfileirar(self, elemento):
        self.itens.append(elemento)

    # remove e retorna o primeiro elemento
    def desenfileirar(self):
        if not self.vazia():
            return self.itens.pop(0)
        else:
            return None # ou raise Exception("Fila vazia")

     # verifica se a fila está vazia   
    def vazia(self):
        return len(self.itens) == 0
    
    # retorna o tamanho da fila
    def tamanho(self):
        return len(self.itens)

fila = Fila()

# ler 5 números do usuário
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    fila.enfileirar(num)

print("\nRemovendo elementos da fila:\n")

# remove e imprime todos os elementos
while not fila.vazia():
    print(fila.desenfileirar())
