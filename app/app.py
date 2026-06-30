from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import os
import bcrypt  # Importation pour le hachage sécurisé des mots de passe

app = Flask(__name__)
# Dans un vrai audit, cette clé devrait être dans os.environ pour ne pas être en clair
app.secret_key = os.environ.get('SECRET_KEY', 'techsecure_super_secret_key')

# Configuration via variables d'environnement (injectées par Docker)
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'rootpassword')
DB_NAME = os.environ.get('DB_NAME', 'techsecure_db')

def get_db_connection():
    """Établit une connexion sécurisée à la base de données MySQL."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset='utf8mb4'
    )

# 💡 EXEMPLE D'UTILISATION DE BCRYPT POUR TON RAPPORT D'AUDIT
def hacher_mot_de_passe(password_clair):
    """Exemple de fonction de hachage demandée par l'audit."""
    sel = bcrypt.gensalt()
    password_hache = bcrypt.hashpw(password_clair.encode('utf-8'), sel)
    return password_hache

# 1️⃣ PAGE D'ACCUEIL
@app.route('/')
def accueil():
    return render_template('accueil.html')

# 2️⃣ PAGE SERVICES
@app.route('/services')
def services():
    return render_template('services.html')

# 3️⃣ PAGE FILIALES (LISTE)
@app.route('/filiales')
def filiales():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, ville, adresse, responsable, employes, ip_reseau FROM filiales")
        liste_filiales = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('filiales.html', filiales=liste_filiales)
    except Exception as e:
        # Sécurisation : On n'affiche plus l'erreur brute à l'écran, on redirige proprement
        flash("Une erreur interne est survenue lors de l'accès aux filiales.", "error")
        return redirect(url_for('accueil'))

# 4️⃣ PAGE AJOUTER UNE FILIALE
@app.route('/ajouter-filiale', methods=['GET', 'POST'])
def ajouter_filiale():
    if request.method == 'POST':
        ville = request.form['ville']
        adresse = request.form['adresse']
        responsable = request.form['responsable']
        employes = request.form['employes']
        ip_reseau = request.form['ip_reseau']

        # Validation basique des champs (Sécurité applicative)
        if not ville or not adresse or not responsable:
            flash("Tous les champs obligatoires doivent être remplis !", "error")
            return redirect(url_for('ajouter_filiale'))

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Requête paramétrée sécurisée contre les injections SQL (Validé !)
            query = """
                INSERT INTO filiales (ville, adresse, responsable, employes, ip_reseau) 
                VALUES (%s, %s, %s, %s, %s)
            """
            valeurs = (ville, adresse, responsable, employes, ip_reseau)
            
            cursor.execute(query, valeurs)
            conn.commit()
            cursor.close()
            conn.close()
            
            flash("La filiale a été ajoutée avec succès !", "success")
            return redirect(url_for('filiales'))
        except Exception as e:
            flash("Impossible d'ajouter la filiale. Vérifiez les informations saisies.", "error")
            return redirect(url_for('ajouter_filiale'))

    return render_template('ajouter_filiale.html')

# 5️⃣ PAGE À PROPOS
@app.route('/apropos')
def apropos():
    return render_template('apropos.html')

# 6️⃣ PAGE CONTACT
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash("Votre message de contact a été envoyé avec succès !", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)