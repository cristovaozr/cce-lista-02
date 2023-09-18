#!/usr/bin/env python3

# poly_division - Código comum de divisão polinomial
# Códigos Corretores de Erro - PPGEE UFPE 2023.2
# Autor: Cristóvão Zuppardo Rufino <cristovao.rufino@ufpe.br>
#
# Para informações sobre a licença, ver o arquivo LICENSE

import math


def perform_division(poly_src: int, src_deg: int, poly: int, poly_deg: int, debug=False) -> (int, int):
    """Performs the division of polynomial "poly_src" by polynomial "poly"

    Parameters
    ----------
        poly_src : int
        Integer representation of the division polynomial
        src_deg : int
        Degree of the poly_src polynomial
        poly : int
        Integer representation of the divider polynomial
        poly_deg : int
        Degree of the poly polynomial
    
    Returns
    -------
        int, int
        Quocient and Remainder of the division
    """
    bit_flag = 1 << src_deg
    poly_int = poly << (src_deg - poly_deg)
    quotient = 0
    while poly_src >= poly:
        if poly_src & bit_flag > 0:
            if debug:
                print("poly={}".format(bin(poly_src)[2:]))
            poly_src ^= poly_int
            quotient |= 1

        quotient <<= 1
        poly_int >>= 1
        bit_flag >>= 1

    remainder = poly_src

    return quotient, remainder
    

def check_if_irreducible(poly: int, poly_deg: int, debug=False) -> (int, int):
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

    return perform_division(check_poly_int, check_poly_deg, poly, poly_deg, debug)