# Application Flask pour la Brute Force de Fichiers ZIP et PDF

Cette application Flask permet de tenter de découvrir les mots de passe de fichiers ZIP et PDF en utilisant une attaque par force brute avec une liste de mots de passe.

## Prérequis

- Python 3.x
- Flask
- pyzipper
- pikepdf

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/Ppouts/Dechiffrement-MDP.git
    ```

2. Installez les dépendances :
    ```bash
    pip install flask pyzipper pikepdf
    ```

3. Modifiez les chemins dans le script principal (par exemple `app.py`) pour correspondre à votre environnement :
    - `chemin_liste_mots_de_passe` : Chemin vers le fichier contenant la liste des mots de passe.
    - `temp` : Répertoire temporaire pour stocker les fichiers uploadés.

## Utilisation

1. Placez votre fichier de liste de mots de passe à l'emplacement spécifié dans `chemin_liste_mots_de_passe`.

2. Exécutez l'application Flask :
    ```bash
    python app.py
    ```

3. Ouvrez un navigateur et accédez à `http://127.0.0.1:5000/`.

### Décrypter un fichier ZIP

1. Allez à `http://127.0.0.1:5000/zip.html`.
2. Uploadez le fichier ZIP que vous souhaitez déchiffrer.
3. L'application tentera de trouver le mot de passe en utilisant la liste de mots de passe fournie.

### Décrypter un fichier PDF

1. Allez à `http://127.0.0.1:5000/pdf.html`.
2. Uploadez le fichier PDF que vous souhaitez déchiffrer.
3. L'application tentera de trouver le mot de passe en utilisant la liste de mots de passe fournie.

## Structure du Code

- `app.py` : Contient le code principal de l'application Flask et les fonctions de brute force pour les fichiers ZIP et PDF.
- `templates/` : Contient les fichiers HTML pour les pages web (`index.html`, `zip.html`, `pdf.html`).
- `staic/` : Contient un dossier CSS avce le fichier ( `Page.css` ) pour les page HTML et le dossier JS avec le fichier ( `script.js` ) pour le Drag and Drop

## Notes

- Assurez-vous que le répertoire temporaire (`temp`) existe et que vous avez les permissions nécessaires pour y écrire.
- L'attaque par force brute peut prendre beaucoup de temps en fonction de la longueur de la liste de mots de passe et de la complexité du mot de passe du fichier cible.


