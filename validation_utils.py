import random

def cpf_validator(cpf):
    cpf_num = ''.join(filter(str.isdigit, cpf))
    cpf_nine = cpf_num[0:9]
    first_check_digit = cpf_num[9]
    second_check_digit = cpf_num[10]

    if len(cpf_num) != 11:
        return False
    if cpf_num == cpf_num[0]*11:
        return False
    
    def complex_validation(cpf_nine, first_check_digit, second_check_digit):
        #transformação de tipos
        first_check_digit = int(first_check_digit)
        second_check_digit = int(second_check_digit)

        # Verify first check digit
        soma_regressiva = 10
        resultado = 0
        for digito in cpf_nine:
            resultado += int(digito) * soma_regressiva
            soma_regressiva -= 1
        rest = resultado % 11
        first_digit = 0 if rest <2 else 11 - rest

        if first_check_digit != first_digit:
            return False
        
        # Verify second check digit
        soma_regressiva = 11
        resultado = 0
        ten_cpf = cpf_nine + str(first_check_digit)
        for digit in ten_cpf:
            resultado += int(digit) * soma_regressiva
            soma_regressiva -=1
        rest = resultado%11
        second_digit = 0 if rest <2 else 11 - rest
        if second_check_digit != second_digit:
            return False
        
        return True
    return complex_validation(cpf_nine=cpf_nine, first_check_digit=first_check_digit, second_check_digit=second_check_digit)

def email_validator(email):
    if email.count('@') != 1:
        return False
    
    local, domain = email.split('@')

    if not local or not domain:
        return False

    if local[0] == '.' or local[-1] == '.':
        return False
    if '..' in local:
        return False

    allowed_local_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+/=?^_`{|}~.-")
    if any(ch not in allowed_local_chars for ch in local):
        return False

    if '.' not in domain:
        return False

    domain_parts = domain.split('.')
    if any(not part for part in domain_parts):
        return False

    allowed_domain_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-")
    for part in domain_parts:
        if part[0] == '-' or part[-1] == '-':
            return False
        if any(ch not in allowed_domain_chars for ch in part):
            return False

    if len(domain_parts[-1]) < 2:
        return False
    if len(email) > 254:
        return False

    return True

def phone_validator(phone):
    digits = ''.join(filter(str.isdigit, phone))

    if len(digits) not in [10, 11]:
        return False

    ddd = digits[:2]
    first_digit_after_ddd = digits[2]

    if not (11 <= int(ddd) <= 99):
        return False
    if len(digits) == 10:
        if first_digit_after_ddd in ['0', '1']:
            return False
    if len(digits) == 11:
        if first_digit_after_ddd != '9':
            return False
    return True