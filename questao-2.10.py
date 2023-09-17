#!/usr/bin/env python3

# Questão 2.10 - Códigos Corretores de Erro - PPGEE UFPE 2023.2
# Autor: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>
#
# Para informações sobre a licença, ver o arquivo LICENSE

import sys
import math
from poly_division import perform_division

def check_if_irreducible(poly: int, poly_deg: int) -> (int, int):
    """Checks wheter a polynomial is irreducible. This is done by checking if poly
    divides x^(2^poly_deg - 1) + 1

    Parameters
    ----------
        poly : int
        Integer representation of the polynomial to check
        poly_deg : int
        Degree of the poly polynomial
    
    Returns
    -------
        int, int
        Quotient and Remainder of the test. The remainder should be zero, if poly is irreducible
    """
    check_poly_deg = int(math.pow(2, poly_deg) - 1)
    check_poly_int = (1 << check_poly_deg) | 1

    return perform_division(check_poly_int, check_poly_deg, poly, poly_deg)


def main():
    quotient, remainder = check_if_irreducible(int("101001", 2), 5)
    print("Quociente: {}, resto: {}".format(bin(quotient)[2:], bin(remainder)[2:]))

    if remainder == 0:
        print("O polinômio é irredutível")
    else:
        print("O polinômio não é irredutível")

    return 0


if __name__ == "__main__":
    sys.exit(main())
