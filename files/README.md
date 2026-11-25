# AURUM — site vitrine

Site vitrine français, avec une démonstration autonome exécutée dans le navigateur. Le serveur Python ne sert que les fichiers publics du site.

## Lancement local

Depuis ce dossier, avec Python 3 :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Ouvrir http://localhost:8000. Sous Windows, activer l'environnement avec `.venv\Scripts\activate` au lieu de `source .venv/bin/activate`.

## Déployer comme Web Service sur Render, sans Blueprint

1. Déposer tous les fichiers de ce dossier à la racine d'un dépôt Git, puis pousser la branche voulue.
2. Dans Render, créer un **Web Service**, connecter le dépôt et sélectionner cette branche.
3. Choisir le langage **Python**, puis saisir :
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Activer **Auto-Deploy** pour les commits de la branche choisie dans les paramètres du service. Render déploiera ensuite les changements poussés sur cette branche.
5. Lancer le premier déploiement et vérifier l'URL fournie par Render.

Le serveur écoute sur le port fourni par Render. Aucun `render.yaml` ni Blueprint n'est utilisé. Le dépôt et le service doivent être reliés dans le compte du propriétaire : les fichiers seuls ne créent pas le service et n'activent pas l'auto-déploiement à distance. Les modalités et les éventuels frais dépendent du forfait Render choisi.

## Fonctionnel

- Navigation responsive, menu mobile, FAQ, fenêtres fermables et liens vers les sections.
- Démonstration autonome : trois projets et clients fictifs, compte rendu d'exemple, création et validation de tâches ou réserves, chronomètre local, agenda fictif et réinitialisation.
- Les tâches de démonstration sont enregistrées dans le stockage local du navigateur quand il est disponible. Le chronomètre est temporaire et ne survit pas à un rechargement. Aucun compte ni serveur supplémentaire n'est nécessaire à la démo.
- La capture de l'application est celle fournie par le créateur, avec son logo retouché pour refléter la nouvelle identité ; la photographie architecturale est une illustration générée.

## Simulé

Les projets, clients, rendez-vous, comptes rendus, tâches et durées de la démonstration sont fictifs. L'aperçu est indépendant de l'application réelle et ne lui transmet aucune donnée ; aucun e-mail n'est envoyé. L'agenda est en lecture seule et ne se synchronise pas. Les fonctions décrites sur le site ne sont pas toutes reproduites dans la démo.

## Avant publication

- Vérifier et compléter les mentions légales, la politique de confidentialité et les coordonnées de contact ; les boutons affichent pour l'instant un message explicite.
- Vérifier les fonctionnalités, leurs conditions de disponibilité et la conformité des relevés de facturation avec le responsable du produit.
- Configurer si nécessaire le lien officiel dans `config.js` (le lien fourni par le créateur est utilisé par défaut). L'autre lien fourni est https://comte-rendu-mod.onrender.com.
- Compléter les métadonnées de partage avec l'URL publique définitive et une image sociale appropriée.
- Vérifier la politique de confidentialité relative aux polices Google et au stockage local, ou héberger les polices localement.
- Configurer le serveur de l'application réelle pour les e-mails et les automatismes si souhaités ; le présent site ne les configure pas.
