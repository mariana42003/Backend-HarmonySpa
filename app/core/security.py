
from pwdlib import PasswordHash

# Crea el administrador de hashing con el algoritmo recomendado.
password_hasher = PasswordHash.recommended()


# Genera un hash seguro para almacenar la contraseña.
def hash_password(password: str) -> str:

    # Verifica que la contraseña tenga al menos 12 caracteres.
    if len(password) < 12:
        raise ValueError(
            "La contraseña debe tener al menos 12 caracteres"
        )

    # Genera y devuelve el hash de la contraseña.
    return password_hasher.hash(password)


# Verifica si una contraseña coincide con su hash.
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    # Compara la contraseña ingresada con el hash almacenado.
    return password_hasher.verify(
        plain_password,
        hashed_password
    )
