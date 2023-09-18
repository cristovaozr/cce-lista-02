#!/usr/bin/env python3

# Questão 2.12 - Códigos Corretores de Erro - PPGEE UFPE 2023.2
# Autor: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>
#
# Para informações sobre a licença, ver o arquivo LICENSE

import sys
from poly_division import check_if_irreducible


def main():
    for poly in range(32, 64):
        # print("Verificando o polinômio {}...".format(bin(poly)[2:]))
        _, remainder = check_if_irreducible(poly, 5)
        if remainder == 0:
            print("{} -> Irredutível".format(bin(poly)[2:]))
        # else:
        #     print("{} -> Redutível".format(bin(poly)[2:]))

    return 0


if __name__ == "__main__":
    sys.exit(main())
