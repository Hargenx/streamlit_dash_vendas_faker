# -*- coding: utf-8 -*-
import pandas as pd
from faker import Faker
import random

fake = Faker('pt_BR')

def generate_sales_data(num_items):
    sales_data = []

    for _ in range(num_items):
        invoice_id = fake.unique.random_number(digits=9)
        branch = random.choice(['A', 'B', 'C'])
        city = fake.city()
        customer_type = random.choice(['Membro', 'Normal'])
        gender = fake.random_element(['Masculino', 'Feminino'])
        product_line = fake.random_element(['Saúde e beleza', 'Eletrônicos', 'Casa e estilo de vida', 'Esportes e viagens', 'Alimentos e bebidas'])
        unit_price = round(random.uniform(10, 100), 2)
        quantity = random.randint(1, 10)
        tax = round(unit_price * quantity * 0.05, 4)
        total = round(unit_price * quantity + tax, 4)
        date = fake.date_this_year()
        time = fake.time(pattern='%H:%M')
        payment = fake.random_element(['Cartão de crédito', 'Ewallet', 'Dinheiro'])
        cogs = round(total * 0.8, 2)
        gross_margin_percentage = round(random.uniform(3, 8), 6)
        gross_income = round(total * (gross_margin_percentage / 100), 4)
        rating = round(random.uniform(4, 9), 1)

        sales_data.append([invoice_id, branch, city, customer_type, gender, product_line, unit_price, quantity, tax, total, date, time, payment, cogs, gross_margin_percentage, gross_income, rating])

    return sales_data

def save_to_excel(data, filename):
    df = pd.DataFrame(data, columns=["ID da Fatura", "Filial", "Cidade", "Tipo de Cliente", "Gênero", "Linha de Produto", "Preço Unitário", "Quantidade", "Imposto 5%", "Total", "Data", "Hora", "Pagamento", "COGS", "Margem Bruta %", "Renda Bruta", "Avaliação"])
    df.to_excel(filename, index=False, engine='openpyxl')


# Gerar dados de vendas
sales_data = generate_sales_data(1000)

# Salvar os dados em um arquivo Excel
save_to_excel(sales_data, 'mercado_fake.xlsx')
