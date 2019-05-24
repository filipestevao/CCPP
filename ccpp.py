#!/usr/bin/env python3

# Creep Curve Points Projection (CCPP)
# Autor: Filipe Estevão de Freitas

from tkinter import *
from time import *

# Constantes
TEXTO_TITULO = ('Verdana', '14', 'bold')
TEXTO = ('Verdana', '14')

class CCPP(object):
    def __init__(self):
        # Cria o conteiner principal do programa
        self.root = Tk()
        self.root.title("CCPP")
        self.root.resizable(False, False)
        # Funções
        self.criaFrames()
        self.criaWidgets()
        # mainloop
        self.root.mainloop()

    def criaFrames(self):
        # Cria as frames
        self.frameDataInicio = Frame(self.root, padx=20)
        self.frameHoraInicio = Frame(self.root)
        self.frameDataFim = Frame(self.root, padx=20)
        self.frameHoraFim = Frame(self.root)
        self.framePontos = Frame(self.root)
        self.frameBotao = Frame(self.root, pady=15)
        # Empacota as frames
        self.frameDataInicio.pack()
        self.frameHoraInicio.pack()
        self.frameDataFim.pack()
        self.frameHoraFim.pack()
        self.framePontos.pack()
        self.frameBotao.pack()

    def criaWidgets(self):
        # frameDataInicio
        self.textoInicio = Label(self.frameDataInicio, text="Início do Ensaio", font=TEXTO_TITULO)
        self.labelDataI = Label(self.frameDataInicio, text="Data: ", width=7, anchor=E, font=TEXTO)
        self.entryDataI = Entry(self.frameDataInicio, font=TEXTO, width=11)
        self.textoInicio.pack(pady=5)
        self.labelDataI.pack(side=LEFT, pady=5)
        self.entryDataI.pack(pady=5)
        # frameHoraInicio
        self.labelHoraI = Label(self.frameHoraInicio, text="Horário: ", width=7, anchor=E, font=TEXTO)
        self.entryHoraI = Entry(self.frameHoraInicio, font=TEXTO, width=11)
        self.labelHoraI.pack(side=LEFT, pady=5)
        self.entryHoraI.pack(pady=5)
        # frameDataFim
        self.textoFim = Label(self.frameDataFim, text="Fim do Ensaio", font=TEXTO_TITULO)
        self.labelDataF = Label(self.frameDataFim, text="Data: ", width=7, anchor=E, font=TEXTO)
        self.entryDataF = Entry(self.frameDataFim, font=TEXTO, width=11)
        self.textoFim.pack(pady=5)
        self.labelDataF.pack(side=LEFT, pady=5)
        self.entryDataF.pack(pady=5)
        # frameHoraFim
        self.labelHoraF = Label(self.frameHoraFim, text="Horário: ", width=7, anchor=E, font=TEXTO)
        self.entryHoraF = Entry(self.frameHoraFim, font=TEXTO, width=11)
        self.labelHoraF.pack(side=LEFT, pady=5)
        self.entryHoraF.pack(pady=5)
        # framePontos
        self.labelPontos = Label(self.framePontos, text='Número de pontos', font=TEXTO_TITULO)
        self.entryPontos = Entry(self.framePontos, font=TEXTO, width=5, justify=CENTER)
        self.labelPontos.pack(pady=5)
        self.entryPontos.pack(pady=5)
        self.entryPontos.insert(0, '30')
        # frameBotao
        self.botaoCalc = Button(self.frameBotao, text="Calcular", command=self.calcular, font=TEXTO_TITULO)
        self.botaoCalc.pack()
        # PREENCHE ENTRADA AUTOMÁTICA (PARA TESTES)
        # self.entryDataI.insert(0, '01/01/2018')
        # self.entryHoraI.insert(0, '10:0:0')
        # self.entryDataF.insert(0, '2/1/18')
        # self.entryHoraF.insert(0, '15:30:0')

    def calcular(self):
        try:
            self.diaI, self.mesI, self.anoI = [int(i) for i in self.entryDataI.get().split('/')]
            self.horaI, self.minI, self.segI = [int(i) for i in self.entryHoraI.get().split(':')]
            self.diaF, self.mesF, self.anoF = [int(i) for i in self.entryDataF.get().split('/')]
            self.horaF, self.minF, self.segF = [int(i) for i in self.entryHoraF.get().split(':')]
            if 0 <= self.anoI <= 50:
                self.anoI += 2000
            if 0 <= self.anoF <= 50:
                self.anoF += 2000
        except ValueError:
            self.mensagemErro()
        else:
            self.criaJanelaCalculo()

    def mensagemErro(self):
        # Cria o conteiner do erro
        self.erro = Tk()
        self.erro.title("Erro")
        self.erro.resizable(False, False)
        # Mensagem de erro
        self.labelErro = Label(self.erro, text='ERRO', font=TEXTO_TITULO, fg='red')
        self.labelErro.pack(pady=5)
        self.commentErro = Label(self.erro, font=TEXTO)
        self.commentErro['text'] = 'Digite a data no formato DIA/MÊS/ANO\nExemplo: 01/01/2018 ou 1/1/18\n\nDigite o horário como\nHORA:MINUTO:SEGUNDO (formato 24h)\nExemplo: 15:30:00'
        self.commentErro.pack(padx=10, pady=5)
        self.botaoFechar = Button(self.erro, text="OK", command=lambda:self.erro.destroy(), font=TEXTO_TITULO)
        self.botaoFechar.pack(pady=5)
        # mainloop
        self.erro.mainloop()

    def criaJanelaCalculo(self):
        # Cria o conteiner do cálculo
        self.janelaCalc = Tk()
        self.janelaCalc.title("Cálculo")
        self.janelaCalc.resizable(False, False)
        # Funções
        self.defineInicio()
        self.defineFim()
        self.duracaoEnsaio()
        self.geraPontos()
        # Botões janela Calc
        self.frameBotCalc = Frame(self.janelaCalc)
        self.botaoCopiar = Button(self.frameBotCalc, text="Copiar", command=self.copiaTexto, font=TEXTO_TITULO)
        self.botaoFecharCalc = Button(self.frameBotCalc, text="Fechar", command=lambda:self.janelaCalc.destroy(), font=TEXTO_TITULO)
        self.frameBotCalc.pack(pady=10)
        self.botaoCopiar.pack(side=LEFT, padx=7)
        self.botaoFecharCalc.pack(side=RIGHT, padx=7)
        # mainloop
        self.janelaCalc.mainloop()

    def defineInicio(self):
        self.inicio = []
        teste = [self.anoI, self.mesI, self.diaI, self.horaI, self.minI, self.segI, 0, 0, 0]
        teste_verao = [self.anoI, self.mesI, self.diaI, self.horaI, self.minI, self.segI, 0, 0, 1]
        h_teste = localtime(mktime(struct_time(teste)))
        h_teste_verao = localtime(mktime(struct_time(teste_verao)))
        if teste[3] == h_teste[3]:
            self.inicio = teste.copy()
        elif teste_verao[3] == h_teste_verao[3]:
            self.inicio = teste_verao.copy()

    def defineFim(self):
        self.fim = []
        teste = [self.anoF, self.mesF, self.diaF, self.horaF, self.minF, self.segF, 0, 0, 0]
        teste_verao = [self.anoF, self.mesF, self.diaF, self.horaF, self.minF, self.segF, 0, 0, 1]
        h_teste = localtime(mktime(struct_time(teste)))
        h_teste_verao = localtime(mktime(struct_time(teste_verao)))
        if teste[3] == h_teste[3]:
            self.fim = teste.copy()
        elif teste_verao[3] == h_teste_verao[3]:
            self.fim = teste_verao.copy()

    def duracaoEnsaio(self):
        # Duração do ensaio
        self.seg_inicio = mktime(struct_time(self.inicio))
        self.seg_fim = mktime(struct_time(self.fim))
        self.dif = self.seg_fim - self.seg_inicio
        dur_dias = round((self.dif / (24 * 60 * 60)), 12)
        dur_hora = round(((dur_dias - int(dur_dias)) * 24), 12)
        dur_min = round(((dur_hora - int(dur_hora)) * 60), 12)
        dur_seg = round(((dur_min - int(dur_min)) * 60), 12)
        # widgets
        self.frameDuracao = Frame(self.janelaCalc)
        self.frameDuracao.pack(padx=10, pady=10)
        self.labelDuracao = Label(self.frameDuracao, text="Duração do ensaio:", font=TEXTO)
        self.labelDuracao.pack()
        self.textDuracao = Text(self.frameDuracao, font=TEXTO, width=25, height=2, borderwidth=0)
        self.textDuracao.tag_config('center', justify=CENTER)
        # imprime a duração
        self.textDuracao.insert('end', "%i dia(s), %i hora(s),\n%i minuto(s) e %i segundo(s)" % (dur_dias, dur_hora, dur_min, dur_seg), 'center')
        self.textDuracao.pack()

    def geraPontos(self):
        # Gera os pontos
        self.pontos = int(self.entryPontos.get())
        self.soma_ponto = round((self.dif / (self.pontos - 1)), 11)
        # Intervalo entre pontos
        self.frameIntervalo = Frame(self.janelaCalc)
        self.frameIntervalo.pack(pady=10)
        self.labelIntervalo = Label(self.frameIntervalo, font=TEXTO)
        self.labelIntervalo['text'] = "Intervalo entre pontos:"#"\n%g hora(s)" % (self.soma_ponto/3600)
        self.labelIntervalo.pack()
        self.textIntervalo = Text(self.frameIntervalo, font=TEXTO, width=25, height=1, borderwidth=0)
        self.textIntervalo.tag_config('center', justify=CENTER)
        self.textIntervalo.insert('end', "%g hora(s)" % (self.soma_ponto/3600), 'center')
        self.textIntervalo.pack()
        # Listbox
        self.frameListbox = Frame(self.janelaCalc)
        self.frameListbox.pack(padx=20)
        self.scrollbar = Scrollbar(self.frameListbox)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.pontosTela = Listbox(self.frameListbox, font=TEXTO, selectmode=EXTENDED)
        self.pontosTela.pack()
        self.scrollbar['command'] = self.pontosTela.yview
        self.pontosTela['yscrollcommand'] = self.scrollbar.set
        # Imprime os pontos na tela
        for i in range(self.pontos):
            vetor = localtime(round((self.seg_inicio + (self.soma_ponto * i)), 11))
            self.pontosTela.insert(END, '%02i/%02i/%i %02i:%02i:%02i' % (vetor[2], vetor[1], vetor[0], vetor[3], vetor[4], vetor[5]))

    def copiaTexto(self):
        self.root.clipboard_clear()
        self.root.clipboard_append('\n'.join(self.pontosTela.get(0, END)))


if __name__ == '__main__':
    CCPP()
