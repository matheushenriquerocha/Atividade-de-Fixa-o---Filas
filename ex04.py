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

# Cria a fila de tarefas   
tarefas = Fila()

# Adiciona tarefas (simulação)
lista_tarefas = [
    "Processar imagem",
    "Gerar relatório",
    "Enviar e-mail",
    "Salvar backup",
    "Analisar logs"
]

for t in lista_tarefas:
    tarefas.enfileirar(t)

print("Servidor Iniciado...")
print("Tarefas pendentes:", tarefas.itens, "\n")

# Processamento das tarefas
while not tarefas.vazia():
    tarefa = tarefas.desenfileirar()
    print(f"Processando tarefa: {tarefa}")

print("\nTodas as tarefas foram processadas.")
