# CCPP
Creep Curve Points Projection

## Descrição

*Projeção de Pontos para a Curva de Fluência*

Programa simples desenvolvido para o facilitar a construção da curva de fluência. O usuário informa o início, o fim do ensaio e a quantidade de pontos da curva, então calcula-se o tempo total do ensaio, o intervalo entre cada ponto e são mostrados as datas e horários para se inserir na planilha dos dados de fluência.

## Dependências

* Python3
* Tkinter (interface gráfica em Python)

### Instalação no Windows

Baixar e instalar o Python3 [direto do site oficial](https://www.python.org/) (tkinter já incluso).

### Instalação em distribuições Linux

O Python3 vem instalado por padrão na maioria das distribuições Linux, porém é necessário instalar o Tkinter. Em algumas distribuições basta procurar `tkinter` na loja de aplicativos. Caso prefira usar o terminal, segue os comandos de instalação.

Para Ubuntu e derivados:
```
sudo apt install python3-tk
```

Para o Fedora:
```
sudo dnf install python3-tkinter
```

## Instalação do CCPP

### Instalação no Windows

* Baixar o arquivo `ccpp.py`.
* Renomar para `ccpp.pyw` (basta adicionar o `w` depois do `py`).
* Clicar duas vezes sobre `ccpp.pyw`.

### Instalação em distribuições Linux
Baixar o programa:
```
git clone https://github.com/filipestevao/CCPP.git
```
Navegar para a pasta CCPP:
```
cd CCPP
```
Dar permissão de execução para o arquivo `ccpp.py`:
```
chmod +x ccpp.py
```
Abrir o arquivo `ccpp.py`:
```
./ccpp.py
```
