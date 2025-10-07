from symmetric import SymmetricCrypto
from asymmetric import AsymmetricCrypto
import base64


def demo_symmetric():
    print('--- Démonstration symétrique ---')
    key = SymmetricCrypto.generate_key()
    print('Clé générée :', key.decode())
    msg = 'Bonjour monde symétrique'
    token = SymmetricCrypto.encrypt(msg, key)
    # Fernet token is URL-safe base64 bytes, show as readable string
    print('Jeton chiffré (base64) :', token.decode())
    clear = SymmetricCrypto.decrypt(token, key)
    print('Message déchiffré :', clear)


def demo_asymmetric():
    print('\n--- Démonstration asymétrique ---')
    priv, pub = AsymmetricCrypto.generate_rsa_keypair()
    print('Paire RSA générée')
    msg = 'Exemple de chiffrement asymétrique'
    ct = AsymmetricCrypto.encrypt(msg, pub)
    # RSA ciphertext is binary; display in base64 for readability
    print('Chiffrement (base64) :', base64.b64encode(ct).decode())
    pt = AsymmetricCrypto.decrypt(ct, priv)
    print('Message déchiffré :', pt)


if __name__ == '__main__':
    demo_symmetric()
    demo_asymmetric()
