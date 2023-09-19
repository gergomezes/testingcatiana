#!/usr/bin/env python3
import subprocess

# Zeptat se uživatele na URL
target_url = input("Zadejte cílovou URL: ").strip()

# Název souboru pro uložení výstupu
output_file = "wpscan_output.txt"

# Funkce pro spuštění nástroje WPScan s sudo a zápisem do souboru
def run_wpscan(target):
    with open(output_file, "w") as output:
        result = subprocess.run(["sudo", "wpscan", "--url", target], stdout=output, stderr=subprocess.PIPE, text=True)
    return result.stderr

# Spustit WPScan a uložit výstup do souboru
wpscan_error = run_wpscan(target_url)

# Výstup odeslán zpět na webové rozhraní
print("Content-Type: text/html")
print()
print("<html>")
print("<head><title>WPScan Results</title></head>")
print("<body>")
print("<h1>WPScan Results</h1>")
print("<p>Výstup WPScan byl uložen do souboru: {}</p>".format(output_file))
print("</body>")
print("</html>")
