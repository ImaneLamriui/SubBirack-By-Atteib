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

# Function to display results
def birack(data):
    print(data)

# Function to execute SubBirack and get subdomains
def birackinit(domain):
    print(f"SubBirack is scanning for subdomains of {domain}...")
    
    # Execute Sublist3r via subprocess
    result = subprocess.run(['sublist3r', '-d', domain], capture_output=True, text=True)
    
    subdomains = result.stdout.splitlines()
    return [subdomain for subdomain in subdomains if domain in subdomain]

# Function to check if subdomains are active
def mata(subdomains):
    active_subdomains = []
    for subdomain in subdomains:
        try:
            # Send a HEAD request to test HTTP response
            response = requests.head(f"http://{subdomain}", timeout=5)
            if response.status_code < 400:
                birack(f"Active subdomain found: {subdomain}")
                active_subdomains.append(subdomain)
        except requests.exceptions.RequestException:
            continue
    return active_subdomains

# Function to resolve DNS
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
    # Check if the domain is passed as an argument
    if len(sys.argv) < 2:
        print("Usage: ./SubBirack.py <domain>")
        sys.exit(1)

    # Target domain passed as an argument
    domain = sys.argv[1]

    # Searching for subdomains
    subdomains = birackinit(domain)

    # Message to start the scan
    birack(f" Subdomains found by SubBirack for {domain} ")
    for subdomain in subdomains:
        birack(subdomain)

    # Checking for active subdomains
    active_subdomains = mata(subdomains)

    # DNS Resolution
    birack("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐ DNS Resolutions ⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    for subdomain in active_subdomains:
        resolve_dns(subdomain)

    birack("=== SubBirack scan completed ===")
