# Análise de Linguagens dos Repositórios do GitHub

Este projeto utiliza Python com as bibliotecas `requests` e `pandas` para obter e analisar a lista de linguagens de programação usadas nos repositórios de grandes empresas no GitHub.

## Funcionalidades

- Obtém dados dos repositórios do GitHub usando sua API.
- Analisa as linguagens de programação utilizadas nesses repositórios.
- Fornece um resumo do uso das linguagens nos repositórios.

## Instalação

1. Clone o repositório:
  ```bash
  git clone https://github.com/gabrielcsg/py-corporate-langs-etl.git
  cd py-corporate-langs-etl
  ```

2. Crie um ambiente virtual e ative-o:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

3. Instale os pacotes necessários:
  ```bash
  pip install -r requirements.txt
  ```

4. Crie um arquivo .env no diretório raiz e adicione sua chave de API do GitHub, nome de usuário e versão do GitHub:
  ```bash
  GITHUB_API_KEY=sua_chave_de_api_do_github
  GITHUB_USERNAME=seu_nome_de_usuario_no_github
  GITHUB_VERSION=sua_versao_do_github
  ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.