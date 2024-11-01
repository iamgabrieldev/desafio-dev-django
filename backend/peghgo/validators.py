import re
from validate_docbr import CPF

def social_security_number_invalid(numero_social_security_number):
    social_security_number = CPF()
    social_security_number_valido = social_security_number.validate(numero_social_security_number)
    return not social_security_number_valido

def name_invalid(nome):
    return not nome.isalpha()

def phone_number__invalid(phone_number):
    # 86 99999-9999
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,phone_number)
    #print(resposta)
    return not resposta

def date_invalid(start_date,end_date):
    return end_date < start_date