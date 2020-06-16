# Como usar:

Selecione a pasta baixada em seu terminal:

```bash
cd caminho_da_pasta
```

em que caminho_da_pasta é o caminho do diretório que a pasta se encontra.

Crie seu ambiente virtual:

```bash
seu_comando_de_python -m venv nome_ambiente_virtual
```

em que seu_comando_de_python é o comando utilizado para usar o python e nome_ambiente_virtual é o nome do seu ambiente virtual.

Ative seu ambiente virtual:

```bash
source nome_ambiente_virtual/bin/activate
```

instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

Inicie o servidor:

```bash
seu_comando_de_python manage.py runserver --insecure
```

Isso irá abrir uma conexão com a porta 8000 (--insecure irá carregar o CSS e JavaScript). Basta clicar ou copiar o endereço no seu
navegador para abrir o site. Caso tenha algo rodando nessa porta, pode usar outra. Basta, no terminal, usar o comando:

```bash
seu_comando_de_python manage.py runserver numero_porta --insecure
```

em que numero_porta é a porta que deseja utilizar.

Para desligar o servidor:

```bash
CTRL+C
```

Para desligar o ambiente virtual:

```bash
deactivate
```
