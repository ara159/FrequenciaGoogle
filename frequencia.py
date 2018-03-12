import requests
import sys
import operator
from bs4 import BeautifulSoup

class Minerador:
    def __init__(self):
        self.simbolos = ["\n", "=", "+", "(", ")", "*", ",", ".", "#", "!", "$",
            "_", "%", "[", "]", "{", "}", "/", "&","—", "|", "«", ":", "'", "<",
            ">", "–", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.ignorar_palavras = ["", "de", "o", "a", "do", "que", "em", "da",
            "para", "um", "dois", "no", "os", "mais", "-", "se", "como", "dos", "foi",
            "e", "com", "uma", "na", "não", "seu", "of", "sua", "por", "as", "ao",
            "The", "ele", "the", "é", "das", "var", "Em", "seus", "ou",
            "if", "and", "era", "anos", "foram", "minutos", "new", "ele", "von", "sobre", "mas",
            "ser", "pelo", "b", "entre", "à", "até", "1", "nos", "então", "quando", "in",
            "pela", "suas", "sem", "ter", "fim", "pode", "vez", "todo", "às", "são",
            "já", "ela", "aos", "nas", "mesmo", "maior", "menor", "vai", "grande", "tem",
            "será", "você", "há", "muito", "ainda", "mil", "sendo", "h", "?", "partir",
            "eu", "diz", "te", "ul", "li", "está", "só", "disse", "caso", "isso", "após",
            "leia", "dizem", "também", "tempo", "contenham", "seria", "conversa",
            "comentários", "conta"]
        self.ignorar_sites = ["youtube", "letras", "vagalume", "facebook", "twitter",
            "tumblr", "cifraclub", "instagram", "olx", "americanas", "mercadolivre"]

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

    def pesquisar(self, assunto, paginas=1):
        url = "https://google.com.br/search"
        params = {"q": assunto}
        links = []
        headers = {
            "accept-language": "pt-BR,pt;q=0.9,en;q=0.8",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
            }
        for pagina in range(paginas):
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
                if not self.ignorar_site(link):
                    links.append(link)
        return links

    def frequencia(self, links):
        frequencia = {}
        for link in links:
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
        for i in range(40):
            if i % 2 == 0:
                if not i == 0: print()
            texto = frequencia[i][0]+"("+str(frequencia[i][1])+")"
            print(str(i+1)+":", " "*(2 - len(str(i+1))), texto, end=" "*(22-len(texto)))
        print()

    def run(self, assunto, pagina=1):
        pesquisa = self.pesquisar(assunto, pagina)
        frequencia = self.frequencia(pesquisa)
        self.exibir(pesquisa, frequencia)

if __name__ == "__main__":
    assunto = sys.argv[1]
    paginas = int(sys.argv[2])
    Minerador().run(assunto, paginas)
