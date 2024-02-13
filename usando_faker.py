# -*- coding: utf-8 -*-
import pandas as pd
from faker import Faker
import random
from typing import List, Dict, Any, Union

fake = Faker('pt_BR')

def gerar_dados_venda(num_items: int) -> List[Dict[str, Any]]:
    """
    Gera dados fictícios de vendas.

    Parameters:
        num_items (int): Número de itens a serem gerados.

    Returns:
        List[Dict[str, Any]]: Lista de dicionários contendo os dados de vendas.
    """
    if not isinstance(num_items, int) or num_items <= 0:
        raise ValueError("O número de itens deve ser um inteiro positivo.")

    dados_venda = []

    for _ in range(num_items):
        venda = {
            "ID_Fatura": fake.unique.random_number(digits=9),
            "Filial": random.choice(['A', 'B', 'C']),
            "Estado": fake.estado_nome(),
            "Tipo_Cliente": random.choice(['Membro', 'Normal']),
            "Genero": fake.random_element(['Masculino', 'Feminino']),
            "Linha_Produto": fake.random_element(['Saúde e beleza', 'Eletrônicos', 'Casa e estilo de vida', 'Esportes e viagens', 'Alimentos e bebidas']),
            "Preço_Unitario": round(random.uniform(10, 100), 2),
            "Quantidade": random.randint(1, 10),
            "Imposto_5%": 0,  # Você pode ajustar a lógica do imposto conforme necessário
            "Total": 0,  # Você pode ajustar a lógica do total conforme necessário
            "Data": fake.date_this_year(),
            "Hora": fake.time(pattern='%H:%M'),
            "Pagamento": fake.random_element(['Cartão de crédito', 'Ewallet', 'Dinheiro']),
            "COGS": 0,  # Você pode ajustar a lógica do COGS conforme necessário
            "Margem_Bruta_%": round(random.uniform(3, 8), 6),
            "Renda_Bruta": 0,  # Você pode ajustar a lógica da renda bruta conforme necessário
            "Avaliacao": round(random.uniform(4, 9), 1)
        }

        # Atualize os campos calculados conforme necessário
        venda["Imposto_5%"] = round(venda["Preço_Unitario"] * venda["Quantidade"] * 0.05, 4)
        venda["Total"] = round(venda["Preço_Unitario"] * venda["Quantidade"] + venda["Imposto_5%"], 4)
        venda["COGS"] = round(venda["Total"] * 0.8, 2)
        venda["Renda_Bruta"] = round(venda["Total"] - venda["COGS"], 4)

        dados_venda.append(venda)

    return dados_venda

def salva_excel(data: List[Dict[str, Any]], filename: str) -> None:
    """
    Salva os dados em um arquivo Excel.

    Parameters:
        data (List[Dict[str, Any]]): Lista de dicionários contendo os dados.
        filename (str): Nome do arquivo Excel.

    Returns:
        None
    """
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, engine='openpyxl')



if "__main__" == __name__:
    # Gerar dados de vendas
    dados_venda = gerar_dados_venda(1000)
    # Salvar os dados em um arquivo Excel
    salva_excel(dados_venda, 'mercado_faker.xlsx')
