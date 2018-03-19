# FrequenciaGoogle
Verifica as palavras mais comuns entre vários sites dentro de uma pesquisa google qualquer.

# Intruções
Pacotes necessários:

	BeatifulSoup
	
Modo de uso:

	python3 -m frequencia 'pesquisa' [--help] [-p paginas] [-r resultados] [-is sites] [-iS sibolos] [-ip palavras] [-ais sites] [-aiS simbolos] [-aip palavras]
Onde "n" é a quantidade de páginas google que será avaliada.

    -p: Paginas de pesquisa google
    -r: Quantidade de resultados a serem exibidos
    -is: Lista de sites que deseja ignorar (separados por virgula)
    -iS: Lista de simbolos que deseja ignorar (separados por virgula)
    -ip: Lista de palavras que deseja ignorar (separadas por virgula)
    -ais: Adiciona lista de sites que deseja ignorar (separados por virgula) à lista já existente
    -aiS: Adiciona lista de simbolos que deseja ignorar (separados por virgula) à lista já existente
    -aip: Adiciona lista de palavras que deseja ignorar (separados por virgula) à lista já existente
    --help: Exibe esta tela de ajuda

As páginas google normalmente fornecem 10 links, então se você quiser avaliar 30 links será necessário 3 páginas google.

Espero que seja util a alguém :)
