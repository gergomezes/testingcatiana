#!/usr/bin/env python3
import subprocess

# Zeptat se uživatele na URL
target_url = input("Zadejte cílovou URL: ").strip()

# Funkce pro spuštění nástroje Nmap
def run_nmap(target):
    result = subprocess.run(["nmap", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

# Funkce pro spuštění WPScan
def run_wpscan(target):
    result = subprocess.run(["wpscan", "--url", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

# Funkce pro spuštění Nikto
def run_nikto(target):
    result = subprocess.run(["nikto", "-h", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

# Výstupy z jednotlivých nástrojů
nmap_output, nmap_error = run_nmap(target_url)
wpscan_output, wpscan_error = run_wpscan(target_url)
nikto_output, nikto_error = run_nikto(target_url)

# Výstup odeslán zpět na webové rozhraní
print("Content-Type: text/html")
print()
print("<html>")
print("<head><title>Penetration Test Results</title></head>")
print("<body>")
print("<h1>Penetration Test Results</h1>")
print("<h2>Nmap Results:</h2>")
print("<pre>")
print(nmap_output)
print("</pre>")
print("<h2>WPScan Results:</h2>")
print("<pre>")
print(wpscan_output)
print("</pre>")
print("<h2>Nikto Results:</h2>")
print("<pre>")
print(nikto_output)
print("</pre>")
print("</body>")
print("</html>")
