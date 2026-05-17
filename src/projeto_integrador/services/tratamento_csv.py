
import pandas as pd

def executar_pipeline():

#==================================================================================================================
# TRATAMENTO: ABERTURA DO ARQUIVO CSV, ENTENDIMENTO DO ESQUEMA E APLICAÇÕES DE TRATAMENTOS SOLICITADOS
#==================================================================================================================

    df = pd.read_csv("data/raw/base_data_breachs.csv")         #Função para ler o arquivo csv buscando da pasta (raw)

    df = df.drop(columns=["Sources", "Entity"])              #Excluidas as coluns Souces e Entity.
    print(df.duplicated().sum())                             # Não foi encontrados dados duplicados, então sem necessidade de drop_duplicate
    df = df.dropna(subset=["Records", "Method"])              # excluidos os nulos destas colunas, ao total 3 registros foram excluídos

    df["Records"] = pd.to_numeric(df["Records"], errors="coerce") #fiz a coersão de tipo pra transformar o diferente de numeros em Nan, e em seguida vou excluí-los
    df = df.dropna(subset=["Records", "Method"])    # aqui faço a exclusão de tudo que é Nan (Not A Number = não é número)
    print(df.head())
    df.info()                 #Mostra o schema completo:

# =========================================================
# PADRONIZAÇÃO DAS CATEGORIAS
# =========================================================

    df["Organization type"] = df["Organization type"].replace({
    "social networking": "social media",
    "social network": "social media",
    "tech": "technology",
    "web": "technology",
    "web, tech": "technology"
    })

    df["Method"] = df["Method"].replace({
    "hacked": "cyber attack",
    "poor security": "security failure"
    })

# =========================================================
# VALIDAÇÃO DA PADRONIZAÇÃO DE CATEGORIAS
# =========================================================
    print(df["Organization type"].unique())

    print(df["Method"].unique())


# =========================================================
# EXPORTAÇÃO DO NOVO DATA CSV NO DATA\CURATED
# =========================================================
    df.to_csv("data/curated/base_tratada.csv", index=False)

    print("CSV tratado salvo com sucesso!")