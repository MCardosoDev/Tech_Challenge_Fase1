#%%
import pandas as pd
import streamlit as st
import locale
from Utils import plot_pareto, plot_regressao_estimada

#%%
dataset_exp = pd.read_csv('Data/ExpVinhoPeriodo.csv', sep=',')
dataset_exp = dataset_exp.sort_values('Valor', ascending=False)
dataset_exp.head(10)
#%%
dataset_imp = pd.read_csv('Data/ImpVinhosPeriodo.csv', sep=',')
dataset_imp.head(10)
#%%
dataset_exp_pareto = pd.read_csv('Data/ExpPareto.csv', sep=',')
dataset_exp_pareto.head(10)
#%%
dataset_imp_pareto = pd.read_csv('Data/ImpPareto.csv', sep=',')
dataset_imp_pareto.head(10)
#%%
dataset_pib = pd.read_csv('Data/Pib.csv', sep=',')
dataset_pib.head(10)
#%%
dataset_inflation = pd.read_csv('Data/Inflation.csv', sep=',')
dataset_inflation.head(10)
#%%
dataset_trade = pd.read_csv('Data/Trade.csv', sep=',')
dataset_trade.head(10)
#%%
dataset_population = pd.read_csv('Data/Population.csv', sep=',')
dataset_population.head(10)
#%%
dataset_unemployment = pd.read_csv('Data/Unemployment.csv', sep=',')
dataset_unemployment.head(10)
#%%
dataset_exportacao = pd.read_csv('Data/Exportacao.csv', sep=',')
dataset_exportacao.head(10)
#%%
dataset_wht = pd.read_csv('Data/wht.csv', sep=',')
dataset_wht.head(10)
#%%
dataset_exp.Valor.sum()
#%%
dataset_exp.Quantidade.sum()
#%%
total_exp_pareto = dataset_exp_pareto.query("Porcentagem_acumulada_valor < 90 or Porcentagem_acumulada_quantidade < 90")
total_exp_pareto.head(100)
#%%
total_exp_pareto.Pais_destino.head(10)
country_order = list(total_exp_pareto.Pais_destino)
#%%

st.title('Analise sobre a importação de vinhos e insights para melhorias')

tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["Geral", "Exportação de Vinhos", "Vinhos - Princípio de Pareto", "Financeiro - Regressão estimada", "Tipos consumidos", "Resultados"])

with tab0:
    '''
    ## Análise dos Dados para Melhorar a Exportação de Vinhos

    Esta análise tem como objetivo utilizar os dados disponíveis sobre a exportação de vinhos, dados econômicos, demográficos e o ranking de felicidade da população para fornecer insights sobre como melhorar a exportação de vinhos para diferentes países. Os dados foram obtidos de fontes confiáveis, como a Embrapa (Empresa Brasileira de Pesquisa Agropecuária), o Banco Mundial e o Relatório Mundial de Felicidade.
    
    ## Dados Utilizados

    1. **Exportação de Vinhos** - Os dados sobre a exportação de vinhos foram obtidos do Centro Nacional de Pesquisa de Uva e Vinho (CNPUV) da Embrapa. Esses dados fornecem informações relevantes sobre os países que podem ser alvos de exportação de vinhos.

        - Link: [Exportação de Vinhos](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06)

    2. **Dados Econômicos e Demográficos** - Para entender o contexto econômico e demográfico dos países, foram coletados os seguintes dados:

        - **Produto Interno Bruto (PIB)**: O PIB é uma medida amplamente utilizada para avaliar o tamanho e o desempenho econômico de um país.
            - Link: [PIB dos Países](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)

        - **Taxa de Inflação Anual**: A taxa de inflação anual é um indicador que mede a variação dos preços ao longo do tempo e é relevante para entender a estabilidade econômica dos países.
            - Link: [Taxa de Inflação Anual dos Países](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG)

        - **Proporção do Comércio Internacional**: Essa proporção indica a importância do comércio internacional em relação ao PIB de um país, o que pode indicar o quão aberto ele é para o comércio exterior.
            - Link: [Proporção do Comércio Internacional em relação ao PIB dos Países](https://data.worldbank.org/indicator/NE.TRD.GNFS.ZS)

        - **População Total**: O número total de pessoas em um país é relevante para entender o potencial mercado consumidor e a demanda por vinhos.
            - Link: [População Total dos Países](https://data.worldbank.org/indicator/SP.POP.TOTL)

        - **Taxa de Desemprego**: A taxa de desemprego é um indicador importante para avaliar a situação econômica e a capacidade de compra dos consumidores em um país.
            - Link: [Taxa de Desemprego Total dos Países](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS)

    3. **Ranking de Felicidade da População** - O ranking de felicidade é um indicador que avalia o bem-estar e a satisfação da população em diferentes países.

        - Link: [World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness)
  
    ## Análise e Insights

    Com base nos dados coletados, é possível realizar uma análise detalhada para melhorar e exportação de vinhos.
    '''

