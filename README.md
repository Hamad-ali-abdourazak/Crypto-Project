# crypto-simple

Un petit projet de démonstration cryptographique en Python utilisant la bibliothèque `cryptography`.

Fichiers :
- `symmetric.py` : helpers Fernet (chiffrement symétrique)
- `asymmetric.py` : génération de clés RSA et chiffrement/déchiffrement
- `demo.py` : script de démonstration

Démarrage rapide :
1. python -m venv .venv
2. .\.venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. python demo.py
 
Description
-----------
Ce dépôt contient des exemples simples pour illustrer deux modes de chiffrement courants :

- Chiffrement symétrique (Fernet) : facile à utiliser, adapté aux petits messages ou aux clés partagées.
- Chiffrement asymétrique (RSA) : permet d'échanger des messages sans partager de clé secrète au préalable.

Objectifs pédagogiques
----------------------
- Montrer comment générer une clé Fernet, chiffrer et déchiffrer un message.
- Générer une paire de clés RSA, chiffrer avec la clé publique et déchiffrer avec la clé privée.
- Présenter de bonnes pratiques de base : afficher les sorties binaires en base64 pour la lisibilité, ne jamais partager les clés privées en clair.

Installation
------------
1. Créer un environnement virtuel :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Installer les dépendances :

```powershell
pip install -r requirements.txt
```

Utilisation
-----------
Exécuter la démonstration (comprend les exemples symétrique et asymétrique) :

```powershell
python demo.py
```

Exemples de fonctions disponibles
--------------------------------
- `symmetric.generate_key()` → retourne une clé Fernet (bytes)
- `symmetric.encrypt(message: bytes, key: bytes)` → retourne le token chiffré (bytes)
- `symmetric.decrypt(token: bytes, key: bytes)` → retourne le message original (bytes)

- `asymmetric.generate_rsa_keypair()` → génère une paire (privée, publique)
- `asymmetric.encrypt(message: bytes, public_key)` → chiffre avec OAEP+SHA256
- `asymmetric.decrypt(ciphertext: bytes, private_key)` → déchiffre le ciphertext

Remarques de sécurité
---------------------
- Ne stockez jamais une clé privée sans protection. Utilisez un magasin de clés sécurisé (HSM, keystore chiffré) pour des usages en production.
- Les exemples ici sont éducatifs : pour des fichiers volumineux, préférez un schéma hybride (chiffrer le contenu avec une clé symétrique, chiffrer la clé symétrique avec RSA).
- Évitez d'exposer des clés ou des secrets dans le code ou dans le dépôt public.

Structure du dépôt
------------------
- `symmetric.py` — utilitaires pour Fernet (génération de clé, chiffrement/déchiffrement)
- `asymmetric.py` — génération RSA, sérialisation et opérations de chiffrement/déchiffrement
- `demo.py` — script d'exemple lisible et commenté (sorties en français)
- `requirements.txt` — dépendances nécessaires (cryptography)
- `.gitignore` — règles d'exclusion (virtualenv, caches Python, etc.)

Licence
-------
Par défaut, aucun fichier LICENSE n'est inclus. Si vous souhaitez un dépôt open-source, je peux ajouter une licence standard (MIT, Apache 2.0, ...). Indiquez votre préférence.

Contribuer
----------
Contributions bienvenues : issues pour signaler des améliorations ou des corrections. Pour des modifications importantes (tests, CI, packaging), ouvrez une pull request.

Contact
-------
Pour toute question ou demande spécifique (ex : sauvegarde des clés PEM, CLI, tests unitaires), répondez à ce message et je m'en occupe.
