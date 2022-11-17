from passlib.hash import pbkdf2_sha256


def gerar_hash(text):
    return pbkdf2_sha256.hash(text)


def verificar_hash(text, entry_hash):
    return pbkdf2_sha256.verify(text, entry_hash)
