# 🚀 Análise do Clima em Marte com a API da NASA

Este projeto foi desenvolvido como parte do desafio técnico da Aleon. Ele realiza uma análise exploratória e visual do clima em Marte, utilizando dados da **sonda InSight** fornecidos pela **API pública da NASA**.

## 🌌 Visão Geral

A sonda InSight envia dados meteorológicos do planeta Marte, incluindo:
- Temperatura média diária
- Pressão atmosférica
- Velocidade dos ventos
- Estações marcianas

Com esses dados, foi criado:
- Um **notebook com análise descritiva**
- Um **dashboard interativo com Streamlit**

---

## 🎯 Objetivos

- Consumir a API pública da NASA
- Tratar e visualizar os dados meteorológicos marcianos
- Obter insights por meio de regressão e análise estatística
- Criar um painel interativo para visualização dos dados

---

## 📊 O que foi feito

- 🔎 Extração de dados via `InSight Weather API`
- 🧼 Limpeza e organização dos dados
- 📈 Visualizações com:
  - Temperatura média por sol
  - Pressão atmosférica
  - Distribuição da velocidade do vento
  - Regressão linear de temperatura
  - Mapa de correlação entre variáveis
- 📊 Estatísticas descritivas
- 🌐 Interface web com **Streamlit**

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Jupyter Notebook**
- **Streamlit**
- `requests`, `pandas`, `matplotlib`, `seaborn`, `python-dotenv`

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Defina sua chave da NASA

Crie um arquivo `.env` na raiz do projeto com:

```env
NASA_API_KEY=sua_chave_aqui
```

---

## 📗 Rodando o Notebook

```bash
jupyter notebook
```

Abra o arquivo `mars_analysis_final.ipynb` e execute.

---

## 🌐 Rodando a Interface Web

```bash
streamlit run app.py
```

Isso abrirá o painel interativo no navegador.

---

## 📌 Conclusões

- A temperatura média em Marte é extremamente baixa, com variações entre -63°C e -62°C.
- A pressão atmosférica permanece consistentemente baixa.
- Os ventos variam entre 5–8 m/s.
- A regressão linear indica uma leve tendência de queda de temperatura ao longo dos dias.
- A correlação mostra que variáveis de temperatura estão fortemente ligadas entre si, enquanto pressão e vento têm menos relação.

---

## 🛰️ Fonte dos Dados

[InSight: Mars Weather Service API (NASA)](https://api.nasa.gov/)

---

## 👨‍💻 Desenvolvido por Everton Pereira Militão

*com Python, ciência de dados e muita curiosidade espacial 🚀*
