#!/usr/bin/env python3
"""
Cliente HTTPS que realiza uma requisição ao servidor verificando o certificado TLS.
"""

import requests
import logging

# Caminho para o certificado do servidor (salvo após a geração)
CERT_PATH = './server-cert.pem'

def main():
    logging.basicConfig(level=logging.INFO)
    url = 'https://localhost:443'
    logging.info(f"Realizando requisição HTTPS para {url}")
    try:
        # Agora a verificação TLS é ativada usando o certificado do servidor
        response = requests.get(url, verify=CERT_PATH)
        logging.info(f"Resposta do servidor: {response.status_code}")
        print(response.text)
    except requests.exceptions.SSLError as e:
        logging.error(f"Erro SSL na conexão: {e}")
    except Exception as e:
        logging.error(f"Erro na requisição: {e}")

if __name__ == '__main__':
    main()
