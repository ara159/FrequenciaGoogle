import sys

opcoes_lista = ['-p', '-r', '-is', '-iS', '-ip', '-ais', '-aiS', '-aip']

ajuda = """Frequencia.py 0.0.1
Feito por Ara159 03/2018

Modo de uso:
    python3 frequencia.py pesquisa [--help] [-p paginas] [-r resultados] [-is sites] [-iS sibolos] [-ip palavras] [-ais sites] [-aiS simbolos] [-aip palavras]

    -p: Paginas de pesquisa google
    -r: Quantidade de resultados a serem exibidos
    -is: Lista de sites que deseja ignorar (separados por virgula)
    -iS: Lista de simbolos que deseja ignorar (separados por virgula)
    -ip: Lista de palavras que deseja ignorar (separadas por virgula)
    -ais: Adiciona lista de sites que deseja ignorar (separados por virgula) à lista já existente
    -aiS: Adiciona lista de simbolos que deseja ignorar (separados por virgula) à lista já existente
    -aip: Adiciona lista de palavras que deseja ignorar (separados por virgula) à lista já existente
    --help: Exibe esta tela de ajuda
"""

args = {}
args["main"] = []

def paramentros_ivalidos():
    texto = """Parâmetros inválidos.
--help para obter ajuda."""
    print(texto)
    exit(1)

def is_set(valor):
    global args
    return valor in args

def get(param):
    global args
    if is_set(param):
        return args[param]
    else: return None

if "--help" in sys.argv:
    print(ajuda)
    exit(0)

i = 1
while i < len(sys.argv):
    try:
        act = sys.argv[i]
        if act[0] == "-":
            args[act] = sys.argv[i+1]
            i+=1
        else:
            args["main"].append(act)
        i+=1
    except:
        paramentros_ivalidos()

if len(args['main']) == 0:
    paramentros_ivalidos()
