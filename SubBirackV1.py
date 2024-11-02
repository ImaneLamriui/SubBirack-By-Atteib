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
    print(f"Scanning for subdomains of {domain}...")
# Exécuter Sublist3r via subprocess
    result = subprocess.run(['sublist3r', '-d', domain], capture_output=True, text=True)
    return [sub for sub in result.stdout.splitlines() if domain in sub]
# Fonction pour résoudre les DNS
def mata(subdomains):
    active = []
    for sub in subdomains:
        try:
            response = requests.head(f"http://{sub}", timeout=5)
            if response.status_code < 400:
                birack(f"Active subdomain: {sub}")
                active.append(sub)
        except requests.exceptions.RequestException:
            continue
    return active

def resolve_dns(subdomain):
    try:
        for ip in dns.resolver.resolve(subdomain, 'A'):
            birack(f"{subdomain} resolves to {ip}")
    except dns.resolver.NXDOMAIN:
        birack(f"{subdomain} does not exist.")
    except (dns.resolver.NoAnswer, dns.resolver.Timeout):
        birack(f"No DNS answer for {subdomain}.")
    except Exception as e:
        birack(f"Error resolving {subdomain}: {e}")

# Vérifier si le domaine est passé en argument
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./SubBirack.py <domain>")
        sys.exit(1)
# Passer le domaine cible en argument pour obtenir les sous-domaines avec SubBrute
    domain = sys.argv[1]
    subdomains = birackinit(domain)

# Afficher les sous-domaines trouvés
    birack(f"Subdomains found for {domain}:")
    for sub in subdomains:
        birack(sub)

# Vérifier quels sous-domaines sont actifs
    active_subdomains = mata(subdomains)

# Résoudre les DNS des sous-domaines actifs
    birack("\n⭐⭐⭐⭐⭐⭐ DNS Resolutions ⭐⭐⭐⭐⭐⭐:")
    for sub in active_subdomains:
        resolve_dns(sub)

    birack("=== SubBirack scan completed ===")
