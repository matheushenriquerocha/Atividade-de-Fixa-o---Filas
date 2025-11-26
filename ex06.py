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

# Criando a fila de impressão    
fila_impressao = Fila()

# Documentos (nome, páginas)
documentos = [
    ("Relatorio_Final.pdf", 12),
    ("Ficha_Cadastro.docx", 3),
    ("Lista_Alunos.xlsx", 5),
    ("Contrato_Assinado.pdf", 8)
]

# Enfileirando documentos
for nome, paginas in documentos:
    fila_impressao.enfileirar((nome, paginas))
    print(f"Documento adicionado: {nome} ({paginas} páginas)")

print("\nIniciando impressão...")

# Processando a fila de impressão
while not fila_impressao.vazia():
    doc = fila_impressao.desenfileirar()
    nome, paginas = doc
    print(f"Imprimindo: {nome} - {paginas} página(s)")

print("\nTodos os documentos foram impressos.")
