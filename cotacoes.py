# Importar os módulos
from kivy.app import App
from kivy.lang import Builder
import requests as rq


GUI = Builder.load_file('my.kv')

# Criar a classe que armazena os widgets


class WidgetPrincipal(App):
    def build(self):
        return GUI

    def mostrar_cotacoes(self):
        cotacoes = rq.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        cotacoes = cotacoes.json()
        cotacao_dolar = cotacoes['USDBRL']['bid']
        cotacao_euro = cotacoes['EURBRL']['bid']

        euro = float(cotacao_euro)
        dolar = float(cotacao_dolar)

        self.root.ids['lbl_cotacao1'].text = cotacao_euro

        self.root.ids['lbl_cotacao2'].text = cotacao_dolar

        if euro <= 5.4200:
            self.root.ids['lbl_cotacao1'].text = 'Euro ta bom! Bora comprar:   ' + cotacao_euro
            print("\n Euro ta bom! Bora comprar: ", str(cotacao_euro))

        elif euro >= 5.4700:
            self.root.ids['lbl_cotacao1'].text = 'Caro demais para comprar:   ' + cotacao_euro
            print("\n Caro demais pra comprar euro: ", str(cotacao_euro))

        else:
            print("\n Euro: ", str(cotacao_euro))

        if dolar <= 5.3000:
            self.root.ids['lbl_cotacao2'].text = 'Bora comprar dolar:  ' + cotacao_dolar
            print("\n Bora comprar dolar: ", str(cotacao_dolar))

        elif dolar >= 5.4000:
            self.root.ids['lbl_cotacao2'].text = 'Caro demais pra comprar dolar:  ' + cotacao_dolar
            print("\n Caro demais pra comprar dolar: ", str(cotacao_dolar))

        else:
            print("\n Dolar: ", str(cotacao_dolar))

    def on_start(self):
        self.mostrar_cotacoes()


if __name__ == '__main__':
    WidgetPrincipal().run()
