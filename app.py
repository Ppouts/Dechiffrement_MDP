import os  
import pyzipper 
import pikepdf  
from flask import Flask, render_template, request 

app = Flask(__name__)  

chemin_liste_mots_de_passe = r"chemin\vers\liste\de\mots\de\passe"  # Chemin du fichier contenant la liste des mots de passe
temp_dir = r"chemin\vers\repertoir\temp"  # Répertoire temporaire pour stocker les fichiers uploadés

if not os.path.exists(temp_dir): 
    os.makedirs(temp_dir)  

def brute_force_zip(chemin_zip, chemin_liste_mots_de_passe):  
    try:
        with open(chemin_liste_mots_de_passe, 'r', encoding='utf-8') as wordlist: 
            for mot_de_passe in wordlist:  
                mot_de_passe = mot_de_passe.strip() 
                try:
                    with pyzipper.AESZipFile(chemin_zip) as zf:  
                        zf.extractall(pwd=mot_de_passe.encode())  
                        return mot_de_passe  
                except pyzipper.BadZipFile: 
                    print("Fichier ZIP invalide") 
                    return None  
                except Exception as e:  
                    print(f"Erreur inconnue : {e}")  
                    continue  
        print("Mot de passe non trouvé dans la liste.")  
        return None  
    except Exception as e:  
        print(f"Erreur lors de la brute-force ZIP : {e}")  
        return None 
    
def brute_force_pdf(chemin_pdf, chemin_liste_mots_de_passe):
    try:
        with open(chemin_liste_mots_de_passe, 'r', encoding='utf-8') as wordlist:  
            for mot_de_passe in wordlist:  
                mot_de_passe = mot_de_passe.strip()  
                try:
                    with pikepdf.open(chemin_pdf, password=mot_de_passe) as pdf: 
                        print(f"Mot de passe trouvé : {mot_de_passe}")  
                        return mot_de_passe 
                except pikepdf.PasswordError:
                    continue 
        print("Mot de passe non trouvé dans la liste.")
        return None  
    except Exception as e:
        print(f"Erreur lors de l'utilisation de pikepdf : {e}")  
        return None  

# def determine_zip_encryption_type(chemin_zip):
#     try:
#         with pyzipper.AESZipFile(chemin_zip) as zf:
#             if zf.fp is not None:
#                 try:
#                     zf.extract(zf.namelist()[0], pwd=b'test')
#                 except RuntimeError as e:
#                     if "File is encrypted" in str(e):
#                         print("Chiffrement AES détecté")
#                         return "AES"
#                     else:
#                         print(f"Erreur de Runtime détectée pour AES: {e}")
#                 except Exception as e:
#                     print(f"Exception générale pour AES: {e}")
#     except pyzipper.BadZipFile:
#         print("Fichier ZIP invalide")
#         return "Invalid ZIP file"
#     except Exception as e:
#         print(f"Exception générale pour AESZipFile: {e}")

#     try:
#         with pyzipper.ZipFile(chemin_zip) as zf:
#             if zf.fp is not None:
#                 try:
#                     zf.extract(zf.namelist()[0], pwd=b'test')
#                 except RuntimeError as e:
#                     if "File is encrypted" in str(e):
#                         print("Chiffrement ZipCrypto détecté")
#                         return "ZipCrypto"
#                     else:
#                         print(f"Erreur de Runtime détectée pour ZipCrypto: {e}")
#                 except Exception as e:
#                     print(f"Exception générale pour ZipCrypto: {e}")
#     except pyzipper.BadZipFile:
#         print("Fichier ZIP invalide")
#         return "Invalid ZIP file"
#     except Exception as e:
#         print(f"Exception générale pour ZipFile: {e}")

#     print("Chiffrement inconnu")
#     return "Unknown encryption"


# def determine_pdf_encryption_type(chemin_pdf):
#     try:
#         with pikepdf.open(chemin_pdf) as pdf:
#             if pdf.is_encrypted:
#                 return pdf.encryption['/Filter']
#     except pikepdf.PasswordError:
#         pass  # PDF chiffré, mais mot de passe nécessaire pour obtenir des détails
#     except Exception as e:
#         return f"Erreur lors de la détermination du chiffrement PDF : {e}"

#     return "Unknown encryption"

@app.route('/')  
def index():
    return render_template('index.html')  

@app.route('/zip.html', methods=['GET', 'POST'])  
def zip():
    if request.method == 'POST': 
        if 'zip_file' not in request.files: 
            return render_template('zip.html') 

        fichier_zip = request.files['zip_file']  
        if fichier_zip.filename == '':  
            return render_template('zip.html')  

        chemin_fichier_zip = os.path.join(temp_dir, fichier_zip.filename)  
        fichier_zip.save(chemin_fichier_zip) 
        print(f"Fichier ZIP sauvegardé à : {chemin_fichier_zip}")  

        mot_de_passe = brute_force_zip(chemin_fichier_zip, chemin_liste_mots_de_passe)

        if mot_de_passe: 
            print(f"Mot de passe trouvé : {mot_de_passe}")  
            return render_template('zip.html', mot_de_passe=mot_de_passe)  
        else:
            print("Mot de passe non trouvé")
            return render_template('zip.html', mot_de_passe="Mot de passe non trouvé")  

    return render_template('zip.html')  

@app.route('/pdf.html', methods=['GET', 'POST'])
def pdf():
    if request.method == 'POST': 
        if 'pdf_file' not in request.files:
            return render_template('pdf.html') 

        fichier_pdf = request.files['pdf_file']  
        if fichier_pdf.filename == '':
            return render_template('pdf.html')  

        chemin_fichier_pdf = os.path.join(temp_dir, fichier_pdf.filename) 
        fichier_pdf.save(chemin_fichier_pdf)  
        print(f"Fichier PDF sauvegardé à : {chemin_fichier_pdf}")  

        mot_de_passe = brute_force_pdf(chemin_fichier_pdf, chemin_liste_mots_de_passe)

        if mot_de_passe: 
            print(f"Mot de passe trouvé : {mot_de_passe}")  
            return render_template('pdf.html', mot_de_passe=mot_de_passe)  
        else:
            print("Mot de passe non trouvé")
            return render_template('pdf.html', mot_de_passe="Mot de passe non trouvé")

    return render_template('pdf.html') 

if __name__ == "__main__":  
    app.run(debug=True)
