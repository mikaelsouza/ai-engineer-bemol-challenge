# Metadados de Dados Preprocessados

Durante o processo do desafio, alguns arquivos auxiliáres e finais foram gerados para serem utilizados em alguns momentos.

Seguem os 3 documentos gerados e suas respectivas características:

1. `rfm.csv`: Contém informações relacionadas a frequência, recência, quantia gasta e localização de cada cliente.
2. `labeled_rfm.csv`: Mesmo arquivo que `rfm.csv`, porém acrescentado da coluna label que identifica o tipo de cada cliente da base.
3. `confidential_rfm`: Mesmo arquivo que `labeled_rfm.csv`, porém sem as informações de frequência, recência e quantia gasta do cliente. Foi criado apenas pelo desconforto que qualquer pessoa com acesso a API teria TODAS as informações relacionadas ao cliente.

### Colunas:

Todas as colunas geradas estão descritas no notebook `notebooks/1-data-exploration.ipynb`, porém, para reiterar alguns aspectos serão brevemente apresentadas o que cada atributo representa.

* `CustomerID`: ID único numérico de cada cliente existente na base de dados.
* `Recency`: Valor numérico que representa a quantidade de dias que o cliente fez sua última compra comparada com a compra mais recente existente entre os clientes.
* `Frequency`: Contagem da quantidade de vezes que um cliente realizou uma compra (sem cancelar) com a empresa.
* `Amount`: Soma de todos os gastos realizados por aquele cliente.
* `Country`: País de origem do cliente.
* `Label`: Grupo em que o cliente foi enquadrado pelo modelo.