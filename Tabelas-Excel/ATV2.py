import pandas as pd

# Dados do Balanço Patrimonial (BP)
bp_data = {
    'Contas': [
        'Salários e encargos', 'Impostos, taxas e contribuições a recolher', 'Aplicações financeiras (Curto Prazo)', 
        'Investimentos', 'Estoques', 'Contas a receber', 'Tributos a recuperar', 'Veículos',
        'Imobilizado', 'Aplicações financeiras (Longo Prazo)', 'Instrumentos financeiros derivativos (Longo Prazo)',
        'Provisões (Longo Prazo)', 'Benefícios a funcionários (Longo Prazo)', 'Outros ativos (Longo Prazo)',
        'Contas a pagar (Curto Prazo)', 'Empréstimos e financiamentos (Curto Prazo)', 'Provisões (Curto Prazo)',
        'Empréstimos e financiamentos (Longo Prazo)', 'Instrumentos financeiros derivativos (Longo Prazo)',
        'Capital social'
    ],
    'Valores': [
        2128.55, 513.32, 277.20, 289.06, 9619.02, 5741.50, 3435.69, 7969.59, 26630.16, 242.17, 
        11.64, 559.61, 2011.80, 38003.64, 23195.10, 1298.09, 418.40, 2202.98, 1054.34, 58177.99
    ]
}

# Dados do Demonstrativo de Fluxo de Caixa (DFC)
dfc_data = {
    'Atividades': [
        'Geração de caixa das atividades operacionais', '(Aumento)/redução no contas a receber e demais contas a receber',
        '(Aumento)/redução nos estoques', '(Aumento)/(redução) no contas a pagar e demais contas a pagar', 
        'Juros pagos', 'Juros recebidos', 'Imposto de renda e contribuição social (pagos)/creditados',
        'Proventos/(recompra) de ações', 'Aquisição de participação de não controladores', 'Proventos de empréstimos', 
        'Liquidação de empréstimos', 'Caixa líquido de custos financeiros, exceto juros', 'Pagamento de passivos de arrendamento', 
        'Dividendos e juros sobre o capital próprio pagos', 'Proventos da venda de imobilizado e intangíveis', 
        'Aquisição de imobilizado e intangíveis', 'Aplicação financeira/proventos líquidos de títulos de dívida', 
        'Proventos/(aquisição) de outros ativos, líquidos'
    ],
    'Ano 1': [
        3845.23, 370.76, 357.86, 1308.55, 126.93, 361.85, 726.74, 291.10, 2.93, 20.35, 444.54, 547.68, 346.08, 
        85.96, 54.75, 1028.09, 0.00, 109.55
    ],
    'Ano 2': [
        3807.73, 47.95, 333.85, 1793.42, 147.20, 208.54, 453.69, 20.23, 7.09, 0.00, 54.76, 1211.27, 284.61, 
        128.61, 34.45, 1295.74, 1.90, 44.83
    ]
}

# Criando DataFrames para cada tabela
bp_df = pd.DataFrame(bp_data)
dfc_df = pd.DataFrame(dfc_data)

# Criando um writer para salvar várias abas no mesmo arquivo Excel
with pd.ExcelWriter('balanco_e_fluxo_de_caixa.xlsx', engine='xlsxwriter') as writer:
    # Escrever cada DataFrame em uma aba específica
    bp_df.to_excel(writer, sheet_name='Balanço Patrimonial', index=False)
    dfc_df.to_excel(writer, sheet_name='Fluxo de Caixa', index=False)

print("Arquivo Excel com Balanço Patrimonial e Fluxo de Caixa foi gerado com sucesso.")
