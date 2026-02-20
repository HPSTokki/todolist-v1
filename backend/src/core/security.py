from pwdlib import PasswordHash

hash_context = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return hash_context.hash(password)

def verify_password(password: str, hash_password: str) -> bool:
    return hash_context.verify(password, hash_password)