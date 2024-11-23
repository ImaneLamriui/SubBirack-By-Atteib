# SubBirack

> [!Note]
> SubBirack.py est un script conçu pour identifier et analyser en profondeur les sous-domaines d'un domaine cible. 
> 
> ## ✨ Fonctionnalités
> Il intègre plusieurs fonctionnalités, notamment :
* **Recherche de sous-domaines** : Utilisation de l'outil Sublist3r pour scanner et lister les sous-domaines d'un domaine.  
* **Vérification des sous-domaines actifs** : Validation des sous-domaines via des requêtes HTTP pour détecter ceux qui sont actifs.  
* **Résolution DNS** : Vérification de la résolution DNS des sous-domaines actifs pour obtenir leurs adresses IP associées.


⚙️ **Installer les dépendances** : 

### Prérequis
- Python 3.7 ou supérieur
- `pip` installé
- Git installé sur votre machine


### 📋 Étapes d'installation

**Clonez le dépôt Git** :

    git clone https://github.com/BirackInit/SubBirack.git
    cd SubBirack
    
**Installer les modules nécessaires en utilisant le fichier requirements.txt fourni**.
    
    pip install -r requirements.txt

**Rendez le script exécutable (optionnel mais recommandé) :**

    chmod +x SubBirack.py

## 🛠️ Utilisation :

**Utilisez la commande suivante pour analyser un domaine cible :**

    python3 SubBirack.py example.com

**Exemple** :

    ./SubBirack.py example.com



## ⚠️ Disclaimer :

> [!Important]
>
> SubBirack.py est un outil puissant qui doit être utilisé de manière légale et éthique. Il est strictement réservé à :  
* Des tests d'intrusion autorisés avec l'accord explicite des propriétaires des systèmes concernés.
* Des analyses de sécurité dans le cadre de missions légales avec consentement.
* Un usage personnel en laboratoire pour des tests sur des environnements contrôlés. 
>
> L'utilisation de cet outil pour analyser ou compromettre des systèmes sans autorisation est illégale et pourrait entraîner des sanctions civiles et pénales. L'auteur décline toute responsabilité pour tout usage inapproprié de cet outil.



## 🎥 Démo : 
* Pour voir une démonstration du script en action, voici une capture d'écran de l'exécution d'une analyse :



![image](https://github.com/user-attachments/assets/a1818389-7c81-4013-9c92-08cfb9692e65)


