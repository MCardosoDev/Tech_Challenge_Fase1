#%%
import pandas as pd
import streamlit as st
from Utils import plot_pareto
from Utils import plot_regressao_estimada
from Utils import plot_consumo_projetado
from Utils import plot_comparacao
from Utils import plot_per_anual
from Utils import plot_regressao1

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
dataset_Qexp_pareto = pd.read_csv('QExpPareto.csv', sep=',')
dataset_Qexp_pareto.head(10)

#%%
dataset_exp_pareto_5 = pd.read_csv('ExpPareto5.csv', sep=',')
dataset_exp_pareto_5.head(10)

#%%
dataset_anos = pd.read_csv('PorcentAnual.csv', sep=',',index_col=0)
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
total_exp_pareto = dataset_exp_pareto.query("Porcentagem_acumulada_valor < 75")
total_exp_pareto.head(10)

#%%
total_imp_pareto = dataset_imp_pareto.query("Porcentagem_acumulada_valor < 99 or Porcentagem_acumulada_quantidade < 99")
total_imp_pareto.head(10)

#%%
imp_ordem_pareto = list(total_imp_pareto.Pais_destino)
exp_ordem_pareto = list(total_exp_pareto.Pais_destino)
ordem=["Paraguai","Estados Unidos", "China","Haiti","Reino Unido", "Rússia"]

