#!/usr/bin/env python3
import subprocess

# Zeptat se uživatele na URL
target_url = input("Zadejte cílovou URL: ").strip()

# Funkce pro spuštění nástroje WPScan
def run_wpscan(target):
    result = subprocess.run(["wpscan", "--url", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

# Výstupy z WPScan
wpscan_output, wpscan_error = run_wpscan(target_url)

# Výstup odeslán zpět na webové rozhraní
print("Content-Type: text/html")
print()
print("<html>")
print("<head><title>WPScan Results</title></head>")
print("<body>")
print("<h1>WPScan Results</h1>")
print("<pre>")
print(wpscan_output)
print("</pre>")
print("</body>")
print("</html>")
