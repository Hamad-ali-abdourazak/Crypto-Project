from cryptography.fernet import Fernet

# Helpers Fernet : génération de clé, chiffrement, déchiffrement
class SymmetricCrypto:
    @staticmethod
    def generate_key() -> bytes:
        # génère une clé Fernet
        return Fernet.generate_key()

    @staticmethod
    def encrypt(message: str, key: bytes) -> bytes:
        # chiffre un message UTF-8
        f = Fernet(key)
        return f.encrypt(message.encode('utf-8'))

    @staticmethod
    def decrypt(token: bytes, key: bytes) -> str:
        # déchiffre et retourne une chaîne UTF-8
        f = Fernet(key)
        return f.decrypt(token).decode('utf-8')
