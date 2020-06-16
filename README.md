# Iniciando o Site

Usei o  [Python 3.8](https://www.python.org/downloads/release/python-380/)  para o projeto. Como padrão, nos comandos usarei `python3.8` como meu comando para utilizar o Python, mas você deve usar o comando para Python da sua máquina (substituindo nos locais que estiver `python3.8`).

Selecione a pasta baixada em seu terminal:

```bash
cd caminho_da_pasta
```

em que caminho_da_pasta é o caminho do diretório que a pasta se encontra.

Crie seu ambiente virtual:

```bash
python3.8 -m venv meu_ambiente_virtual
```

Aqui, chamei o ambiente virtual de `meu_ambiente_virtual`. Caso queira nomear de outra maneira, basta colocar o nome desejado no lugar de `meu_ambiente_virtual` (assim como nos comandos subsequentes).

Ative seu ambiente virtual:

```bash
source meu_ambiente_virtual/bin/activate
```

instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

Inicie o servidor:

```bash
python3.8 manage.py runserver
```

Isso irá abrir uma conexão com a porta 8000. Basta clicar em `http://127.0.0.1:8000/` ou copiar o endereço no seu navegador para abrir o site. Caso tenha algo rodando nessa porta, pode usar outra. Basta, no terminal, usar o comando:

```bash
python3.8 manage.py runserver numero_porta
```

em que `numero_porta` é a porta que deseja utilizar, como, por exemplo, `8888`.

Para desligar o servidor:

```bash
CTRL+C
```

Para desligar o ambiente virtual:

```bash
deactivate
```

# Usando o Site

Com o servidor rodando, podemos utilizar as diversas funcionalidades do Site.

## Tabela de Rankings

Na **Home** do Site é exibido o **ranking de confiabilidade** das empreasas adicionadas ao **Banco de Dados** do Site. As empresas são mostradas em ordem decrescente de confiabilidade, isto é, da mais confiável, para a menos confiável. O índice de confiabilidade de uma empresa aparece vermelho, se estiver abaixo de 50%; aparece preto se estiver entre 50% e 75%; e aparece verde se estiver acima de 75%. 

## Empresas

Clicando no nome da empresa na tabela, é exibido seu nome, o índice de confiabilidade e a posição no ranking de confiabilidade. Caso a empresa tenha um logo e uma descrição, esses também serão exibidos.

## Sobre o Site

No **Sobre** do Site são exibidas inúmeras informações sobre o Site, como quais campos as empresas possuem no Banco de Dados e como são calculados os índice de confiabilidade das empresas.

## Login

No **Login** o usuário pode fazer login em sua conta (caso já esteja cadastrado) para ter acesso a área administrativa do Site.

## Cadastro

No **Cadastro** o usuário pode se cadastrar no Site, bastando informar um nome de usuário (diferentes dos já cadastrados no Site) e informando uma senha (o qual deve ser repetida).

## Área Administrativa

Na **Área Administrativa** o usuário pode adicionar uma empresa ao Banco de Dados ou enviar finanças de uma empresa já adicionada.

## Adicionar Empresa

Para adicionar uma empresa, basta digitar o nome da empresa (ID e índice são criados automaticamente) e clicar em **Adicionar Empresa**. Ainda são oferecidos os campos de logo (para enviar um arquivo de imagem do logo da empresa) e de descrição (para digitar uma breve descrição da empresa) de forma opcional para o usuário.

## Enviar Finanças

Para enviar finanças, o usuário deve selecionar uma das empresas adicionadas ao Banco de Dados pelo seu ID e enviar um arquivo `.json` com as chaves **"nf"** e **"d"**, referentes às notas fiscais e débitos da empresa, respectivamente, com valores iguais a quantidade das mesmas. Após o envio, o índice da empresa é recalculado e a tabela de rankings na Home do Site é atualizada (assim como a posição das empresas no ranking).


