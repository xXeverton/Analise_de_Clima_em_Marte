# 🚀 Análise do Clima em Marte com a API da NASA

Este projeto faz parte do desafio técnico da Aleon e consiste na análise de dados meteorológicos de Marte, coletados pela sonda InSight da NASA.

## 🔍 Objetivo

- Consumir a API da NASA
- Tratar os dados meteorológicos
- Criar visualizações e gerar insights sobre o clima marciano

## 📊 O que foi feito

- Extração de dados via API (InSight Weather)
- Limpeza e organização dos dados
- Visualizações sobre:
  - Temperatura média
  - Pressão atmosférica
  - Velocidade dos ventos
- Análise descritiva com insights

## 🛠️ Tecnologias e Bibliotecas

- Python
- Jupyter Notebook
- requests, pandas, matplotlib, seaborn

## 🚀 Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Crie e ative o ambiente virtual:
    ```bash
    python -m venv venv
    venv\\Scripts\\activate  # Windows
    source venv/bin/activate  # Linux/Mac
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Abra o Jupter Notebook:
    ```bash
    jupyter notebook
    ```

## 📌 Conclusões
- A temperatura média em Marte é extremamente baixa, com variações entre -63°C e -62°C nos últimos sols registrados.
- A pressão atmosférica permanece consistentemente baixa, como esperado para o ambiente marciano.
- A velocidade do vento varia, mas geralmente está entre 5–8 m/s.
- A regressão linear indica uma leve tendência de resfriamento nos últimos dias analisados, possivelmente associada à mudança de estação.
- O mapa de correlação mostra uma relação direta entre temperatura mínima, média e máxima, como esperado. A pressão e o vento não demonstram correlação forte com outras variáveis nesse intervalo de dados.