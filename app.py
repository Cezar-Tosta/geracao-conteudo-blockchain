import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv() # Lê o arquivo .env criado anteriormente

## conexão com a LLM
id_model = "llama3-70b-8192"
llm = ChatGroq(
    model=id_model,
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

## função de geração
def llm_generate(llm, prompt):
  template = ChatPromptTemplate.from_messages([
      ("system", "Você é um especialista em marketing técnico para projetos blockchain, com conhecimento em Web3, DeFi, NFTs, segurança e desenvolvimento de comunidades descentralizadas."),
      ("human", "{prompt}"),
  ])

  chain = template | llm | StrOutputParser()

  res = chain.invoke({"prompt": prompt})
  return res

st.set_page_config(page_title = "Gerador de conteúdo 🤖", page_icon="🤖")
st.title("Gerador de conteúdo")

# Campos do formulário
topic = st.text_input("Tópico Blockchain:", placeholder="Ex: Contratos Inteligentes, Ethereum, Segurança Web3, etc.")
platform = st.selectbox("Canal de Distribuição:", ['LinkedIn', 'Blog', 'Newsletter Técnica', 'Twitter (X)', 'Medium'])
tone = st.selectbox("Estilo de Conteúdo:", ['Técnico', 'Institucional', 'Educacional', 'Informal', 'Engajador'])
length = st.selectbox("Nível de Profundidade:", ['Resumo', 'Explicativo', 'Detalhado'])
audience = st.selectbox("Perfil do Leitor:", ['Desenvolvedores', 'Investidores', 'Geral', 'Clientes Coporativos', 'Público Interno'])
cta = st.checkbox("Incluir Chamada para Ação (CTA)")
hashtags = st.checkbox("Retornar Hashtags")
keywords = st.text_area("Palavras-chave (SEO):", placeholder="Ex: staking, layer2, defi security, NFT utility, etc.")

if st.button("Gerar conteúdo"):
  prompt = f"""
  Escreva um texto com SEO otimizado sobre o tema '{topic}'.
  Retorne em sua resposta apenas o texto final e não inclua ela dentro de aspas.
  - Onde será publicado: {platform}.
  - Estilo de Conteúdo: {tone}.
  - Perfil do Leitor: {audience}.
  - Nível de Profundidade: {length}.
  - {"Inclua uma chamada para ação clara." if cta else "Não inclua chamada para ação"}
  - {"Retorne ao final do texto hashtags relevantes." if hashtags else "Não inclua hashtags."}
  {"- Palavras-chave que devem estar presentes nesse texto (para SEO): " + keywords if keywords else ""}
  """
  try:
      res = llm_generate(llm, prompt)
      st.markdown(res)
  except Exception as e:
      st.error(f"Erro: {e}")