# Projeto Integrador - Grupo 10

## Tema: Segurança Cibernética

## Integrantes
- Gabriel Oliveira Silva
- Luan Vinicius Soares dos Reis
- Luanda da Silva
- Lucas Ferreira Vaz Almeida
- Márcio dos Santos

## Descrição do contexto
A base de dados que será trabalhada é a base Data Breaches disponível no Kagle. A base traz dados de diversas fontes (reportagens, comunicados de imprensa governamental e artigos de notícias tradicionais) detalhando vazamento de dados e inclui os eventos envolvendo o roubo ou comprometimento de aproximadamente 30.000 registros. Tem 7 colunas, divididas em: entidade, ano, número de registros envolvidos na violação, tipo de organização, metódo e fonte. A base de dados contém um total de 352 linhas.

## Objetivo
Analisar o panorama histórico de violações de dados para identificar quais setores da economia são mais vulneráveis e quais métodos de ataque apresentam maior frequência e severidade ao longo dos anos.

## Planejamento
- Criar repositório no GitHub - Luan
- Escolher base de dados - todos os integrantes
- Definir o objetivo - todos os integrantes
- Dividir as tarefas do grupo e criar o cronograma - Luanda
- Planejamento do dashboard - Luan e Luanda
- Tratamento e carregamento de dados base para dashboard - Marcio
- Criação do dashboard - Gabriel e Lucas
- Publicação dashboard - Luanda e Luan

## Cronograma geral
- Escolha da base de dados e objetivos - 03/março
- Dividisão das tarefas do grupo - 06/março
- Escolha dos tratamentos - 10/março
- Planejamento da dashboard - 16/março
- Criação do repositório no Github - 19/março
- Entrega da primeira parte do projeto - 22/março
- Tratamentos - 15/março
- Dashboard - 17/março
- Publicação Streamlit - 18/março

## Status do Projeto

- [x] Estruturação inicial do projeto
- [x] Configuração do Poetry
- [x] Criação do ambiente virtual
- [x] Organização da arquitetura ETL
    - [x] Configuração do pandas

## Tratamentos

(Cronograma para efetuar os tratamentos)
1. Ler dataset ✅
2. Inspecionar estrutura ✅
3. Entender schema ✅
4. Regra de negocio na pasta src\projeto_integrador\service. - "Armazenamento do arquivo csv em: data\staging\Tratamento_BD_breachs.py"✅
5. Validar ✅
6. Viabilizar base tratada na pasta: data\curated\base_tratada.csv ✅

(Tratamentos finais exigidos)
1. Excluir as colunas "Sources" e "Entity" que não são necessárias para essa análise ✅
2. Quantificar dados duplicados, se houver; excluir cópias desnecessárias. ✅
3. Excluir nulos das colunas "Records" e "Method". Total de 3 registros forão excluídos. ✅ 
4. Excluir as linhas em "Records" que possuem strings e não números inteiros. Exemplo: 19 years of data ✅
5. Padronizar as colunas "Organization type" e "Method" para classificações mais gerais e melhorar a visualização dos gráficos ✅
6. Excluir as linhas em "Years" que possuem mais de 4 dígitos para manter apenas as linhas que possuem um ano específico. Total de 2 registros excluídos. ✅

### Comando para rodar o programa no terminal:
poetry run python -m src.projeto_integrador.main

### Próximos passos

- [x] Finalizar tratamento dos dados
- [x] Validar dados tratados
- [x] Integrar pipeline ao Streamlit
- [x] Criar visualizações

## Dashboard
- Média: média de quantidade de dados vazada por evento ✅
- Gráfico de pizza: dos tipos de organização ✅
- Gráfico de linha: frequência de vazamentos ao longo dos anos ✅
- Gráfico de barra vertical/horizontal: os 5 metódos que possuem um volume maior de vazamentos ✅
- Heatmap: verificar as correlações ✅
