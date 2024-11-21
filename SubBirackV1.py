#!/usr/bin/env python3
import subprocess
import requests
import dns.resolver
import sys

# En-tête du script
print("""
##########################################################
#####  Script: SubBirack.py
#####  Description: Ce script identifie les sous-domaines
¦¦¦¦¦¦¦ ¦¦    ¦¦ ¦¦¦¦¦¦  ¦¦ ¦¦¦¦¦¦   ¦¦¦¦¦   ¦¦¦¦¦¦ ¦¦   ¦¦ 
¦¦      ¦¦    ¦¦ ¦¦   ¦¦ ¦¦ ¦¦   ¦¦ ¦¦   ¦¦ ¦¦      ¦¦  ¦¦  
¦¦¦¦¦¦¦ ¦¦    ¦¦ ¦¦¦¦¦¦  ¦¦ ¦¦¦¦¦¦  ¦¦¦¦¦¦¦ ¦¦      ¦¦¦¦¦   
     ¦¦ ¦¦    ¦¦ ¦¦   ¦¦ ¦¦ ¦¦   ¦¦ ¦¦   ¦¦ ¦¦      ¦¦  ¦¦  
¦¦¦¦¦¦¦  ¦¦¦¦¦¦  ¦¦¦¦¦¦  ¦¦ ¦¦   ¦¦ ¦¦   ¦¦  ¦¦¦¦¦¦ ¦¦   ¦¦          
###########################################################
""")

# Fonction pour afficher les résultats
def birack(data):
    print(data)

# Fonction pour exécuter SubBirack et obtenir des sous-domaines
def birackinit(domain):
    print(f"SubBirack is scanning for subdomains of {domain}...")
    
    # Exécuter Sublist3r via subprocess
    result = subprocess.run(['sublist3r', '-d', domain], capture_output=True, text=True)
    
    subdomains = result.stdout.splitlines()
    return [subdomain for subdomain in subdomains if domain in subdomain]

# Fonction pour vérifier si les sous-domaines sont actifs
def mata(subdomains):
    active_subdomains = []
    for subdomain in subdomains:
        try:
            # Faire une requête HEAD pour tester la réponse HTTP
            response = requests.head(f"http://{subdomain}", timeout=5)
            if response.status_code < 400:
                birack(f"Active subdomain found: {subdomain}")
                active_subdomains.append(subdomain)
        except requests.exceptions.RequestException:
            continue
    return active_subdomains

# Fonction pour résoudre les DNS
def resolve_dns(subdomain):
    try:
        result = dns.resolver.resolve(subdomain, 'A')
        for ipval in result:
            birack(f"{subdomain} resolves to {ipval.to_text()}")
    except dns.resolver.NXDOMAIN:
        birack(f"{subdomain} does not exist.")
    except dns.resolver.NoAnswer:
        birack(f"No DNS answer for {subdomain}.")
    except dns.resolver.Timeout:
        birack(f"Timeout resolving {subdomain}.")
    except Exception as e:
        birack(f"Error resolving {subdomain}: {e}")

if __name__ == "__main__":
    # Vérifier si le domaine est passé en argument
    if len(sys.argv) < 2:
        print("Usage: ./SubBirack.py <domain>")
        sys.exit(1)

    # Domaine cible passé en argument
    domain = sys.argv[1]

    # Étape 1 : Obtenir la liste des sous-domaines avec SubBirack
    subdomains = birackinit(domain)

    # Afficher les sous-domaines trouvés
    birack(f" Subdomains found by SubBirack for {domain} ")
    for subdomain in subdomains:
        birack(subdomain)

    # Étape 2 : Vérifier quels sous-domaines sont actifs
    active_subdomains = mata(subdomains)

    # Étape 3 : Résoudre les DNS des sous-domaines actifs
    birack("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐ DNS Resolutions ⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    for subdomain in active_subdomains:
        resolve_dns(subdomain)

    birack("=== SubBirack scan completed ===")
