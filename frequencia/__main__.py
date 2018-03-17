from . import args, frequencia

if __name__ == "__main__":
    mine = frequencia.Minerador()
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
