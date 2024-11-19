import secrets

from argon2 import PasswordHasher

password_hasher = PasswordHasher()


class ArgonUtils:

    @staticmethod
    def generate_secret_key() -> str:
        random_key: str = secrets.token_urlsafe(32)  # Generate a random password
        hasher = PasswordHasher()
        secret_key: str = hasher.hash(random_key)
        return secret_key
