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
def show_results(data):
    print(data)

# Fonction pour exécuter SubBirack et obtenir des sous-domaines
def get_subdomains(domain):
    print(f"SubBirack is scanning for subdomains of {domain}...")
    
    # Exécuter Sublist3r via subprocess
    result = subprocess.run(['sublist3r', '-d', domain], capture_output=True, text=True)
    
    subdomains = result.stdout.splitlines()
    return [subdomain for subdomain in subdomains if domain in subdomain]

# Fonction pour vérifier si les sous-domaines sont actifs (renommée en check_subdomains)
def check_subdomains(subdomains):
    active_subdomains = []
    for subdomain in subdomains:
        try:
            # Faire une requête HEAD pour tester la réponse HTTP
            response = requests.head(f"http://{subdomain}", timeout=5)
            if response.status_code < 400:
                show_results(f"Active subdomain found: {subdomain}")
                active_subdomains.append(subdomain)
        except requests.exceptions.RequestException:
            continue
    return active_subdomains

# Fonction pour résoudre les DNS
def resolve_dns(subdomain):
    try:
        result = dns.resolver.resolve(subdomain, 'A')
        for ipval in result:
            show_results(f"{subdomain} resolves to {ipval.to_text()}")
    except dns.resolver.NXDOMAIN:
        show_results(f"{subdomain} does not exist.")
    except dns.resolver.NoAnswer:
        show_results(f"No DNS answer for {subdomain}.")
    except dns.resolver.Timeout:
        show_results(f"Timeout resolving {subdomain}.")
    except Exception as e:
        show_results(f"Error resolving {subdomain}: {e}")

if __name__ == "__main__":
    # Vérifier si le domaine est passé en argument
    if len(sys.argv) < 2:
        print("Usage: ./SubBirack.py <domain>")
        sys.exit(1)

    # Domaine cible passé en argument
    domain = sys.argv[1]

    # Étape 1 : Obtenir la liste des sous-domaines avec SubBirack
    subdomains = get_subdomains(domain)

    # Afficher les sous-domaines trouvés
    show_results(f"????? Subdomains found by SubBirack for {domain} ?????")
    for subdomain in subdomains:
        show_results(subdomain)

    # Étape 2 : Vérifier quels sous-domaines sont actifs avec SubBirack (check_subdomains)
    active_subdomains = check_subdomains(subdomains)

    # Étape 3 : Résoudre les DNS des sous-domaines actifs
    show_results("\n????? DNS Resolutions ?????")
    for subdomain in active_subdomains:
        resolve_dns(subdomain)

    show_results("=== SubBirack scan completed ===")
