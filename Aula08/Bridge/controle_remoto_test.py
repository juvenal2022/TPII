from controle_remoto import TV, Radio, ControleRemoto, ControleAvancado

def test_tv_ligar(capsys):
    tv = TV()
    controle = ControleRemoto(tv)

    controle.ligar()

    captured = capsys.readouterr()
    assert "TV ligada" in captured.out

def test_radio_volume(capsys):
    radio = Radio()
    controle = ControleAvancado(radio)
    
    controle.aumentar_volume()

    captured = capsys.readouterr()
    assert "Volume do Rádio: 20" in captured.out

def test_tv_desligar(capsys):
    tv = TV()
    controle = ControleRemoto(tv)

    controle.desligar()

    captured = capsys.readouterr()
    assert "TV desligada" in captured.out