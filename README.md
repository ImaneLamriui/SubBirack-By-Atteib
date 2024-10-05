# SubBirack

## ✨ Fonctionnalités

SubBirack.py est un script avancé conçu pour identifier et analyser en profondeur les sous-domaines d'un domaine cible. Il intègre plusieurs fonctionnalités, notamment :

●  **Recherche de sous-domaines** : Utilisation de l'outil Sublist3r pour scanner et lister les sous-domaines d'un domaine.  
●  **Vérification des sous-domaines actifs** : Validation des sous-domaines via des requêtes HTTP pour détecter ceux qui sont actifs.  
●  **Résolution DNS** : Vérification de la résolution DNS des sous-domaines actifs pour obtenir leurs adresses IP associées.

## 🛠️ Utilisation :

    Cloner le dépôt : git clone https://github.com/votre-utilisateur/SubBirack.git

    cd SubBirack

➕ **Installer les dépendances** : 
Assurez-vous d'avoir un environnement virtuel activé et exécutez :

    source venv/bin/activate
    pip install -r requirements.txt

**Exécuter le script** : 
Utilisez la commande suivante pour analyser un domaine :

    ./SubBirack.py <domaine>

**Exemple** :

    ./SubBirack.py example.com

## ⚙️ Exigences :

Python 3.x : Assurez-vous que Python 3 est installé.
Sublist3r : Cet outil est utilisé pour la recherche de sous-domaines. 

Installez-le via pip :

    pip install sublist3r
    
Modules requis :

    requests
    dns.resolver
    subprocess
    
Ces modules peuvent être installés via le fichier requirements.txt fourni.

## 💡 Remarques :

**Environnement virtuel** : 
L'utilisation d'un environnement virtuel est recommandée pour isoler les dépendances. Activez-le avec :

    source venv/bin/activate

**Sublist3r** : Si vous rencontrez des problèmes lors de l'installation, utilisez pipx pour l'installer dans un environnement isolé :

    pipx install sublist3r

**Ajout au PATH** : Si nécessaire, ajoutez Sublist3r à votre PATH :

    export PATH=$PATH:/root/.local/bin

## ⚠️ Disclaimer :

SubBirack.py est un outil puissant qui doit être utilisé de manière légale et éthique. Il est strictement réservé à :  
●     Des tests d'intrusion autorisés avec l'accord explicite des propriétaires des systèmes concernés.  
●     Des analyses de sécurité dans le cadre de missions légales avec consentement.  
●     Un usage personnel en laboratoire pour des tests sur des environnements contrôlés. 

L'utilisation de cet outil pour analyser ou compromettre des systèmes sans autorisation est illégale et pourrait entraîner des sanctions civiles et pénales. L'auteur décline toute responsabilité pour tout usage inapproprié de cet outil.


## 🎥 Démo :

Pour voir une démonstration du script en action, voici une capture d'écran de l'exécution d'une analyse : 
