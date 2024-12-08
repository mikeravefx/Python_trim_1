def calculate_power():
    """
    Calculates the power of a base number raised to an exponent.

    This function prompts the user to input a base number and an exponent,
    then calculates and prints the result of the base raised to the power
    of the exponent. The base number is rounded to two decimal places
    before the calculation.

    Parameters:
    None

    Returns:
    None
    """
    my_float_variable = float(input("Dime la base: "))
    exponente = float(input("Dime el exponente: "))
    print(round(my_float_variable, 2) ** exponente)