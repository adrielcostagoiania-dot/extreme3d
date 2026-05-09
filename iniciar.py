import http.server
import socketserver
import webbrowser
import threading
import time
import os
import sys

PORT = 8080
URL = f"http://localhost:{PORT}/print3d-manager.html"

# Muda para a pasta do script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print()
print("  ==========================================")
print("        EXTREME 3D Manager")
print("  ==========================================")
print()

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Silencia logs desnecessarios

def abrir_navegador():
    time.sleep(1.5)  # Aguarda servidor subir
    print(f"  Abrindo: {URL}")
    print()
    webbrowser.open(URL)

# Abre navegador em thread separada
t = threading.Thread(target=abrir_navegador)
t.daemon = True
t.start()

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"  Servidor rodando na porta {PORT}")
        print(f"  Acesse: {URL}")
        print()
        print("  NAO feche esta janela enquanto usar o sistema.")
        print("  Para encerrar: feche esta janela ou Ctrl+C")
        print("  ==========================================")
        print()
        httpd.serve_forever()
except OSError:
    # Porta ja em uso — apenas abre o navegador
    print(f"  Servidor ja rodando! Abrindo navegador...")
    webbrowser.open(URL)
except KeyboardInterrupt:
    print()
    print("  Sistema encerrado.")
