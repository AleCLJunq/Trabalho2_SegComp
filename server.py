#!/usr/bin/env python3
"""
Servidor HTTPS que utiliza TLS para comunicação segura.
O servidor usa um certificado autoassinado (server.pem).
"""

import ssl
import http.server
import logging
import sys

def create_https_server(server_address=('localhost', 443), certfile='./server.pem'):
    """
    Cria e configura um servidor HTTPS.
    
    Args:
        server_address (tuple): Endereço e porta do servidor.
        certfile (str): Caminho para o certificado e chave privada.
    
    Returns:
        http.server.HTTPServer: Instância do servidor HTTPS configurado.
    """
    handler = http.server.SimpleHTTPRequestHandler
    try:
        httpd = http.server.HTTPServer(server_address, handler)
    except Exception as e:
        logging.error(f"Erro ao criar o servidor HTTP: {e}")
        sys.exit(1)

    # Configura o contexto SSL para TLS seguro
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    try:
        context.load_cert_chain(certfile=certfile)
    except Exception as e:
        logging.error(f"Erro ao carregar o certificado: {e}")
        sys.exit(1)

    # Envolve o socket com o contexto SSL
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    return httpd

def main():
    logging.basicConfig(level=logging.INFO)
    server_address = ('localhost', 443)
    certfile = './server.pem'
    logging.info("Inicializando o servidor HTTPS...")
    server = create_https_server(server_address, certfile)
    logging.info(f"Servidor rodando em https://{server_address[0]}:{server_address[1]}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Encerramento solicitado pelo usuário.")
    finally:
        server.server_close()
        logging.info("Servidor fechado.")

if __name__ == '__main__':
    main()
