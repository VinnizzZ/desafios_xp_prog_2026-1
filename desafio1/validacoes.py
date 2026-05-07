import re

def ehEmailValido(email: str) -> bool:
    email_valido = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_valido, email):
        return True
    return False

def ehCPFValido(cpf: str) -> bool:
    cpf_valido = r'^[0-9]{3,}+\.[0-9]{3,}+\.[0-9]{3,}+-[0-9]{2,}$'
    if re.match(cpf_valido, cpf):
        return True
    return False

def ehSenhaForte(senha: str) -> bool:
    if len(senha) >= 8:
        maiuscula = re.search(r'[+A-Z]', senha)
        minuscula = re.search(r'[+a-z]', senha)
        if maiuscula and minuscula:
            numero = re.search(r'[+0-9]', senha)
            especial = re.search(r'[^a-zA-Z0-9]', senha)
            if numero and especial:
                return True
    return False