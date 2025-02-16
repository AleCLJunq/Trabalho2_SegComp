# Projeto HTTPS – CIC0201 Segurança Computacional 2024/2

## Descrição

Este projeto demonstra a implementação de um servidor e um cliente HTTPS para estabelecer uma comunicação segura via TLS. O objetivo é aplicar conceitos de criptografia, autenticação e integridade dos dados por meio da configuração de certificados, garantindo que o cliente valide corretamente o certificado do servidor.

O projeto foi desenvolvido para a disciplina CIC0201 - Segurança Computacional 2024/2 e abrange:

- Configuração de um servidor HTTPS utilizando o módulo `http.server` e a biblioteca `ssl` do Python.
- Implementação de um cliente HTTPS que valida o certificado do servidor utilizando a biblioteca `requests`.
- Geração de certificados autoassinados com o campo Subject Alternative Name (SAN) configurado para "localhost", evitando o erro de "Hostname mismatch".

## Estrutura do Projeto

```
Projeto-HTTPS/
├── client.py            # Código do cliente HTTPS
├── server.py            # Código do servidor HTTPS
├── requirements.txt     # Dependências do projeto (biblioteca requests)
└── README.md            # Este arquivo de documentação
```

## Requisitos

- Python 3.x instalado.
- OpenSSL instalado para geração dos certificados.
- Biblioteca Python `requests` (disponível via pip).

## Instalação

1. **Clone ou Baixe o Projeto**\
   Faça o download dos arquivos do projeto e navegue até o diretório:

   ```bash
   cd Projeto-HTTPS
   ```

2. **Instale as Dependências**\
   Utilize o pip para instalar a biblioteca necessária:

   ```bash
   pip install -r requirements.txt
   ```

## Geração do Certificado TLS

Para que o cliente valide a comunicação segura, é necessário gerar um certificado TLS que contenha "localhost" no campo Subject Alternative Name (SAN). Siga os passos abaixo:

1. **Crie o Arquivo de Configuração OpenSSL**\
   Crie um arquivo chamado `openssl.cnf` com o seguinte conteúdo:

   ```ini
   [req]
   default_bits = 4096
   prompt = no
   default_md = sha256
   distinguished_name = req_distinguished_name
   x509_extensions = v3_req

   [req_distinguished_name]
   C = "Seu País"
   ST = "Seu Estado"
   L = "Sua cidade"
   O = MeuServidor
   CN = localhost

   [v3_req]
   subjectAltName = @alt_names

   [alt_names]
   DNS.1 = localhost
   IP.1 = 127.0.0.1
   ```

2. **Gere o Certificado e a Chave Privada**\
   Execute o comando abaixo para gerar um certificado autoassinado válido por 365 dias:

   ```bash
   openssl req -x509 -newkey rsa:4096 -keyout server-key.pem -out server-cert.pem -days 365 -nodes -config openssl.cnf
   ```

3. **Combine a Chave e o Certificado para o Servidor**\
   O servidor utilizará um arquivo único contendo a chave privada e o certificado:

   ```bash
   cat server-key.pem server-cert.pem > server.pem
   ```

## Execução do Projeto

### 1. Executando o Servidor HTTPS

Inicie o servidor com o comando:

```bash
python3 server.py
```

O servidor será iniciado em `https://localhost:443`, utilizando o arquivo `server.pem` para a comunicação segura.

### 2. Executando o Cliente HTTPS

Em outro terminal, execute o cliente:

```bash
python3 client.py
```

O cliente fará uma requisição HTTPS para o servidor, validando o certificado através do arquivo `server-cert.pem`. Se a configuração estiver correta, a resposta do servidor será exibida sem erros.

## Observações e Considerações de Segurança

- **Certificados Autoassinados:**\
  Este projeto utiliza certificados autoassinados, que são adequados para testes e desenvolvimento. Em ambiente de produção, recomenda-se utilizar certificados emitidos por uma autoridade certificadora confiável.

- **Verificação TLS:**\
  O cliente valida o certificado do servidor usando:

  ```python
  response = requests.get(url, verify='./server-cert.pem')
  ```

  Assim, a comunicação é segura e o erro de "Hostname mismatch" é evitado ao incluir "localhost" no campo SAN.

## Dependências e Bibliotecas Utilizadas

- **http.server:** Para a criação do servidor HTTP.
- **ssl:** Para configurar a camada de segurança TLS.
- **requests:** Para realizar requisições HTTP/HTTPS no cliente.
- **OpenSSL:** Para geração e manipulação dos certificados TLS.


## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