with tab1:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    valor = locale.currency(dataset_exp.Valor.sum(), grouping=True, symbol=True)
    quantidade = locale.format_string("%.2f", dataset_exp.Quantidade.sum(), grouping=True)
    st.markdown('***Valores totais de exportação de vinhos no período de 15 anos entre 2007 a 2021***')
    st.markdown(
        f"""
        <div style="padding: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #f5f5f5; color: #000000; text-align: center;">
            <p style="font-size: 24px; font-weight: bold; display: inline; margin-right: 100px;">{valor}</p>
            <p style="font-size: 24px; font-weight: bold; display: inline;">{quantidade} L</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    df = pd.DataFrame(dataset_exp)
    st.write("\n")
    st.markdown('##### Dados sobre exportação de vinhos no período')
    st.dataframe(df, use_container_width=True)

with tab2:
    '''
    ##### Países que mais impactam na exportação de vinhos - Princípio 80/20

    ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
    '''
    st.markdown('###### Valor US$')
    st.plotly_chart(
        plot_pareto(
            total_exp_pareto,
            "Pais_destino",
            "Valor",
            "Pais_destino",
            "Porcentagem_acumulada_valor",
            "Países",
            "Vendas",
            total_exp_pareto.Valor.mean()
        ),  use_container_width = True
    )
    st.write("\n")
    st.markdown('###### Quantidade KG/L')
    st.plotly_chart(
        plot_pareto(
            total_exp_pareto,
            "Pais_destino",
            "Quantidade",
            "Pais_destino",
            "Porcentagem_acumulada_quantidade",
            "Países",
            "Quantidade",
            total_exp_pareto.Quantidade.mean()
        ),  use_container_width = True
    )

with tab3:
    '''
    ##### Valores financeiros dos países que mais impactam na exportação de vinhos

    ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
    '''
    st.markdown('###### Valor US$')
    st.plotly_chart(
        plot_regressao_estimada(
            dataset_exportacao,
            'Valores de exportação para os principais países',
            int,
            country_order[:-5]
        ),
        use_container_width = True
    )
    st.plotly_chart(
        plot_regressao_estimada(
            dataset_pib,
            'PIB dos países responsáveis por 80% da exportação',
            float,
            country_order[:-5]
        ),
        use_container_width = True
    )
    st.plotly_chart(
        plot_regressao_estimada(
            dataset_inflation,
            'Inflação dos países responsáveis por 80% da exportação',
            float,
            country_order[:-5]
        ),
        use_container_width = True
    )
    st.plotly_chart(
        plot_regressao_estimada(
            dataset_trade,
            'Comércio internacional do países responsáveis por 80% da exportação',
            float,
            country_order[:-5]
        ),
        use_container_width = True
    )
    st.plotly_chart(
        plot_regressao_estimada(
            dataset_population,
            'População dos países responsáveis por 80% da exportação',
            int,
            country_order[:-5]
        ),
        use_container_width = True
    )
    st.plotly_chart(
        plot_regressao_estimada(
            dataset_unemployment,
            'Desemprego dos países responsáveis por 80% da exportação',
            float,
            country_order[:-5]
        ),
        use_container_width = True
    )
    st.plotly_chart(
        plot_regressao_estimada(
            dataset_wht,
            'World Happiness dos países responsáveis por 80% da exportação',
            int,
            country_order = ['Paraguay','Russia','United States','United Kingdom','China','Netherlands','Spain']
        ),
        use_container_width = True
    )
with tab4:
    '''
    ##### Valores financeiros dos países que mais impactam na exportação de vinhos

    ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
    '''

with tab5:
    '''
    ##### Valores financeiros dos países que mais impactam na exportação de vinhos

    ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
    '''