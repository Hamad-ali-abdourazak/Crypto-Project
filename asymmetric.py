from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Helpers RSA : génération de clés, sérialisation, chiffrement, déchiffrement
class AsymmetricCrypto:
    @staticmethod
    def generate_rsa_keypair(key_size=2048):
        # génère une paire RSA
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def serialize_private_key(private_key, password: bytes = None) -> bytes:
        # retourne PEM; peut chiffrer avec password
        encryption_algo = serialization.BestAvailableEncryption(password) if password else serialization.NoEncryption()
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryption_algo
        )

    @staticmethod
    def serialize_public_key(public_key) -> bytes:
        # retourne PEM de la clé publique
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    @staticmethod
    def encrypt(message: str, public_key) -> bytes:
        # chiffre avec OAEP+SHA256
        return public_key.encrypt(
            message.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def decrypt(ciphertext: bytes, private_key) -> str:
        # déchiffre et renvoie UTF-8
        return private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode('utf-8')
