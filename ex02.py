class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, elemento):
        self.itens.append(elemento)

    def desenfileirar(self):
        if not self.vazia():
            return self.itens.pop(0)
        else:
            return None 
 
    def vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

# Cria a fila de atendimento    
fila = Fila()

# Adiciona clientes na fila
clientes = ["Ana", "Carlos", "Mariana", "João", "Fernanda"]

for cliente in clientes:
    fila.enfileirar(cliente)

print("Iniciando atendimento...\n")

# Atende clientes até a fila ficar vazia
while not fila.vazia():
    atendido = fila.desenfileirar()
    print(f"Atendendo: {atendido}")

print("\nTodos os clientes foram atendidos.")
