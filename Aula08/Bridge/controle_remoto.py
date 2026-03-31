# Importa recursos para criação de classes abstratas
from abc import ABC, abstractmethod

# =========================
# IMPLEMENTAÇÃO (Implementor)
# =========================

class Dispositivo(ABC):
    """
    Classe abstrata que define a interface comum
    para todos os dispositivos (TV, Rádio, etc.)
    """

    @abstractmethod
    def ligar(self):
        pass  # Método que deve ser implementado pelas subclasses

    @abstractmethod
    def desligar(self):
        pass  # Método que deve ser implementado pelas subclasses

    @abstractmethod
    def set_volume(self, volume):
        pass  # Define o volume do dispositivo

# =========================
# IMPLEMENTAÇÕES CONCRETAS
# =========================

class TV(Dispositivo):
    """
    Implementação concreta de um dispositivo do tipo TV
    """

    def __init__(self):
        self.volume = 10  # Volume inicial da TV

    def ligar(self):
        print("TV ligada")  # Simula ligar a TV

    def desligar(self):
        print("TV desligada")  # Simula desligar a TV

    def set_volume(self, volume):
        self.volume = volume  # Atualiza o volume
        print(f"Volume da TV: {self.volume}")  # Mostra o novo volume

class Radio(Dispositivo):
    """
    Implementação concreta de um dispositivo do tipo Rádio
    """

    def __init__(self):
        self.volume = 5  # Volume inicial do rádio

    def ligar(self):
        print("Rádio ligado")  # Simula ligar o rádio

    def desligar(self):
        print("Rádio desligado")  # Simula desligar o rádio

    def set_volume(self, volume):
        self.volume = volume  # Atualiza o volume
        print(f"Volume do Rádio: {self.volume}")  # Mostra o novo volume

# =========================
# ABSTRAÇÃO (Abstraction)
# =========================

class ControleRemoto:
    """
    Classe de abstração que representa um controle remoto genérico.
    Ela NÃO sabe detalhes do dispositivo, apenas usa a interface.
    """

    def __init__(self, dispositivo):
        # Aqui ocorre o BRIDGE:
        # o controle mantém uma referência para um dispositivo
        self.dispositivo = dispositivo

    def ligar(self):
        # Delegação da chamada para o dispositivo
        self.dispositivo.ligar()

    def desligar(self):
        # Delegação da chamada para o dispositivo
        self.dispositivo.desligar()

# =========================
# ABSTRAÇÃO REFINADA
# =========================

class ControleAvancado(ControleRemoto):
    """
    Extensão da abstração básica, adicionando novas funcionalidades
    """

    def aumentar_volume(self):
        print("Aumentando volume...")
        # Define um volume maior diretamente no dispositivo
        self.dispositivo.set_volume(20)

    def diminuir_volume(self):
        print("Diminuindo volume...")
        # Define um volume menor diretamente no dispositivo
        self.dispositivo.set_volume(2)

# =========================
# CLIENTE (Uso do sistema)
# =========================

if __name__ == "__main__":

    # Cria instâncias dos dispositivos (implementações)
    tv = TV()
    radio = Radio()

    # Cria controles associados aos dispositivos
    controle_tv = ControleRemoto(tv)  # Controle básico para TV
    controle_radio = ControleAvancado(radio)  # Controle avançado para rádio

    # Operações com a TV
    print("\n--- Controle da TV ---")
    controle_tv.ligar()
    controle_tv.desligar()

    # Operações com o Rádio
    print("\n--- Controle do Rádio ---")
    controle_radio.ligar()
    controle_radio.aumentar_volume()
    controle_radio.diminuir_volume()
    controle_radio.desligar()