#%%
import pandas as pd
import streamlit as st
import locale
from Utils import plot_pareto, plot_regressao_estimada, plot_consumo_projetado, plot_comparacao

#%%
dataset_exp = pd.read_csv('ExpVinhoPeriodo.csv', sep=',')
dataset_exp = dataset_exp.sort_values('Valor', ascending=False)
dataset_exp.head(10)

#%%
dataset_imp = pd.read_csv('ImpVinhosPeriodo.csv', sep=',')
dataset_imp = dataset_imp.sort_values('Valor', ascending=False)
dataset_imp.head(10)

#%%
dataset_exp_pareto = pd.read_csv('ExpPareto.csv', sep=',')
dataset_exp_pareto.head(10)

#%%
dataset_imp_pareto = pd.read_csv('ImpPareto.csv', sep=',')
dataset_imp_pareto.head(10)

#%%
dataset_pib = pd.read_csv('Pib.csv', sep=',')
dataset_pib.head(10)

#%%
dataset_inflation = pd.read_csv('Inflation.csv', sep=',')
dataset_inflation.head(10)

#%%
dataset_trade = pd.read_csv('Trade.csv', sep=',')
dataset_trade.head(10)

#%%
dataset_population = pd.read_csv('Population.csv', sep=',')
dataset_population.head(10)

#%%
dataset_unemployment = pd.read_csv('Unemployment.csv', sep=',')
dataset_unemployment.head(10)

#%%
dataset_exportacao = pd.read_csv('Exportacao.csv', sep=',')
dataset_exportacao.head(10)

#%%
dataset_importacao = pd.read_csv('Importacao.csv', sep=',')
dataset_importacao.head(10)

#%%
dataset_consumo = pd.read_csv('Consumo.csv', sep=',')
dataset_consumo.head(10)

#%%
dataset_consumo_vinho = pd.read_csv('ConsumoVinho.csv', sep=',')
dataset_consumo_vinho.head(10)

#%%
dataset_wht = pd.read_csv('wht.csv', sep=',')
dataset_wht.head(10)

#%%
dataset_exp.Valor.sum()

#%%
dataset_exp.Quantidade.sum()

#%%
total_exp_pareto = dataset_exp_pareto.query("Porcentagem_acumulada_valor < 91 or Porcentagem_acumulada_quantidade < 91")
total_exp_pareto.head(10)

#%%
total_imp_pareto = dataset_imp_pareto.query("Porcentagem_acumulada_valor < 99 or Porcentagem_acumulada_quantidade < 99")
total_imp_pareto.head(10)

#%%
imp_ordem_pareto = list(total_imp_pareto.Pais_destino)
exp_ordem_pareto = list(total_exp_pareto.Pais_destino)

