🤖 TechMind AI Chatbot

A beautifully designed, AI-powered chatbot interface built using **LangChain**, **Mistral AI**, and **Streamlit**. TechMind is your futuristic, emoji-friendly AI assistant that helps you explore coding, AI, tech, and beyond in a fun and interactive way!

![TechMind Chatbot UI](./preview.png)

---

## 🚀 Features

- ⚡️ Powered by [Mistral 7B Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) via HuggingFace
- 🧠 Prompt engineering using LangChain's `ChatPromptTemplate`
- 🎨 Fully customized futuristic UI with CSS animations
- 📚 Chat history with sidebar navigation
- 🧪 API Key protection using `.env`
- 🛠 Developed in **Python** and deployed with **Streamlit**

---

## 🧰 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Mistral AI via HuggingFace](https://huggingface.co/mistralai)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)
- [tiktoken](https://github.com/openai/tiktoken) for token handling

---

## 📁 File Structure

```

├── .env                # API keys (should be excluded from GitHub)
├── .gitignore
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── preview\.png         # (Optional) UI screenshot

````

---

## 🧪 Setup Instructions

### 1. 🔑 Get API Keys

- [HuggingFace Token](https://huggingface.co/settings/tokens)
- [LangChain API Key](https://smith.langchain.com/)

### 2. 📝 Create `.env` File

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
LANGCHAIN_API_KEY=your_langchain_key
````

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. 🚀 Run the App

```bash
streamlit run app.py
```

---

## ✨ Screenshots

![Chat Interface](./preview.png)

> ✨ Beautifully styled messages with animated gradients and avatars
> 🎯 Sidebar with chat history and custom welcome animation

---

## 🧠 Prompt Design

This chatbot uses the following system message to set its tone:

```
You are TechMind, an advanced AI assistant. Be helpful, engaging, and tech-savvy. Use emojis to make responses fun and friendly!
```

---

## 📦 Requirements

```txt
langchain
langchain-openai
langchain-community
ollama
streamlit
python-dotenv
tiktoken
langchain-huggingface
langchain-core
```

---

## 🙅 Security Note

Make sure to:

* ✅ Add `.env` to your `.gitignore` file (already done)
* ❌ Never commit your API keys to the repo!

---

## 💡 Inspiration

This project blends conversational AI and aesthetic frontend design to help developers and tech learners chat with an intelligent assistant in a creative and comfortable space.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧑‍💻 Author

**Dhruvi Gaur** – [@DhruviGaur30](https://github.com/DhruviGaur30)
Made with 💜, LangChain, and Streamlit.

```

---

Let me know if you'd like to auto-generate a [preview.png UI screenshot](f), or want help writing a [deployment guide for Streamlit Cloud](f), or even a [LICENSE file](f)!
```
