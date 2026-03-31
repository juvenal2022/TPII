import json
import csv
from io import StringIO

# ========================================
# Adaptee (Sistema legado que fornece CSV)
# ========================================
class SistemaCSV:
    def get_dados_csv(self): # Simula um sistema legado que retorna dados em CSV
        return "nome,idade\nMaria,25\nJoão,30\nAna,22"

# ========================================
# Target (Interface esperada pelo cliente)
# ========================================
class InterfaceJSON:
    def get_dados(self): # Método qua deve retornar dados no formato JSON
        raise NotImplementedError("Este método deve ser implementado.")
    
# ========================================
# Adapter (Converte CSV -> JSON)
# ========================================
class CSVparaJSONAdapter(InterfaceJSON):
    def __init__(self, sistema_csv): # Função para receber uma instância do sistema legado (Adptee)
        self.sistema_csv = sistema_csv

    def get_dados(self): # Função para converter os dados CSV para JSON
        # 1. Obtém os dados do sistema legado
        csv_data = self.sistema_csv.get_dados_csv()
        # 2. Converte a string CSV em um "arquivo" em memória
        arquivo_csv = StringIO(csv_data)
        # 3. Usa DictReader para transformar cada linha em dicionário
        leitor = csv.DictReader(arquivo_csv)
        # 4. Converte o conteúdo em lista de dicionários
        lista_dados = []
        for linha in leitor:
            lista_dados.append(linha)
        # 5. Converte a lista para JSON
        json_data = json.dumps(lista_dados, indent=2, ensure_ascii=False)

        return json_data

# ========================================
# Cliente (Usa apenas a Interface JSON)
# ========================================
def main():
    # Instancia o sistema legado
    sistema_legado = SistemaCSV()
    # Cria o adapter
    adaptador = CSVparaJSONAdapter(sistema_legado)
    # Cliente consome como JSON
    dados_json = adaptador.get_dados()

    print("Dados convertidos para JSON: ")
    print(dados_json)

# ========================================
# Execução do programa
# ========================================
if __name__ == "__main__":
    main()