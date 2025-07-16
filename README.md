# 🚀 Gerador de Conteúdo Blockchain com IA

Este projeto utiliza a LLM **LLaMA 3 - 70B** via **LangChain + Groq** para gerar conteúdo estratégico voltado ao ecossistema blockchain, como:

- Publicações técnicas para LinkedIn, Medium e blogs;
- Explicações de conceitos Web3;
- Promoções de produtos como tokens, DApps e contratos inteligentes;
- Geração de conteúdo com SEO e CTA.

## 🧠 Tecnologias

- Python
- [Streamlit](https://streamlit.io)
- LangChain
- [Groq API](https://console.groq.com/)
- dotenv

## 📦 Instalação

1. Instalação de bibliotecas:
```bash
  pip install langchain langchain-community langchain-groq
```
2. Instalação do Streamlit:
```bash
pip install streamlit
```
3. Para armazenamento das chaves:
```bash
pip install python-dotenv
```
4. Criação do arquivo de ambiente: .env (o conteúdo será a API KEY):
```bash
GROQ_API_KEY="SUA CHAVE AOI AQUI"
```
<img src="/imagens/env.png" alt="Arquivo .env" width="300"/>
5. Rodar no Streamlit pelo comando:
```bash
streamlit run app.py
```
6. Acessar as URLs disponíveis no terminal (Local ou Nettwork)

## 📌 Exemplo de Uso
**Selecione**:
- Tópico Blockchain: Smart Contracts na Ethereum
- Canal de distribuição: LinkedIn
- Estilo de conteúdo: Técnico
- Nível de profundidade: Explicativo
- Perfil do leitor: Desenvolvedores
- Keywords (SEO): solidity, ethereum, contratos inteligentes

**Clique em "Gerar Conteúdo" e pronto!**

## 🧑‍🏫 Imagem do Aplicativo
<img src="imagens/tela_inicial.png" alt="Tela Inicial" width="600"/>
