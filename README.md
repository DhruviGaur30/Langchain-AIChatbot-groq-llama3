# 🤖 TechMind AI Chatbot

A beautifully designed, AI-powered chatbot interface built using **LangChain**, **Groq's Llama 3**, and **Streamlit**. TechMind is your futuristic, emoji-friendly AI assistant that helps you explore coding, AI, tech, and beyond — in a blazing-fast and interactive way!

---

## 🚀 Features

- ⚡ Powered by [Llama 3 on Groq](https://console.groq.com/) via OpenAI-compatible endpoint
- 🧠 Prompt engineering using LangChain's `ChatPromptTemplate`
- 🎨 Fully customized futuristic UI with CSS animations and glowing themes
- 📚 Chat history with sidebar preview
- 🔒 API key protection using `.env` file
- 🛠 Developed in **Python** and deployed using **Streamlit**

---

## 🧰 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Groq (OpenAI-compatible API)](https://console.groq.com/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)
- [tiktoken](https://github.com/openai/tiktoken)

---

## 📁 Project Structure

├── .env # 🔐 API keys (excluded from GitHub)
├── .gitignore # Files/folders to ignore
├── app.py # 🚀 Main Streamlit chatbot app
├── requirements.txt # 📦 Python dependencies
└── preview.png # 🖼️ Optional UI screenshot

---

---

## 🧪 Setup Instructions

### 1. 🔑 Get API Keys

- [Groq API Key](https://console.groq.com/)
- [LangChain API Key (optional)](https://smith.langchain.com/)

---

### 2. 📝 Create `.env` File

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_key  # Optional
```
### 3. 📦 Install Dependencies
```
pip install -r requirements.txt
```

### 4. 🚀 Run the App
```
streamlit run app.py
```
### 5. Requirements
```
langchain
langchain-openai
langchain-community
streamlit
python-dotenv
tiktoken
langchain-core
```
### 🙅 Security Notes
✅ .env is included in .gitignore (already done)

❌ Never push your API keys to GitHub

☁️ Use Streamlit secrets or deployment env variables when deploying

### 💡 Inspiration
This project merges conversational AI with aesthetic UI design to help devs and tech learners interact with a fun, fast, and powerful coding assistant.

### 📜 License
This project is licensed under the MIT License.

### 🧑‍💻 Author
Dhruvi Gaur – @DhruviGaur30
Made with 💜 using LangChain, Llama 3, Groq, and Streamlit.

