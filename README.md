# Tech_Challenge_Fase1
### Analise de dados de exportação de vinhos do Brasil para outros países.

> Para visualizar as analises em localhost run
>> **streamlit run Tech_Challenge.py**

## Libs

- pip install pandas
- pip install numpy
- pip install matplotlib
- pip install seaborn
- pip install plotly-express
- pip install plotly
- pip install streamlit 
- pip install openpyxl
- pip install python-math

## Dados usados no período entre 2007 e 2021

- ExpVinho.csv
  - Dados de exportação de vinhos
  - <http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06>

    Países   | Quantidade(Kg) | Valor(US$)
    :---------: | :------: | :-----:
    Africa do Sul | 859.169  | 2.508.140
  
- ImpVinhos.csv
  - Dados de importação de vinhos
  - <http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05>
  
    Países   | Quantidade(Kg) | Valor(US$)
    :---------: | :------: | :-----:
    Afeganistão | 11  | 46

- GPD.xlsx
  - Dados do Produto Interno Bruto (PIB) dos países
  - <https://data.worldbank.org/indicator/NY.GDP.MKTP.CD>
  
    Países   | 2007 | 2008 | 2009
    :---------: | :------: | :-----: | :-----:
    Afghanistan | 9,715,761,649.8  | 10,249,767,311.2 | 12,154,835,707.9

- Inflation.xlsx
  - Dados da taxa de inflação anual dos países
  - <https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG>
  
    Series Name | Series Code | Country Name | Country Code | 2007 [YR2007]
    :---------: | :------: | :-----: | :-----: | :-----:
    Inflation, consumer prices (annual %) | FP.CPI.TOTL.ZG  | Afghanistan | AFG | 8,68057078513406

- Trade.xlsx
  - Dados da proporção do comércio internacional em relação ao Produto Interno Bruto (PIB) dos países.
  - <https://data.worldbank.org/indicator/NE.TRD.GNFS.ZS>
  
    Series Name | Series Code | Country Name | Country Code | 2007 [YR2007]
    :---------: | :------: | :-----: | :-----: | :-----:
    Trade (% of GDP) | NE.TRD.GNFS.ZS  | Albania | ALB | 83,2020801053931

- Population.xlsx
  - Dados do número total de pessoas nos países
  - <https://data.worldbank.org/indicator/SP.POP.TOTL>
  
    Series Name | Series Code | Country Name | Country Code | 2007 [YR2007]
    :---------: | :------: | :-----: | :-----: | :-----:
    Population, total | SP.POP.TOTL  | Afghanistan | AFG | 25903301

- Unemployment.xlsx
  - Dados de desemprego total dos países
  - <https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS>  

    PSeries Name | Series Code | Country Name | Country Code | 2007 [YR2007]
    :---------: | :------: | :-----: | :-----: | :-----:
    Unemployment, total (% of total labor force) (modeled ILO estimate) | SL.UEM.TOTL.ZS  | Afghanistan | AFG | 8,108

- World Happiness Report
  - <https://www.kaggle.com/datasets/unsdsn/world-happiness>
  - 2015.csv
  - 2016.csv
  - 2017.csv
  - 2018.csv
  - 2019.csv