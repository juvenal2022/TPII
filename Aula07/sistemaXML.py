import json # Biblioteca para manipular JSON
import xml.etree.ElementTree as ET # Biblioteca padrão para trabalhar com XML

class SistemaXML: # Define a classe do sistema legado
    def get_dados_xml(self): # Método que retorna dados em XML
        return "<usuario><nome>João</nome><idade>30</idade></usuario>" # Retorna uma string em formato XML
    
class InterfaceJSON: # Define a interface esperada pelo sistema moderno
    def get_dados(self): # Método padrão que deve retornar dados em JSON
        pass # Método abstrato (sem implementação)

class XMLparaJSONAdapter(InterfaceJSON): # Adapter herda da interface esperada
    def __init__(self, sistema_xml): # Construtor recebe o objeto legado (adaptee)
        self.sistema_xml = sistema_xml # Armazena a referência do adaptee

    def get_dados(self):
        xml_data = self.sistema_xml.get_dados_xml() # Chama o método do sitema legado
        root = ET.fromstring(xml_data) # Converte a string XML em estrutura manipulável

        dados = {} # Cria um dicionário vazio para armazenar os dados convertidos
        for child in root: # Itera sobre os elementos XML
            dados[child.tag] = child.text # Converte cada tag em chave do dicionário

        return json.dumps(dados, ensure_ascii=False) # Converte o dicionário para JSON e retorna a string resultante

sistema_legado = SistemaXML() # Instancia o sistema antigo
adaptador = XMLparaJSONAdapter(sistema_legado) # Cria o adapter passando o sistema legado como parâmetro

print(adaptador.get_dados()) # Cliente usa interface JSON sem sbaer do XML

