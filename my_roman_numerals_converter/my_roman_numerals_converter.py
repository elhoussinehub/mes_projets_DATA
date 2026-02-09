def my_roman_numerals_converter(param_1) :
    
    valeurs = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    resultat = str()

    for valeur , symbol in valeurs :
        while param_1 >= valeur :
            resultat += symbol
            param_1 -= valeur

    return resultat
#print(my_roman_numerals_converter(2008))
