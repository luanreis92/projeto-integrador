# Projeto Integrador - Grupo 10

## Tema: Segurança Cibernética

## Integrantes
- Gabriel Oliveira Silva
- Luan Vinicius Soares dos Reis
- Luanda da Silva
- Lucas Ferreira Vaz Almeida
- Márcio dos Santos

## Descrição do contexto
A base de dados que será trabalhada é a base Data Breaches disponível no Kagle. A base traz dados de diversas fontes (reportagens, comunicados de imprensa governamental e artigos de notícias tradicionais) detalhando vazamento de dados e inclui os eventos envolvendo o roubo ou comprometimento de aproximadamente 30.000 regiatros. Tem 7 coluna divididas em: entidade, ano, número de registros envolvidos na violação, tipo de organização, metódo e fonte. Contem um total de 352 linhas.

## Objetivo
Analisar o panorama histórico de violações de dados para identificar quais setores da economia são mais vulneráveis e quais métodos de ataque apresentam maior frequência e severidade ao longo dos anos.

## Planejamento
- Criar repositório no GitHub - Luan
- Escolher base de dados - todos os integrantes
- Definir o objetivo - todos os integrantes
- Dividir as tarefas do grupo e criar o cronograma - Luanda
- Escolher os tratamentos - Luanda
- Planejamento do dashboard - Luan

## Cronograma
- Escolher a base de dados e objetivos - 03/março
- Dividir as tarefas do grupo - 06/março
- Escolher os tratamentos - 10/março
- Planejamento do dashboard - 16/março
- Criar repositório no Github - 19/março
- Entrega da primeira parte do projeto - 22/março

## Tratamentos
1. Tratamento de nulos nas colunas "Records", "Method" e "Sources". Como são apenas 2 linhas, serão excluídos.
2. Quantificar dados duplicados, excluir cópias desnecessárias.
3. Excluir as linhas em "Records" que possuem strings e não números inteiros. Exemplo: 19 years of data
4. Excluir as colunas "Sources" e "Entity" que não são necessárias para essa análise
5. Padronizar as colunas "Organization type" e "Method" para classificações mais gerais e melhorar a visualização dos gráficos

## Dashboard
- Média: média de quantidade vazada por evento
- Gráfico de pizza: dos tipos de organização 
- Gráfico de linha: frequência de vazamentos ao longo tempo
- Gráfico de barra vertical/horizontal: os 10 metódos que possuem um volume maior de vazamentos
- Heatmap: verificar as correlações
