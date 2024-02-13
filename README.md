# Dashboard de Vendas com Streamlit

Este é um projeto simples de dashboard de vendas usando o Streamlit. Ele inclui um script (`main.py`) que cria visualizações interativas e dinâmicas com base em dados de vendas. Além disso, há um script (`usando_faker.py`) para gerar dados fictícios que podem ser usados para testar o dashboard.

## Instalação

Antes de começar, é necessário instalar as dependências do projeto. Certifique-se de ter o Python e o pip instalados. Em seguida, execute o seguinte comando no terminal para instalar as dependências:

```bash
pip install -r requirements.txt
```

## Gerando Dados Fictícios
Para gerar dados fictícios de vendas, execute o script usando_faker.py. Este script usa a biblioteca Faker para criar dados aleatórios realistas de vendas.
```bash
python usando_faker.py
```

- Isso criará um arquivo Excel chamado mercado_faker.xlsx com os dados fictícios gerados.

## Executando o Dashboard
Para executar o dashboard, utilize o script main.py.
```bash
streamlit run main.py
```
O Streamlit iniciará um servidor local e fornecerá um link que você pode abrir no navegador para visualizar o dashboard.

Certifique-se de ter todas as dependências instaladas antes de executar o script.

## Personalização
Você pode personalizar o projeto ajustando os parâmetros em usando_faker.py para gerar diferentes quantidades de dados fictícios ou alterando os gráficos e layouts em main.py para atender às suas necessidades específicas.

Sinta-se à vontade para explorar, modificar e expandir este projeto conforme desejar!

## Licença
Este projeto está sob a [Licença MIT](LICENSE).