#%%
def main():
    st.set_page_config(layout="wide")
    st.title('Análise sobre a importação de vinhos e insights para melhorias')
    tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
                                                                "Geral",
                                                                "Exportação de Vinhos",
                                                                "Vinhos - Analise de Pareto",
                                                                "Valores de Exportação",
                                                                "Cenário mais Recente",
                                                                "Valores de Importação",
                                                                "Dados Externos",
                                                                "Conclusões"
                                                            ])

    with tab0:

        '''
        ## Análise dos Dados para Melhorar a Exportação de Vinhos

        Esta análise tem como objetivo utilizar os dados disponíveis sobre a exportação de vinhos, dados econômicos e sobre consumo de vinho e de álcool, com objetivo de fornecer insights sobre como melhorar a exportação de vinhos para diferentes países. Os dados foram obtidos de fontes confiáveis, como a Embrapa (Empresa Brasileira de Pesquisa Agropecuária), o Banco Mundial, Organização Mundial de Sáude e Organização Internacional da Vinha e do Vinho.
        
        ## Dados Utilizados

        1. **Exportação de Vinhos** - Os dados sobre a exportação de vinhos foram obtidos do Centro Nacional de Pesquisa de Uva e Vinho (CNPUV) da Embrapa. Esses dados fornecem informações relevantes sobre os países que podem ser alvos de exportação de vinhos.

            - Link: [Exportação de Vinhos](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06)

        2. **Dados Econômicos** - Para entender o contexto econômico dos países, foram coletados os seguintes dados:

            - **Produto Interno Bruto (PIB)**: O PIB é uma medida amplamente utilizada para avaliar o tamanho e o desempenho econômico de um país.
                - Link: [PIB dos Países](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)

            - **Taxa de Inflação Anual**: A taxa de inflação anual é um indicador que mede a variação dos preços ao longo do tempo e é relevante para entender a estabilidade econômica dos países.
                - Link: [Taxa de Inflação Anual dos Países](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG)

            - **Proporção do Comércio Internacional**: Essa proporção indica a importância do comércio internacional em relação ao PIB de um país, o que pode indicar o quão aberto ele é para o comércio exterior.
                - Link: [Proporção do Comércio Internacional em relação ao PIB dos Países](https://data.worldbank.org/indicator/NE.TRD.GNFS.ZS)
      
        3. **Consumo de Álcool** - Os dados sobre o consumo de álcool per capita foram obtidos da Organização Mundial da Saúde (WHO/OMS). Esses dados fornecem informações sobre a quantidade de álcool (incluindo registro e não registro) consumida por pessoa com idade igual ou superior a 15 anos em diferentes países, juntamente com projeções com intervalo de confiança de 95% para os anos de 2020 e 2025. Isso pode ajudar a entender os hábitos de consumo de bebidas alcoólicas e o potencial de mercado para vinhos em cada país.

           - Link: [WHO](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/alcohol-total-(recorded-unrecorded)-per-capita-(15-)-consumption-with-95-ci-projections-to-2020-and-2025)

        4. **Dados sobre o consumo de vinho** - A Organização Internacional da Vinha e do Vinho (OIV) fornece estatísticas abrangentes sobre o consumo de vinho em diferentes países. Esses dados podem incluir informações sobre o consumo per capita, o volume total de consumo, entre outros aspectos relevantes para entender o mercado do vinho em cada país.

           - Link: [OIV](https://www.oiv.int/en/statistics)

        ## Análise e Insights

        Com base nos dados coletados, é possível realizar uma análise detalhada para melhorar a exportação de vinhos.
        '''

    with tab1:
        valor = "{:,.2f}".format(dataset_exp.Valor.sum())
        quantidade = "{:,.2f}".format(dataset_exp.Quantidade.sum())
        st.markdown('***Valores totais de exportação de vinhos no período de 15 anos entre 2007 a 2021***')
        st.markdown(
            f"""
            <div style="padding: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #f5f5f5; color: #000000; text-align: center;">
                <p style="font-size: 24px; font-weight: bold; display: inline; margin-right: 400px;">US$ {valor}</p>
                <p style="font-size: 24px; font-weight: bold; display: inline;">{quantidade} L</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        df = pd.DataFrame(dataset_exp)
        df.rename(columns={'Pais_destino': 'Destino', 'Pais_origem': 'Origem', 'Quantidade': 'Quantidade (L)', 'Valor':'Valor (US$)'}, inplace=True)
        
        st.write("\n")
        st.markdown('##### Dados sobre exportação de vinhos no período')
        st.dataframe(df, use_container_width=True)
        #st.table(dataset_exp.rename(columns=colunas_personalizadas),use_container_width=True)

    with tab2:

        '''
        ##### Países que mais impactam na exportação de vinhos - Princípio 80/20

        ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
        '''

        st.markdown('###### Quantidade (L)')
        st.plotly_chart(
            plot_pareto(
                dataset_Qexp_pareto.query("Porcentagem_acumulada_quantidade < 92"),
                "Pais_destino",
                "Quantidade",
                "Pais_destino",
                "Porcentagem_acumulada_quantidade",
                "País",
                "Quantidade",
                dataset_Qexp_pareto.Quantidade.mean()
            ),  use_container_width = True
        )

        '''
            Analisando o gráfico de pareto para volume total de vinho exportado pelo Brasil entre 2007 e 2021, nota-se que Rússia, Paraguai e Estados Unidos são responsáveis por 
            mais de 80% desse volume.
        
        '''

        st.write("\n")
        st.markdown('###### Valor (US$)')
        st.plotly_chart(
            plot_pareto(
                dataset_exp_pareto.query("Porcentagem_acumulada_valor < 81"),
                "Pais_destino",
                "Valor",
                "Pais_destino",
                "Porcentagem_acumulada_valor",
                "País",
                "Valor",
                dataset_exp_pareto.Valor.mean()
            ),  use_container_width = True
        )
        
        '''
            Ao observar o gráfico para valor total de vendas com a exportação de vinho nesse mesmo período, percebe-se que o Paraguai ultrapassa o percentual da Rússia, e
            que Reino Unido passa a ter maior representatividade no percentual. O que indica que, nesse país, o vinho brasileiro é exportado por um valor superior.
        
        '''
        
    with tab3:
         
        st.plotly_chart(
            plot_per_anual(dataset_anos),
            use_container_width = True
        )

        '''
        O gráfico acima ilustra como foi a distribuição dos valores exportados de vinho pelo Brasil entre 2007 e 2021. Alguns pontos interessantes ilustrados no gráfico são:\n
        - Os picos de exportação em 2009 e 2013
        - Queda no total de exportações em 2010
        - Crescimento das exportações para o Paraguai
                
        #### Os picos de exportação em 2009 e 2013
        Observando a altura total das barras, constata-se que houve dois picos, um no ano de 2009 e outro no ano de 2013. Avaliando o percentual de influência dos países na exportação, 
        percebe-se que ambos os picos ocorreram devido ao crescimento das vendas para a **Rússia**. \n
        Analisando abaixo o comportamento dos valores exportados para a Rússia ao longo dos anos, é possível notar esses picos. Contudo, após 2013, as vendas caíram bruscamente.
        '''

        st.plotly_chart(
            plot_regressao1(
                dataset_exportacao.set_index('pais').query("pais=='Rússia'").reset_index(),
                'Valores de exportação para Rússia (US$)',
                int
            ),
            use_container_width = True
        )

        '''
        O aumento das exportações para Rússia entre 2011 e 2013 pode ser uma consequência da sua adesão à OMC. Pois, _"Após 18 anos de negociações, a adesão da Rússia à OMC foi aceita em 2011"_.
        '''
        st.markdown(
        '<span class="small-font">Fonte: https://g1.globo.com/economia/noticia/2011/11/russia-entra-na-omc-apos-18-anos-de-negociacoes.html',
        unsafe_allow_html=True
        )
        '''
        Já a queda em 2014 pode ser explicada pelo embargos que a Rússia vem sofrendo. _"Após a anexação da Crimeia em março de 2014 e o envolvimento da Rússia no conflito em curso na Ucrânia, os Estados Unidos, a UE, o Canadá, o Japão e outros países impuseram sanções aos setores financeiro, energético e de defesa da Rússia."_
        '''
        st.markdown(
        '<span class="small-font">Fonte: https://g1.globo.com/bom-dia-brasil/noticia/2014/03/ue-e-eua-ampliam-sancoes-contra-russia-apos-anexacao-da-crimeia.html',
        unsafe_allow_html=True
        )
        '''
        #### Queda no total de exportações em 2010
        Em 2008, ocorreu uma crise financeira que foi um evento significativo que afetou a economia global. _"A crise financeira de 2008 ocorreu devido a uma bolha imobiliária nos Estados Unidos, causada pelo aumento nos valores imobiliários, que não foi acompanhado por um aumento de renda da população."_
        '''
        st.markdown(
        '<span class="small-font">Fonte: https://www.politize.com.br/crise-financeira-de-2008/',
        unsafe_allow_html=True
        )
        '''
        Analisando abaixo os valores para os principais exportadores ao longo dos anos, juntamente com linhas de tendência. Percebe-se que a crise global impactou negativamente as exportações, 
        exceto para Rússia e China, que tiveram alta em 2009.\n
       
        '''

        st.plotly_chart(
            plot_regressao_estimada(
                dataset_exportacao[dataset_exportacao['pais'].isin(exp_ordem_pareto)],
                'Valores de exportação para os principais países no período (US$)',
                int,
                exp_ordem_pareto

            ),
            use_container_width = True
        )

        '''
        Com a alta exportação para China e Rússia, o mercado de exportação de vinho brasileiro não refletiu a crise em 2009.
        Entretanto, em 2010 as exportações também caíram para esses países, resultando na queda dos valores em 2010.\n
        
        #### Crescimento das exportações para o Paraguai
        Nos gráficos acima também é possível perceber que as exportações para **Paraguai** vêm crescendo, principalmente a partir de 2014, ano no qual ultrapassa a Rússia como país 
        que mais importa vinho do Brasil. \n
        O interesse no Paraguai pelo vinho brasileiro vem aumentando. _"Com o sucesso dos vinhos doces e que a maior parte do mercado é de vinhos econômicos o vinho espumante brasileiro é considerado como um produto de boa qualidade e com demanda crescente, principalmente na fronteira 
        e existe a possibilidade de escalar os hábitos e o paladar de um segmento médio Premium que já consome vinhos brasileiros com frequência."_
        '''

        st.markdown(
        '<span class="small-font">Fonte: https://www.gov.br/empresas-e-negocios/pt-br/invest-export-brasil/exportar/conheca-os-mercados/pesquisas-de-mercado/estudo-de-mercado.pdf/Paraguai2021.pdf</span>',
        unsafe_allow_html=True
        )
        st.plotly_chart(
            plot_regressao1(
                dataset_exportacao.set_index('pais').query("pais=='Paraguai'").reset_index(),
                'Valores de exportação para Paraguai (US$)',
                int
            ),
            use_container_width = True
        )

        '''
        Essa tendência de aumento do interesse no vinho brasileiro por parte do Paraguai pode trazer benefícios significativos para ambos os países. Sendo positivo para o Brasil fortalecer as relações com esse país.\n\n
        Outras tendências identificadas são: a de aumento das exportações para **China** e a de estabilidade para **Estados Unidos** e **Reino Unido**.
        '''

        st.plotly_chart(
            plot_regressao1(
                dataset_exportacao.set_index('pais').query("pais=='China'").reset_index(),
                'Valores de exportação para China (US$)',
                int
            ),
            use_container_width = True
        )
        '''
        Apesar da China ficar atrás dos Estados Unidos no valor exportado, sua tendência de crescimento a torna um mercado interessante, e deve-se considerar investir mais nas exportações para esse país. _"O total das exportações (geral) do Brasil para a China em 2022 representou mais que o dobro do total embarcado para os Estados Unidos, o segundo maior destino das exportações brasileiras no ano passado."_
        '''
        st.markdown(
        '<span class="small-font">Fonte: https://investnews.com.br/economia/participacao-da-china-na-exportacao-do-brasil-cresceu-56-em-10-anos/#:~:text=As%20exportações%20do%20Brasil%20para,o%20Ministério%20das%20Relações%20Exteriores.</span>',
        unsafe_allow_html=True
        )
        st.markdown("---")
        st.markdown(
            """
            <style>
            .small-font {
             font-size: 12px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
        '''<span class="small-font">
            Para estimativa de Regressão foi utilizado para calcular o coeficientes do polinômio ajustado com a função polyfit do numpy para grau 1 que utiliza o método dos mínimos quadrados, que minimiza o erro quadrático.
             </span>''',
        unsafe_allow_html=True
        )
        st.markdown(
        '<span class="small-font">E = Σᵢ(yᵢ - p(xᵢ))² </span>',
        unsafe_allow_html=True
        )
        st.markdown(
        '<span class="small-font">p(x) = p[0] * xᵈᵉᵍ + p[1] * xᵈᵉᵍ⁻¹ + ... + p[deg-1] * x + p[deg] </span>',
        unsafe_allow_html=True
        )
    
    with tab4:
          
        '''

        Devido a mudança do perfil de exportação ao longo dos 15 anos e visando entender como está o comportamento em um período mais recente, é válido avaliar o gráfico de pareto para o período de 5 anos entre 2016 
        e 2021 abaixo.
        '''
        st.write("\n")
        st.markdown('###### Valor Total de Vendas por países responsáveis por até 90% da vendas no período de 2016 a 2021')
        st.plotly_chart(
            plot_pareto(
                dataset_exp_pareto_5.query("Porcentagem_acumulada_valor < 90").reset_index(),
                "Pais_destino",
                "Valor",
                "Pais_destino",
                "Porcentagem_acumulada_valor",
                "País",
                "Valor (U$)",
                dataset_exp_pareto_5.Valor.mean()
            ),  use_container_width = True
        )
        st.write("\n")

        '''        
        Nota-se um perfil muito diferente do observado para o período de 15 anos. Sendo a maior diferença a pouca expressividade da Rússia, confirmando a tendência de queda 
        observada nos gráficos anteriores.\n
        Uma novidade que aparece no perfil mais recente é o **Haiti**, que aparece como um dos países do grupo com 80% da influência no valor exportado, ultrapassando o Reino Unido. 
        Dando um pouco mais de atenção a esse país, abaixo encontra-se o gráfico dos valores exportados de vinho para Haiti ao longo dos 15 anos.
        '''

        st.plotly_chart(
            plot_regressao1(
                dataset_exportacao.set_index('pais').query("pais=='Haiti'").reset_index(),
                'Valores de exportação para Haiti (US$)',
                int
            ),
            use_container_width = True
        )
        
        '''      
        Observa-se que os valores das exportações para o Haiti apresentou uma grande crescente a partir de 2009. Sendo assim, Haiti é um país de que merece atenção dos investidores com 
        grande potencial de exportação para os próximos anos.

        _"Cada vez mais os empresários brasileiros começam a considerar as exportações como uma decisão estratégica importante para o desenvolvimento dos seus negócios.
        Os principais produtos brasileiros exportados para Haiti são em primeiro lugar - Produtos Alimentícios e Animais Vivos."_
        '''

        st.markdown(
        '<span class="small-font">Fonte: https://www.fazcomex.com.br/comexstat/america-central/exportacao-haiti/.</span>',
        unsafe_allow_html=True
        )
        st.markdown("---")
        st.markdown(
            """
            <style>
            .small-font {
             font-size: 12px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
        '''<span class="small-font">
            Para estimativa de Regressão foi utilizado para calcular o coeficientes do polinômio ajustado com a função polyfit do numpy para grau 1 que utiliza o método dos mínimos quadrados, que minimiza o erro quadrático.
             </span>''',
        unsafe_allow_html=True
        )
        st.markdown(
        '<span class="small-font">E = Σᵢ(yᵢ - p(xᵢ))² </span>',
        unsafe_allow_html=True
        )
        st.markdown(
        '<span class="small-font">p(x) = p[0] * xᵈᵉᵍ + p[1] * xᵈᵉᵍ⁻¹ + ... + p[deg-1] * x + p[deg] </span>',
        unsafe_allow_html=True
        )
        
    with tab5:

        '''
        ##### Valores por país dos que mais importamos vinhos

        ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
        '''

        st.plotly_chart(
            plot_pareto(
                dataset_imp_pareto.query("Porcentagem_acumulada_valor < 99 or Porcentagem_acumulada_quantidade < 99"),
                "Pais_destino",
                "Valor",
                "Pais_destino",
                "Porcentagem_acumulada_valor",
                "País",
                "Valor (US$)",
                 dataset_imp_pareto.Valor.mean()
            ),  use_container_width = True
        )
        '''
        Analisando os dados sobre as importações no mesmo período através do gráfico de pareto acima, identificam-se os países dos quais mais importamos vinho. 
        '''
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_importacao[dataset_importacao['pais'].isin(imp_ordem_pareto)],
                'Valores de importação para os principais países (US$)',
                int,
                imp_ordem_pareto
            ),
            use_container_width = True
        )
       
        '''
        A análise individual da importação desses países ao longo do período é importante para compreender a relação entre importação e exportação, revelando uma correlação negativa entre esses dois fluxos.
        No Brasil consome-se mais vinhos desses países do que eles consomem vinhos brasileiros, o que pode ser atribuído principalmente à tradição e qualidade na fabricação deles.\n
        Dessa lista, vale aprofundar a análise para os Estados Unidos. Apesar de ser um país responsável uma parte das importações, também desempenha um papel significativo como destino de exportação. 
        O mercado dos Estados Unidos é tão essencial que seria inadequado excluí-lo da análise final.
        '''
        st.plotly_chart(
            plot_comparacao(
                dataset_exportacao.query("pais == 'Estados Unidos'"),
                dataset_importacao.query("pais == 'Estados Unidos'"),
                'Exportação',
                'Importação',
                'Valores de Exportação e Importação Estados Unidos (US$)',
                int,
                'Estados Unidos'
            ),
            use_container_width = True
        )

        
        st.markdown("---")
        st.markdown(
            """
            <style>
            .small-font {
             font-size: 12px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
        '''<span class="small-font">
            Para estimativa de Regressão foi utilizado para calcular o coeficientes do polinômio ajustado com a função polyfit do numpy para grau 1 que utiliza o método dos mínimos quadrados, que minimiza o erro quadrático.
             </span>''',
        unsafe_allow_html=True
        )
        st.markdown(
        '<span class="small-font">E = Σᵢ(yᵢ - p(xᵢ))² </span>',
        unsafe_allow_html=True
        )
        st.markdown(
        '<span class="small-font">p(x) = p[0] * xᵈᵉᵍ + p[1] * xᵈᵉᵍ⁻¹ + ... + p[deg-1] * x + p[deg] </span>',
        unsafe_allow_html=True
        )
    with tab6:
        st.markdown('### Dados Econômicos - Banco Mundial')
        '''
        ##### Dados dos países que mais impactam na exportação de vinhos

        ***Valores correspondentes ao período de 15 anos entre 2007 a 2021***
        '''

        st.plotly_chart(
            plot_regressao_estimada(
                dataset_pib[dataset_pib['pais'].isin(ordem)],
                'PIB (US$)',
                float,
                ordem
            ),
            use_container_width = True
        )

        '''
        Avaliando o PIB desses países, nota-se que todos têm uma linha de crescimento nesse período. O que é positivo para o cenário futuro de exportações.
        '''
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_inflation[dataset_inflation['pais'].isin(ordem)],
                'Inflação (%)',
                float,
                ordem
            ),
            use_container_width = True
        )

        '''        
        Em relação à inflação, observa-se uma tendência de queda nos países, com exceção do Haiti. Contudo no último ano, o Haiti também registrou queda. 
        Embora tenha havido um aumento após a pandemia de Covid-19, a maioria dos países da lista tem demonstrado uma trajetória decrescente da inflação ao longo do tempo. 
        O que é um bom indicador para as perspectivas de vendas futuras. 
        '''
        st.plotly_chart(
            plot_regressao_estimada(
                dataset_trade[dataset_trade['pais'].isin(ordem)],
                'Índice de Comércio internacional',
                float,
                ordem
            ),
            use_container_width = True
        ) 

        '''
        O período de pandemia também impactou a relação comercial entre países. No entanto, em 2021, observamos uma melhora em alguns países, exceto no Reino Unido e Haiti. 
        Embora não tenhamos observado um aumento nesses casos específicos, é importante lembrar que ambos têm um bom histórico nas exportações de vinho e crescimento do PIB. 
        Indicando assim perspectivas positivas para o futuro também nesses países.
        '''
        st.write("\n")
        st.write("\n")
        st.markdown('### Consumo de álcool - WHO/OIV')

        '''
        ##### Valores de consumo de vinho e álcool dos países que mais impactam na exportação de vinhos
        '''

        st.plotly_chart(
            plot_regressao_estimada(
                dataset_consumo_vinho[dataset_consumo_vinho['pais'].isin(ordem)],
                'Consumo de vinho (10³ L)',
                int,
                ordem
            ),
            use_container_width = True
        )
        '''
        Com a análise dos gráficos acima, nota-se que os dados da Organização Internacional de Vinha e Vinho apresentam um aumento de consumo de vinho no último ano com exceção da China.\n
        '''

        '''
        ***Valores sobre o consumo de álcool correspondentes ao fato e projeção com intervalo de confiança de 95% para os anos de 2020 e 2025***
        '''

        st.plotly_chart(
            plot_consumo_projetado(
                dataset_consumo[dataset_consumo['pais'].isin(ordem)],
                'Diferença entre valor projetado para 2025 e valor real em 2020 do consumo de álcool per capita (L)',
                ordem
            ),
            use_container_width = True
        )

        '''
        As projeções acima foram feitas com dados disponíveis no **World Health Organization**, que mostram a diferença entre o valor da projeção para 2025 e valor real observado em 2020.
        Analisando os dados de projeção de consumo de álcool para 2025 em conjunto com os de consumo de vinho, espera-se um aumento no consumo de vinho para 2025.
        
        
        '''

        st.markdown("---")
        st.markdown(
            """
            <style>
            .small-font {
             font-size: 12px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            '''<span class="small-font">
            Para estimativa de Regressão foi utilizado para calcular o coeficientes do polinômio ajustado com a função polyfit do numpy para grau 1 que utiliza o método dos mínimos quadrados, que minimiza o erro quadrático.
             </span>''',
            unsafe_allow_html=True
        )
        st.markdown(
            '<span class="small-font">E = Σᵢ(yᵢ - p(xᵢ))² </span>',
        unsafe_allow_html=True
        )
        st.markdown(
            '<span class="small-font">p(x) = p[0] * xᵈᵉᵍ + p[1] * xᵈᵉᵍ⁻¹ + ... + p[deg-1] * x + p[deg] </span>',
        unsafe_allow_html=True
        )

    with tab7:
        
        '''
        #### Conclusões da análise
        
        Primeiramente, é fundamental ressaltar que a situação geopolítica tem um impacto significativo no comércio internacional, e o setor vinícola não é exceção. 
        Tensões políticas e conflitos podem conduzir a restrições comerciais, tarifas altas e, em algumas situações, até a embargos totais. 
        Além disso, essas circunstâncias podem desestabilizar a economia de um país, influenciando a demanda por produtos importados como o vinho.

        Com a análise dos dados de exportação, principalmente financeiros, notamos que, apesar da crise global em 2019-2020 devido à Covid-19,
        observamos um cenário favorável para a economia em 2021, principalmente em alguns países na exportação de vinhos.\n
        Montamos uma lista dos países mais favoráveis para a exportação de vinhos brasileiros nos próximos anos:

        - **Paraguai**        
        - **Estados Unidos**
        - **China**
        - **Haiti**
        - **Reino Unido**
        - **Rússia**

        Mesmo com uma queda na exportação nos últimos anos, a Rússia detém um mercado muito importantes para exportação em um nível global.\n
        No contexto do conflito russo-ucraniano que se iniciou em 2022, a exportação de vinhos para esse país pode se tornar uma tarefa complexa. 
        Desafios logísticos como restrições de transporte e bloqueios podem se apresentar como obstáculos significativos. \n
        Entretanto, informações recentes divulgadas pela imprensa portuguesa apontam que a Rússia triplicou a importação de vinhos portugueses*. 
        Isso reforça a importância do Brasil considerar o fortalecimento das exportações de vinhos para esse mercado. Além disso, o histórico de 
        exportações entre 2007 e 2021 mostra que a Rússia teve uma resposta positiva aos vinhos brasileiros, especialmente em 2013, sendo uma boa janela 
        de oportunidade.\n
        Além disso tanto Rússia, como Reino Unido têm um aumento projetado no consumo de álcool para 2025, e ambos estão em crescimento no consumo de vinho nos últimos anos, 
        sendo mercados com importância global para o comércio.\n
        A China, apesar de ter uma queda na exportação de vinho em 2021, é um país com um mercado de grande potencial a ser explorado. Apresenta um aumento 
        histórico no PIB e queda histórica na inflação, mesmo durante a Covid-19.\n
        Expandindo a análise para outras esferas da geopolítica, as tensões entre China e EUA também podem criar tanto oportunidades quanto desafios para 
        o Brasil. Os EUA têm mostrado uma tendência de crescimento na importação e consumo de bebidas alcoólicas, incluindo o vinho. Por outro lado, um 
        documentário recente destacou o crescimento do setor vinícola chinês com foco na exportação**. \n
        O Paraguai é um país de fronteira e com um paladar que propicia a exportação de vinhos brasileiros, que indica porque é um país que está no topo 
        de importação de vinhos brasileiros, sendo um mercado muito promissor.\n
        O Haiti é um país que, apesar de ter um clima mais quente, teve o maior aumento na exportação de vinhos brasileiros. É o país com o maior aumento histórico do PIB da lista, 
        mesmo com a Covid-19. De acordo com a OMS e a OIV é projetado um aumento no consumo de álcool e um aumento histórico no consumo de vinho, tendo assim 
        o ótimo mercado a ser explorado.\n
        Por fim, é essencial lembrar que estes são apenas cenários hipotéticos, e a realidade pode divergir dependendo de uma ampla variedade de fatores. A geopolítica global é uma 
        tapeçaria complexa e imprevisível, é preciso que estejamos preparados para nos adaptar rapidamente às mudanças no mercado.

        '''
        st.markdown("---")
        st.markdown(
        '<span class="small-font">*https://www.dinheirovivo.pt/economia/exportacoes-de-vinho-para-a-russia-e-a-ucrania-quase-duplicaram-no-primeiro-trimestre-16359199.html',
        unsafe_allow_html=True
        )
        st.markdown(
        '<span class="small-font">**https://exame.com/casual/a-china-e-a-proxima-superpotencia-do-vinho-documentario-tenta-responder/',
        unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()