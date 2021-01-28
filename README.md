# Desafio Bemol - AI Engineer Challenge

## O desafio consiste em:

* Uma análise do perfil do público de clientes da base de dados.
* Segmentar os perfis identificados com base em características úteis para o time de vendas e marketing.
* Fornecer os dados a partir de uma API utilizada para consultas.

## Foco deste processo:

Para apresentar um pouco do meu trabalho, seguirei os passos:

* **Insights**: Obter informações relevantes sobre a base de dados e dos clientes presentes na mesma. Gerar informação útil para o time de vendas e marketing que possam auxiliar nas estratégias de ambos os times.
* **Segmentação**: Separação entre tipos diferentes de clientes. Esta separação será realizada de forma ampla por falta de informação sobre as particularidades que os times de venda e marketing necessitam.
* **Exposição**: Formação e dispinibilização da API para acesso de dados de clientes baseados nos dados relevantes sobre os clientes e na segmentação desenvolvida.

## Organização do projeto

A organização dos arquivos do projeto se encontram da seguinte forma:

* `data`: Armazena arquivos intermediários, arquivos processados e arquivos necessários para a API. Subdivide-se em `data/bin`, onde são encontrados arquivos binários utilizados pela API, `data/raw`, onde estão os dados originais da base de dados e `data/processed`, pasta que armazena os dados durante e após o processo de preprocessamento.

* `docs`: Armazena documentos relacionados ao desafio. Também armazena documentos de metadados dos arquivos gerados no preprocessamento. É subdividido em `docs/md` e `docs/pdf` que armazenam arquivos no formato markdown e pdf respectivamente.

* `notebooks`: Armazena ambos notebooks de exploração de dados e do uso do modelo escolhido para segmentação.

* `src`: Armazena código fonte gerado para este projeto que não está incluso em notebooks. É subdividido em `src/api` onde estão da API desenvolvida e `src/scripts` que são scripts auxiliares para desenvolver alguma atividade específica.

## Como testar:

### Instalação:

O projeto é todo escrito em `Python` utilizando diversas bibliotecas de propósitos diferentes. O arquivo `requirements.txt` disponível na raiz do projeto deverá ser usado para instalar todas as dependências necessárias. Em alguns casos, utilizar o arquivo de requirements não funciona por não encontrar alguns pacotes (pip desatualizado, Ubuntu mais antigo, etc). Caso isso ocorra, segue o comando de instalação com as principais dependências que devem ser instaladas:

`pip install pandas sklearn seaborn flask requests`

Caso queira executar os notebooks existentes, também será necessária a instalação do pacote `jupyterlab` ou `jupyter`.

### Execução:

O projeto consiste em 2 núcleos distintos, os notebooks onde são apresentadas as análises e aplicação do modelo de machine learning e a API para extração dos dados da base de dados. Enquanto o uso de notebooks é mais ubíquo e de menor complexidade para a execução, existem alguns passos a serem tomados ao utilizar o núcleo da API do projeto.

Primeiramente, os comandos abaixo foram testados apenas em uma máquina com Ubuntu 20.04 e outra máquina com macOS 10.11, portanto, se algo descrito abaixo não funcionar corretamente, me contate para que eu possa adicionar os passos corretos aqui. Para a execução do servidor da API, devem ser executados os seguintes passos:

1. Definir uma variável de ambiente chamada `FLASK_APP` com a localização do arquivo `src/api.main.py`. Caso a tentativa de execução seja feita a partir da raiz do projeto, digitar o comando `export FLASK_APP=src/api.main.py` no terminal (Ubuntu ou macOS) deverá ser suficiente.

2. Executar comando `flask run` via terminal. Isso fará com que o flask (instalado anteriormente com pip) busque o arquivo definido na variável de ambiente e inicie o servidor da API. Após essa execução, a API está preparada para receber requisições. O servidor da API será executado em `localhost:5000`.

### Testes:

Caso queira realizar testes rápidos, existe um script `src/scripts/2-testing-api.py` que executa todas as requisições possíveis da API. Também é possível testar a versão da API disponibilizada na núvem, caso a máquina da núvem não tenha desligado.

Outra sugestão é utilizar o [Postman](https://www.postman.com/) para realizar requisições e testar o funcionamento da API.

O arquivo `docs/api.md` apresenta detalhes de quais requisições são possíveis de serem realizadas na API.

### Observações:

* Realizei um preprocessamento nos dados originais de clientes para remover informações confidenciais. Nada muito sério, apenas para simular dados que não devem ser vistos por qualquer um na base de dados.
