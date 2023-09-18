#!/usr/bin/env python3

# Questão 2.10 - Códigos Corretores de Erro - PPGEE UFPE 2023.2
# Autor: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>
#
# Para informações sobre a licença, ver o arquivo LICENSE

import sys
from poly_division import check_if_irreducible


def main():
    quotient, remainder = check_if_irreducible(int("101001", 2), 5, True)
    print("Quociente: {}, resto: {}".format(bin(quotient)[2:], bin(remainder)[2:]))

    if remainder == 0:
        print("O polinômio é irredutível")
    else:
        print("O polinômio não é irredutível")

    return 0


if __name__ == "__main__":
    sys.exit(main())