#%%
def main():
    st.set_page_config(layout="wide")
    st.title('Analise sobre a importação de vinhos e insights para melhorias')
    tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
                                                                "Geral",
                                                                "Exportação de Vinhos",
                                                                "Vinhos - Princípio de Pareto",
                                                                "Valores de Exportação",
                                                                "Valores de Importação",
                                                                "Econômicos - Banco Mundial",
                                                                "Consumo de álcool - WHO/OIV",
                                                                "Resultados"
                                                            ])

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
        
        4. **Consumo de Álcool** - Os dados sobre o consumo de álcool per capita foram obtidos da Organização Mundial da Saúde (OMS). Esses dados fornecem informações sobre a quantidade de álcool (incluindo registro e não registro) consumida por pessoa com idade igual ou superior a 15 anos em diferentes países, juntamente com projeções com intervalo de confiança de 95% para os anos de 2020 e 2025. Isso pode ajudar a entender os hábitos de consumo de bebidas alcoólicas e o potencial de mercado para vinhos em cada país.

           - Link: [WHO](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/alcohol-total-(recorded-unrecorded)-per-capita-(15-)-consumption-with-95-ci-projections-to-2020-and-2025)

        5. **Dados sobre o consumo de vinho** - A OIV fornece estatísticas abrangentes sobre o consumo de vinho em diferentes países. Esses dados podem incluir informações sobre o consumo per capita, o volume total de consumo, entre outros aspectos relevantes para entender o mercado do vinho em cada país.

           - Link: [OIV](https://www.oiv.int/en/statistics)

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
                <p style="font-size: 24px; font-weight: bold; display: inline; margin-right: 400px;">{valor}</p>
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
        ##### Valores por país para os países que mais impactam na exportação de vinhos

        ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
        '''
        st.markdown('###### Valor US$')
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_exportacao[dataset_exportacao['pais'].isin(exp_ordem_pareto)],
                'Valores de exportação para os principais países',
                int,
                exp_ordem_pareto
            ),
            use_container_width = True
        )
        '''
            Para estimativa de **Regressão** foi utilizado para calcular o coeficientes do polinômio ajustado com a função polyfit do numpy para grau 1 que utiliza o método dos mínimos quadrados, que minimiza o erro quadrático.
            - E = Σᵢ(yᵢ - p(xᵢ))²
            - p(x) = p[0] * xᵈᵉᵍ + p[1] * xᵈᵉᵍ⁻¹ + ... + p[deg-1] * x + p[deg]
        '''

    with tab4:
        '''
        ##### Valores por país dos que mais importamos vinhos

        ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
        '''
        st.markdown('###### Valor US$')
        st.plotly_chart(
            plot_pareto(
                total_imp_pareto,
                "Pais_destino",
                "Valor",
                "Pais_destino",
                "Porcentagem_acumulada_valor",
                "Países",
                "Vendas",
                total_imp_pareto.Valor.mean()
            ),  use_container_width = True
        )
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_importacao[dataset_importacao['pais'].isin(imp_ordem_pareto)],
                'Valores de importação para os principais países',
                int,
                imp_ordem_pareto
            ),
            use_container_width = True
        )
        '''
            Para estimativa de **Regressão**foi utilizado para calcular o coeficientes do polinômio ajustado com a função polyfit do numpy para grau 1 que utiliza o método dos mínimos quadrados, que minimiza o erro quadrático.
            - E = Σᵢ(yᵢ - p(xᵢ))²
            - p(x) = p[0] * xᵈᵉᵍ + p[1] * xᵈᵉᵍ⁻¹ + ... + p[deg-1] * x + p[deg]
        '''

    with tab5:
        '''
        ##### Valores financeiros dos países que mais impactam na exportação de vinhos

        ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
        '''
        st.markdown('###### Valor US$')
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_pib[dataset_pib['pais'].isin(exp_ordem_pareto)],
                'PIB dos países responsáveis por 80% da exportação',
                float,
                exp_ordem_pareto
            ),
            use_container_width = True
        )
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_inflation[dataset_inflation['pais'].isin(exp_ordem_pareto)],
                'Inflação dos países responsáveis por 80% da exportação',
                float,
                exp_ordem_pareto
            ),
            use_container_width = True
        )
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_trade[dataset_trade['pais'].isin(exp_ordem_pareto)],
                'Comércio internacional do países responsáveis por 80% da exportação',
                float,
                exp_ordem_pareto
            ),
            use_container_width = True
        )
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_population[dataset_population['pais'].isin(exp_ordem_pareto)],
                'População dos países responsáveis por 80% da exportação',
                int,
                exp_ordem_pareto
            ),
            use_container_width = True
        )
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_unemployment[dataset_unemployment['pais'].isin(exp_ordem_pareto)],
                'Desemprego dos países responsáveis por 80% da exportação',
                float,
                exp_ordem_pareto
            ),
            use_container_width = True
        )
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_wht[dataset_wht['pais'].isin(exp_ordem_pareto)],
                'World Happiness dos países responsáveis por 80% da exportação',
                int,
                exp_ordem_pareto
            ),
            use_container_width = True
        )
        '''
            Para estimativa de **Regressão** foi utilizado para calcular o coeficientes do polinômio ajustado com a função polyfit do numpy para grau 1 que utiliza o método dos mínimos quadrados, que minimiza o erro quadrático.
            - E = Σᵢ(yᵢ - p(xᵢ))²
            - p(x) = p[0] * xᵈᵉᵍ + p[1] * xᵈᵉᵍ⁻¹ + ... + p[deg-1] * x + p[deg]
        '''

    with tab6:
        '''
        ##### Valores de consumo de álcool e somente vinho dos países que mais impactam na exportação de vinhos

        ***Valores sobre o consumo de vinho correspondentes ao período de 15 anos entre 2007 a 2021***
        ***Valores sobre o consumo de álcool correspondentes ao fato e projeção com intervalo de confiança de 95% para os anos de 2020 e 2025***
        '''
        st.markdown('###### Valor US$')
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_consumo_vinho[dataset_consumo_vinho['pais'].isin(exp_ordem_pareto)],
                'Valores de consumo de vinho dos países responsáveis por 80% da exportação',
                int,
                exp_ordem_pareto
            ),
            use_container_width = True
        )
        '''
            Para estimativa de **Regressão** foi utilizado para calcular o coeficientes do polinômio ajustado com a função polyfit do numpy para grau 1 que utiliza o método dos mínimos quadrados, que minimiza o erro quadrático.
            - E = Σᵢ(yᵢ - p(xᵢ))²
            - p(x) = p[0] * xᵈᵉᵍ + p[1] * xᵈᵉᵍ⁻¹ + ... + p[deg-1] * x + p[deg]
        '''
        st.plotly_chart(
            plot_consumo_projetado(
                dataset_consumo[dataset_consumo['pais'].isin(exp_ordem_pareto)],
                'Diferença entre a projeção do consumo de álcool dos países responsáveis por 80% da exportação',
                exp_ordem_pareto
            ),
            use_container_width = True
        )
        '''
            Dados disponíveis no **World Health Organization**

            Diferença corresponde ao valor da projeção para 2025 menos valor fato de 2020
        '''

    with tab7:
        '''
        #### Resultados da analise
        
        Com a análise dos dados de exportação, principalmente financeiros, notamos que, apesar da crise global em 2019-2020 devido à Covid-19, observamos um cenário favorável para a economia em 2021, principalmente em alguns países na exportação de vinhos.

        Dois países, Paraguai e Rússia, são responsáveis por 80% do volume exportado e quase 80% do montante total. Montamos uma lista dos países mais favoráveis a um aumento na exportação de vinhos brasileiros:

        - **Paraguai**
        - **Rússia**
        - **Estados Unidos**
        - **Reino Unido**
        - **China**
        - **Países Baixos**
        - **Alemanha**
        - **Haiti**

        Excluiremos os países analisados que são responsáveis pelo maior volume do qual importamos vinho, devido à correlação negativa entre importação e exportação, com exceção dos Estados Unidos que é um país com um mercado muito grande para exportação como a china.

        Um país com uma queda alta na exportação, mas que, apesar da Covid-19, está com o PIB em uma crescente histórica, inflação e desemprego baixos e com aumento no índice de comércio no último ano.

        De acordo com a Organização Mundial da Saúde (OMS) e a Organização Internacional da Vinha e do Vinho (OIV), os Estados Unidos devem ter um aumento no consumo de bebidas alcoólicas até 2025, seguindo um aumento histórico no consumo de vinho.

        Graficamente, podemos comparar os dados de exportação e importação para visualizar a correlação:
        '''
        st.markdown('###### Valor US$')
        st.plotly_chart(
            plot_comparacao(
                dataset_exportacao.query("pais == 'Estados Unidos'"),
                dataset_importacao.query("pais == 'Estados Unidos'"),
                'Exportação',
                'Importação',
                'Regressão de Exportação e Importação Estados Unidos',
                int,
                'Estados Unidos'
            ),
            use_container_width = True
        )
        # st.write("\n")
        # st.plotly_chart(
        #     plot_regressao_estimada(
        #         dataset_importacao.query("pais == 'Estados Unidos'"),
        #         'Valores de importação para os principais países',
        #         int,
        #         pais_comparacao
        #     ),
        #     use_container_width = True
        # )
        '''
        O Paraguai é um país de fronteira que propicia a exportação, e mesmo após a queda da exportação em 2019-2020, teve um aumento em 2021 e segue em uma tendência histórica de crescimento. O mesmo ocorre com o PIB, inflação e aumento do índice de comércio exterior. De acordo com a OMS e a OIV, é projetado um aumento no consumo de bebidas alcoólicas de até 25%, mesmo com uma queda histórica no consumo de vinho nos últimos anos.

        Chile, Uruguai e Argentina, apesar de importarem uma quantidade alta para o Brasil, seguem a correlação negativa entre importação e exportação.

        A Rússia e o Reino Unido são países que têm valores de exportação de vinhos bastante semelhantes e, após a Covid-19, tiveram um aumento no PIB. Apesar de um aumento na inflação vindo de uma queda histórica, apresentam o mesmo índice de comércio exterior. De acordo com a OMS e a OIV, é projetado um aumento no consumo de álcool de até 2025, e ambos estão em crescimento no consumo de vinho nos últimos anos.

        A China, apesar de ter uma queda na exportação de vinho em 2021, é um país com um mercado de grande potencial a ser explorado. Apresenta um aumento histórico no PIB e queda histórica na inflação, mesmo durante a Covid-19. De acordo com a OMS e a OIV, é projetado um aumento no consumo de álcool, porém com uma queda forte no consumo de vinho.

        Países Baixos e Alemanha, apesar de uma exportação em queda nos últimos anos, de acordo com a OMS e a OIV, é projetada uma queda no consumo de álcool, mas com um aumento no consumo de vinho nos últimos anos, o que pode ser explorado. A Alemanha está em uma queda histórica e os Países Baixos em um aumento histórico. Após a Covid-19, houve um aumento no PIB e, apesar do aumento da inflação em 2021, historicamente se mantêm estáveis. Ambos os países têm um aumento histórico no índice de comércio.

        O Haiti é um país que, apesar de ter um clima mais quente, assim como o Paraguai, teve o maior aumento na exportação de vinhos brasileiros. É o país com o maior aumento histórico do PIB da lista, mesmo com a Covid-19. Apesar de um aumento histórico na inflação, teve uma grande queda em 2021. De acordo com a OMS e a OIV, é projetado um aumento no consumo de álcool e um aumento histórico no consumo de vinho, apesar de uma queda no índice de comércio exterior. No entanto, mantém um aumento na exportação.

        '''
        '''
            Para estimativa de **Regressão** foi utilizado para calcular o coeficientes do polinômio ajustado com a função polyfit do numpy para grau 1 que utiliza o método dos mínimos quadrados, que minimiza o erro quadrático.
            - E = Σᵢ(yᵢ - p(xᵢ))²
            - p(x) = p[0] * xᵈᵉᵍ + p[1] * xᵈᵉᵍ⁻¹ + ... + p[deg-1] * x + p[deg]
        '''

if __name__ == "__main__":
    main()