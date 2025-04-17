import streamlit as st
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Configuração da página
st.set_page_config(page_title="Clima em Marte", layout="centered")
st.title("🌌 Análise do Clima em Marte - NASA InSight API")

# 🌌 CSS para imagem de fundo e conteúdo legível
import streamlit as st
import base64

# Função para converter a imagem para base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Caminho da imagem local
image_base64 = get_base64_image("src/marte.webp")

# CSS para definir o fundo com a imagem
# CSS atualizado para melhor contraste e legibilidade
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("data:image/webp;base64,{image_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }}

        .block-container {{
            background-color: rgba(0, 0, 0, 0.7); /* Fundo escuro translúcido */
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }}

        h1, h2, h3, h4 {{
            color: #F9F9F9;
            text-shadow: 1px 1px 2px black;
        }}

        .stDataFrame, .stTable {{
            background-color: rgba(255, 255, 255, 0.95) !important;
            color: black !important;
            border-radius: 0.5rem;
        }}

        .stMarkdown p {{
            color: #F1F1F1;
            font-size: 1rem;
            text-shadow: 1px 1px 2px black;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# Carrega chave da API
load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")
URL = f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0"

@st.cache_data
def carregar_dados():
    response = requests.get(URL)
    data = response.json()
    sols = list(data.get("sol_keys", []))
    mars_weather = []

    for sol in sols:
        sol_data = data[sol]
        try:
            mars_weather.append({
                "sol": int(sol),
                "min_temp": sol_data["AT"]["mn"],
                "max_temp": sol_data["AT"]["mx"],
                "avg_temp": sol_data["AT"]["av"],
                "wind_speed": sol_data["HWS"]["av"],
                "pressure": sol_data["PRE"]["av"],
                "season": sol_data["Season"]
            })
        except KeyError:
            continue

    df = pd.DataFrame(mars_weather)
    df = df.sort_values("sol")
    return df

df = carregar_dados()

# 📄 Dados Meteorológicos
st.subheader("📄 Dados Meteorológicos de Marte")
st.dataframe(df)

# 📊 Estatísticas
st.subheader("📊 Estatísticas Descritivas")
st.dataframe(df.describe())
st.markdown("> *Um resumo dos dados coletados em diferentes 'sols' revela a hostilidade do ambiente marciano. Temperaturas baixíssimas, baixa pressão e ventos constantes destacam os desafios para qualquer presença humana.*")

# 🌡️ Temperatura Média
st.subheader("🌡️ Temperatura Média por Sol")
fig1, ax1 = plt.subplots()
sns.lineplot(x="sol", y="avg_temp", data=df, marker="o", ax=ax1, color="orangered")
ax1.set_title("Temperatura Média em Marte (°C)")
ax1.set_xlabel("Sol")
ax1.set_ylabel("Temperatura Média (°C)")
st.pyplot(fig1)
st.markdown("> *As temperaturas médias são extremamente frias, mesmo nos períodos menos rigorosos. Isso reforça como Marte exige tecnologias avançadas de aquecimento para futuras missões.*")

# 🌬️ Pressão Atmosférica
st.subheader("🌬️ Pressão Atmosférica por Sol")
fig2, ax2 = plt.subplots()
sns.barplot(x="sol", y="pressure", data=df, hue="sol", ax=ax2, palette="Blues_d", legend=False)
ax2.set_title("Pressão Atmosférica Média (Pa)")
ax2.set_xlabel("Sol")
ax2.set_ylabel("Pressão (Pa)")
st.pyplot(fig2)
st.markdown("> *A atmosfera rarefeita de Marte, refletida em pressões muito baixas, é uma das maiores barreiras à habitabilidade. Esses dados evidenciam o quanto é necessário pressurizar abrigos humanos.*")

# 💨 Velocidade do Vento
st.subheader("💨 Distribuição da Velocidade do Vento")
fig3, ax3 = plt.subplots()
sns.boxplot(data=df["wind_speed"], ax=ax3, color="skyblue")
ax3.set_title("Distribuição da Velocidade do Vento (m/s)")
ax3.set_xlabel("Velocidade do Vento")
st.pyplot(fig3)
st.markdown("> *Apesar da atmosfera fina, os ventos em Marte são capazes de movimentar grandes quantidades de poeira, causando tempestades globais. A distribuição mostra ventos intensos e regulares.*")

# 📈 Regressão Linear
st.subheader("📈 Tendência de Temperatura (Regressão Linear)")
fig4, ax4 = plt.subplots()
sns.regplot(x="sol", y="avg_temp", data=df, ax=ax4, color="tomato", marker="o", ci=None)
ax4.set_title("Tendência de Temperatura Média")
ax4.set_xlabel("Sol")
ax4.set_ylabel("Temperatura Média (°C)")
st.pyplot(fig4)
st.markdown("> *A análise de tendência mostra uma leve queda nas temperaturas, o que pode indicar mudanças sazonais no clima marciano. Uma observação valiosa para planejamentos de longa duração.*")

# 🔗 Correlação
st.subheader("🔗 Correlação entre Variáveis Meteorológicas")
fig5, ax5 = plt.subplots()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax5)
ax5.set_title("Mapa de Correlação")
st.pyplot(fig5)
st.markdown("> *Existe uma forte correlação entre temperaturas mínimas e máximas, como esperado. Essa relação ajuda a prever a variabilidade térmica durante o dia marciano.*")

# 📌 Conclusões
st.markdown("""
---
📌 **Conclusões**:
- A temperatura média em Marte mostra uma leve tendência de queda nos últimos sols.
- A pressão atmosférica se mantém consistentemente baixa.
- Os ventos são fortes e constantes, reforçando o papel das tempestades de poeira.
- A regressão linear evidencia mudanças sazonais possíveis.

🛰️ *Fonte: NASA InSight Weather Service API*  
👨‍💻 *Desenvolvido com 💙 por Everton Pereira Militão usando Streamlit, Seaborn e Python*
""")
