import requests
import sys
import operator
from bs4 import BeautifulSoup

from . import ignorados, args

class Minerador:
    max_paginas = 1
    max_resultados = 40

    def __init__(self):
        self.simbolos = ignorados.simbolos
        self.ignorar_palavras = ignorados.palavras
        self.ignorar_sites = ignorados.sites

    def sem_simbolos(self, palavra):
        for simbolo in self.simbolos:
            if palavra.find(simbolo) != -1:
                return False
        return True

    def ignorar(self, palavra):
        return palavra.lower() in self.ignorar_palavras

    def ignorar_site(self, url):
        for site in self.ignorar_sites:
            if url.find(site) != -1:
                return True
        return False

    def pesquisar(self, assunto):
        url = "https://google.com.br/search"
        params = {"q": assunto}
        links = []
        headers = {
            "accept-language": "pt-BR,pt;q=0.9,en;q=0.8",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
            }
        for pagina in range(self.max_paginas):
            try:
                params["start"] = pagina*10
                r = requests.get(
                        url ,
                        params=params,
                        headers=headers
                    )

                soup = BeautifulSoup(r.text, "html.parser")
                conteiner = soup.findAll("h3", class_="r")

                for link_c in conteiner:
                    link = link_c.find("a")['href']
                    if not link in links and not self.ignorar_site(link):
                        links.append(link)
            except:
                break
        return links

    def frequencia(self, links):
        frequencia = {}

        for link in links:
            try:
                r = requests.get(
                    link,
                    headers={
                        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 \
                        Safari/537.36"}
                    )

                soup = BeautifulSoup(r.text, "html.parser")
                palavras = soup.find("body").text.split(" ")

                for palavra in palavras:
                    if not palavra in frequencia:
                        if self.sem_simbolos(palavra) and not self.ignorar(palavra):
                            frequencia[palavra] = 1
                    else:
                        frequencia[palavra] += 1
            except: continue

        frequencia = sorted(
                        frequencia.items(),
                        key=operator.itemgetter(1),
                        reverse=True)
        return frequencia

    def exibir(self, sites, frequencia):
        print("Sites utilizados para mineração:")
        for i in range(len(sites)):
            print(str(i)+":", sites[i])

        print("\n\nResultados:")
        for i in range(self.max_resultados):
            try:
                if i % 2 == 0:
                    if not i == 0: print()
                texto = frequencia[i][0]+"("+str(frequencia[i][1])+")"
                print(str(i+1)+":", " "*(2 - len(str(i+1))), texto, end=" "*(22-len(texto)))
            except:
                break
        print()

    def iniciar(self, assunto):
        pesquisa = self.pesquisar(assunto)
        frequencia = self.frequencia(pesquisa)
        self.exibir(pesquisa, frequencia)

if __name__ == "__main__":
    mine = Minerador()
    assunto = args.args['main'][0]

    if args.is_set('-p'):
        mine.max_paginas = int(args.get('-p'))
    if args.is_set('-r'):
        mine.max_resultados = int(args.get('-r'))
    if args.is_set('-is'):
        mine.ignorar_sites = args.get('-is').split(',')
    if args.is_set('-iS'):
        mine.simbolos = args.get('-iS').split(',')
    if args.is_set('-ip'):
        mine.ignorar_palavras = args.get('-ip').split(',')
    if args.is_set('-ais'):
        mine.ignorar_sites.extend(args.get('-ais').split(','))
    if args.is_set('-aiS'):
        mine.simbolos.extend(args.get('-aiS').split(','))
    if args.is_set('-aip'):
        mine.ignorar_palavras.extend(args.get('-aip').split(','))

    mine.iniciar(assunto)
