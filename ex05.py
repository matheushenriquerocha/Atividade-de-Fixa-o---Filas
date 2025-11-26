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

# Criando a fila de clientes    
fila_clientes = Fila()

# Clientes chegando á loja
chegadas = ["Lucas", "Bianca", "Pedro", "Sofia", "Marcos"]

print("Clientes chegando á loja:")
for cliente in chegadas:
    fila_clientes.enfileirar(cliente)
    print(f"{cliente} entrou na fila.")

print("\nAtendimento Iniciado...\n")

# Enquanto existirem clientes, eles são atendidos
while not fila_clientes.vazia():
    cliente_atendido = fila_clientes.desenfileirar()
    print(f"Atendendo cliente: {cliente_atendido}")

print("\nTodos os clientes foram atendidos.")