# 🚀 Agente de Recomendação iFood (Projeto-Conceito)

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-API-yellow)

Um agente de IA para recomendação de pratos, desenvolvido como um estudo de caso da cultura de inovação e "fome de construir" do iFood.

---

## 🎯 Demo Interativa

Você pode testar o aplicativo em tempo real no link abaixo:

**[Clique aqui para acessar o Agente iFood](http://localhost:8501/)**


## 📸 GIF do App em Ação

*(**Ação Necessária:** Grave um GIF rápido (usando um app como ScreenToGif) mostrando você digitando uma fome, clicando no botão e recebendo a resposta. Depois, arraste o arquivo GIF para cá).*

[INSIRA UM GIF DA APLICAÇÃO AQUI]

---

## 💡 Contexto do Projeto

Este projeto foi desenvolvido em **16 dias** como parte do meu processo de candidatura para a vaga de Estágio em IA no iFood (novembro de 2025).

A vaga mencionava: *"Queremos ver o impacto das suas criações! Perfis no GitHub, projetos no Hugging Face, demos de desenvolvimentos... tudo isso vale muito mais do que certificados."*

Levei isso a sério. Em vez de apenas enviar um currículo, decidi construir uma solução que simula o ciclo de "experimentação rápida" e a "mentalidade de dono" valorizados pela empresa.

O objetivo foi criar uma demo funcional utilizando as tecnologias da vaga (IA, LLMs, Hugging Face) para demonstrar minha proatividade e alinhamento com a cultura do iFood.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com:

* **Linguagem:** Python
* **Framework Web:** Streamlit (para a criação rápida do frontend)
* **Inteligência Artificial:** Hugging Face API (Router), utilizando o modelo `HuggingFaceH4/zephyr-7b-beta`.
* **Estilização:** CSS personalizado para replicar a identidade visual do iFood.
* **Bibliotecas Python:** `openai` (para se conectar à API do HF), `dotenv`, `re`.

---

## ⚙️ Como Executar Localmente

Para rodar este projeto no seu computador, siga os passos:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/RoanOsorio03/referralAgentAi.git](https://github.com/RoanOsorio03/referralAgentAi.git)
    cd referralAgentAi
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # MacOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure suas chaves de API:**
    * Crie uma pasta `.streamlit` na raiz do projeto.
    * Dentro dela, crie um arquivo `secrets.toml`.
    * Adicione seu token do Hugging Face (com permissão `write`) ao arquivo:
        ```toml
        HF_TOKEN = "hf_SUA_CHAVE_SECRETA_AQUI"
        ```

5.  **Rode o aplicativo:**
    ```bash
    streamlit run app.py
    ```
