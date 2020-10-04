class Contador_de_notas:
    def __init__(self, valor):
        self.__valor = valor
        if self.__valor % 5 != 0:
            raise ValueError('Valor não permitido!'
                             'Favor escolher um valor '
                             'divisível por 5.')
        self.cinco = "cinco"
        self.dez = "dez"
        self.vinte = "vinte"
        self.cinquenta = "cinquenta"
        self.cem = "cem"


    def possibiliadade_1(self):
        dicionario_notas = {
            self.cem: 0,
            self.cinquenta: 0,
            self.vinte: 0,
            self.dez: 0,
            self.cinco: 0,
        }

        valor_temp = self.__valor
        while valor_temp >= 100 and valor_temp > 0:
            dicionario_notas[self.cem] += 1
            valor_temp -= 100
        while valor_temp >= 50 and valor_temp > 0:
            dicionario_notas[self.cinquenta] += 1
            valor_temp -= 50
        while valor_temp >= 20 and valor_temp > 0:
            dicionario_notas[self.vinte] += 1
            valor_temp -= 20
        while valor_temp >= 10 and valor_temp > 0:
            dicionario_notas[self.dez] += 1
            valor_temp -= 10
        while valor_temp >= 5 and valor_temp > 0:
            dicionario_notas[self.cinco] += 1
            valor_temp -= 5


        return f" {dicionario_notas[self.cem]} nota(s) de {self.cem}, " \
               f"{dicionario_notas[self.cinquenta]} nota(s) de" \
               f" {self.cinquenta}, {dicionario_notas[self.vinte]}" \
               f" nota(s) de  {self.vinte}, {dicionario_notas[self.dez]}" \
               f" nota(s) de {self.dez} e" \
               f" {dicionario_notas[self.cinco]} nota(s) de" \
               f" {self.cinco}"

    def possibilidade_2(self):
        dicionario_notas = {
            self.cinquenta: 0,
            self.vinte: 0,
            self.dez: 0,
            self.cinco: 0,
        }

        valor_temp = self.__valor
        while valor_temp >= 50 and valor_temp > 0:
            dicionario_notas[self.cinquenta] += 1
            valor_temp -= 50
        while valor_temp >= 20 and valor_temp > 0:
            dicionario_notas[self.vinte] += 1
            valor_temp -= 20
        while valor_temp >= 10 and valor_temp > 0:
            dicionario_notas[self.dez] += 1
            valor_temp -= 10
        while valor_temp >= 5 and valor_temp > 0:
            dicionario_notas[self.cinco] += 1
            valor_temp -= 5


        return f" {dicionario_notas[self.cinquenta]} nota(s) de" \
               f" {self.cinquenta}, {dicionario_notas[self.vinte]}" \
               f" nota(s) de  {self.vinte}, {dicionario_notas[self.dez]}" \
               f" nota(s) de {self.dez} e" \
               f" {dicionario_notas[self.cinco]} nota(s) de" \
               f" {self.cinco}"

    def possibilidade_3(self):
        dicionario_notas = {
            self.vinte: 0,
            self.dez: 0,
            self.cinco: 0,
        }

        valor_temp = self.__valor
        while valor_temp >= 20 and valor_temp > 0:
            dicionario_notas[self.vinte] += 1
            valor_temp -= 20
        while valor_temp >= 10 and valor_temp > 0:
            dicionario_notas[self.dez] += 1
            valor_temp -= 10
        while valor_temp >= 5 and valor_temp > 0:
            dicionario_notas[self.cinco] += 1
            valor_temp -= 5

        return f" {dicionario_notas[self.vinte]}" \
               f" nota(s) de  {self.vinte}, {dicionario_notas[self.dez]}" \
               f" nota(s) de {self.dez} e" \
               f" {dicionario_notas[self.cinco]} nota(s) de" \
               f" {self.cinco}"

    def possibilidade_4(self):
        dicionario_notas = {
            self.dez: 0,
            self.cinco: 0,
        }

        valor_temp = self.__valor
        while valor_temp >= 10 and valor_temp > 0:
            dicionario_notas[self.dez] += 1
            valor_temp -= 10
        while valor_temp >= 5 and valor_temp > 0:
            dicionario_notas[self.cinco] += 1
            valor_temp -= 5
        return f" {dicionario_notas[self.dez]}" \
               f" nota(s) de {self.dez} e" \
               f" {dicionario_notas[self.cinco]} nota(s) de" \
               f" {self.cinco}"

    def possibilidade_5(self):
        dicionario_notas = {
            self.cinco: 0,
        }

        valor_temp = self.__valor
        while valor_temp % 5 == 0 and valor_temp > 0:
            dicionario_notas[self.cinco] += 1
            valor_temp -= 5
        return f" {dicionario_notas[self.cinco]}" \
               f" nota(s) de {self.cinco} "



    def mostrar_possibilidades(self):
        if self.__valor >= 100:
            return f"{self.possibiliadade_1()}.\n{self.possibilidade_2()}.\n" \
                   f"{self.possibilidade_3()}.\n{self.possibilidade_4()}.\n" \
                   f"{self.possibilidade_5()}"
        elif self.__valor < 100 and self.__valor >= 50 :
            return f"{self.possibilidade_2()}.\n" \
                   f"{self.possibilidade_3()}.\n{self.possibilidade_4()}.\n" \
                   f"{self.possibilidade_5()}"
        elif self.__valor < 50 and self.__valor >= 20:
            return f"{self.possibilidade_3()}.\n{self.possibilidade_4()}.\n" \
                   f"{self.possibilidade_5()}"
        elif self.__valor < 20 and self.__valor >= 10:
            return f"{self.possibilidade_4()}.\n" \
                   f"{self.possibilidade_5()}"
        else:
            return f"{self.possibilidade_5()}"









