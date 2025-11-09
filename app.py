import streamlit as st
import os
import re  # Importado para a Ideia 2
from dotenv import load_dotenv
from openai import OpenAI 

# --- Apenas estilo (Carrega seu arquivo style.css) ---
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Arquivo 'style.css' não encontrado. Os estilos personalizados não serão aplicados.")

# --- Carregar Chaves de API ---
load_dotenv() 
# Lendo a chave HF_TOKEN
api_token = os.getenv("HF_TOKEN")

if api_token is None:
    try:
        # Lendo a chave HF_TOKEN do secrets.toml
        api_token = st.secrets["HF_TOKEN"] 
    except KeyError:
        st.error("Chave HF_TOKEN não encontrada. Configure no .streamlit/secrets.toml")
        st.stop()

# --- Configuração do Cliente de IA ---
try:
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=api_token
    )
except Exception as e:
    st.error(f"Falha ao criar o cliente OpenAI. Erro: {e}")
    st.stop()

# O nome do modelo usado no Hugging Face
MODELO = "HuggingFaceH4/zephyr-7b-beta:featherless-ai"

# --- Função para chamar a IA (com limpeza de string) ---
def gerar_recomendacao(fome):     
    
    prompt_sistema = """Você é o "Agente iFood", um assistente de IA amigável e criativo. 
    Sua missão é dar 3 sugestões de pratos baseadas no pedido do usuário.
    Seja breve, animado e use emojis 🍔🍕🍣.
    
    Responda *exatamente* no seguinte formato de lista numerada:
    1. [Nome do Prato] - [Breve descrição]
    2. [Nome do Prato] - [Breve descrição]
    3. [Nome do Prato] - [Breve descrição]
    
    Não adicione *nenhum* texto antes ou depois da lista (como "Aqui estão..." ou "Agente iFood:")."""
    
    prompt_usuario = f"Pedido do usuário: {fome}"

    try:
        
        completion = client.chat.completions.create(
            model=MODELO, 
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
            max_tokens=250, 
            temperature=0.7,    

            # Lista 'stop' simplificada (removemos os tokens de "início")
            stop=["<|user|>", "[/INST]", "Pedido do usuário:", "Agente iFood:"]
        )
        
        # Pega a resposta da IA
        resposta_ia = completion.choices[0].message.content

        # Limpeza manual do "lixo" do início (como [ASS], <|system|>, etc.)
        lixo_para_limpar = ["<|system|>", "<|assistant|>", "[ASS]"]
        for item in lixo_para_limpar:
            if resposta_ia.startswith(item):
                resposta_ia = resposta_ia.replace(item, "", 1) 
        
        return resposta_ia.strip()
    
    except Exception as e:
        st.warning(f"A IA está processando... Se demorar, tente de novo em 20s.")
        st.error(f"Detalhe do erro: {e}")
        return "O Agente iFood (IA) está 'aquecendo os motores'! 🤖 Por favor, tente novamente em 20 segundos."

# --- Função para Formatar a Resposta ---
def formatar_resposta(recomendacao_texto):
    """
    Usa RegEx para encontrar itens de lista ("1. ...") 
    e exibi-los em caixas st.success separadas.
    """
    sugestoes = re.findall(r"(\d\.\s)(.*)", recomendacao_texto)

    if sugestoes:
        st.subheader("Aqui estão 3 ideias para você:")
        for item in sugestoes:
            st.success(f"{item[0]} {item[1]}")
    else:
        st.subheader("Aqui está uma ideia para você:")
        st.warning("A IA não formatou a resposta como uma lista. Mostrando texto puro:")
        st.markdown(recomendacao_texto)

# --- Configuração da Página ---
st.set_page_config(
    page_title="Agente iFood",
    page_icon="🚀"
)

# ######################################################
# --- CONTEÚDO DO APP (COM A LÓGICA CORRIGIDA) ---
# ######################################################

st.title("Agente de Recomendação")
st.title("ifood") 
st.header("Qual a sua fome hoje?")

# --- ETAPA 1: DEFINIR OS INPUTS ---

# O input de texto vem PRIMEIRO
fome_do_usuario = st.text_input(
    "Descreva o que você gostaria de comer (ex: 'algo doce', 'um lanche barato', 'comida italiana'):"
)

# Variável para guardar qual prompt será enviado para a IA
prompt_final_para_ia = None

# O botão principal usa o texto do input
if st.button("Sugerir Cardápio!"):
    prompt_final_para_ia = fome_do_usuario

st.write("Ou escolha uma sugestão rápida:")
col1, col2, col3 = st.columns(3)

# Botões rápidos agora também definem o prompt_final_para_ia
with col1:
    if st.button("Algo leve 🥗"):
        prompt_final_para_ia = "Algo leve e saudável"

with col2:
    if st.button("Tô com pressa 🏃"):
        prompt_final_para_ia = "Uma comida rápida e prática"

with col3:
    if st.button("Me surpreenda! ✨"):
        prompt_final_para_ia = "Me surpreenda com uma sugestão criativa"

# --- ETAPA 2: PROCESSAR A IA (SE UM BOTÃO FOI CLICADO) ---

# Esta lógica agora roda se *qualquer* um dos 4 botões for clicado
if prompt_final_para_ia is not None:
    if not prompt_final_para_ia.strip(): # Checa se o prompt não está vazio
        st.error("Por favor, me diga o que você quer comer primeiro.")
    else:
        # Se um botão foi clicado E o prompt não está vazio, rode a IA
        with st.spinner("O Agente iFood está pensando na sugestão perfeita... 👨‍🍳"):
            recomendacao = gerar_recomendacao(prompt_final_para_ia)
            
            if recomendacao: 
                formatar_resposta(recomendacao)
            else:
                st.error("A IA não retornou uma resposta. Tente novamente.")