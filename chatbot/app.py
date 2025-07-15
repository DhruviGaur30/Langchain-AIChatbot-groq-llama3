from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables (only works locally)
load_dotenv()

# API Key handling - works both locally and in deployment
def get_api_key(key_name):
    """Get API key from Streamlit secrets first, then fallback to environment variables"""
    try:
        # Try Streamlit secrets first (for deployment)
        return st.secrets[key_name]
    except (KeyError, FileNotFoundError):
        # Fallback to environment variables (for local development)
        return os.getenv(key_name)

# Get API keys
GROQ_API_KEY = get_api_key("GROQ_API_KEY")
LANGCHAIN_API_KEY = get_api_key("LANGCHAIN_API_KEY")

# Page config
st.set_page_config(
    page_title="TechMind AI 🤖",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Animated background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 50%, rgba(0, 255, 255, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 50%, rgba(255, 0, 255, 0.1) 0%, transparent 50%);
        animation: pulse 4s ease-in-out infinite alternate;
        z-index: -1;
    }
    
    @keyframes pulse {
        0% { opacity: 0.3; }
        100% { opacity: 0.7; }
    }
    
    /* Hide default elements */
    .stDeployButton, #MainMenu, footer, header {
        display: none !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: rgba(15, 15, 35, 0.95) !important;
        backdrop-filter: blur(20px);
        border-right: 2px solid rgba(0, 255, 255, 0.3);
        width: 20rem !important;
    }
    
    /* Sidebar content positioning */
    .css-1d391kg .element-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        height: 100vh;
        padding: 1rem;
    }
    
    /* Main content adjustment - responsive to sidebar */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: none;
        transition: all 0.3s ease;
        margin-left: 0;
    }
    
    /* Adjust main content when sidebar is open */
    .css-1d391kg:not(.css-1lcbmhc) ~ .main .block-container {
        margin-left: 21rem;
        width: calc(100% - 21rem);
    }
    
    /* Welcome section */
    .welcome-hero {
        text-align: center;
        padding: 2rem 0 !important;
        margin: 0 auto;
        max-width: 600px;
        margin-bottom: 1rem !important;
    }
    
    .hero-avatar {
        width: 120px;
        height: 120px;
        background: linear-gradient(45deg, #00ffff, #ff00ff);
        border-radius: 50%;
        margin: 0 auto 2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        animation: float 3s ease-in-out infinite;
        box-shadow: 0 0 50px rgba(0, 255, 255, 0.5);
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.7);
        margin-bottom: 2rem;
    }
    
    /* Chat messages */
    .chat-msg {
        display: flex;
        margin: 1.5rem 0;
        gap: 1rem;
        align-items: flex-start;
    }
    
    .chat-msg.user {
        flex-direction: row-reverse;
    }
    
    .msg-avatar {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        flex-shrink: 0;
    }
    
    .msg-avatar.bot {
        background: linear-gradient(45deg, #000246, #B34DFF);
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
    }
    
    .msg-avatar.user {
        background: linear-gradient(45deg, #ff00ff, #ff0080);
        box-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
    }
    
    .chat-msg.bot .msg-bubble {
        max-width: 70%;
        padding: 1rem 1.5rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #00c6ff, #7f00ff) !important;
        border: none !important;
        color: white !important;
        box-shadow: 0 0 20px rgba(127, 0, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .msg-bubble:hover {
        background: rgba(255, 255, 255, 0.15);
        transform: translateY(-2px);
    }
    
    .msg-bubble p {
        margin: 0;
        color: white;
        line-height: 1.6;
    }
    
    /* Sidebar content */
    .sidebar-header {
        text-align: center;
        padding: 1rem;
        margin-bottom: 2rem;
        border-bottom: 1px solid rgba(0, 255, 255, 0.3);
    }
    
    .sidebar-logo {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .sidebar-title {
        font-size: 1.3rem;
        font-weight: 600;
        background: linear-gradient(45deg, #00ffff, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .history-item {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 255, 255, 0.2);
        border-radius: 8px;
        padding: 0.6rem;
        margin-bottom: 0.5rem;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .history-item:hover {
        background: rgba(0, 255, 255, 0.1);
        transform: translateX(3px);
        box-shadow: 0 3px 10px rgba(0, 255, 255, 0.2);
    }
    
    .history-text {
        color: rgba(255, 255, 255, 0.9);
        font-size: 0.85rem;
        display: block;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    
    .history-time {
        color: rgba(255, 255, 255, 0.4);
        font-size: 0.65rem;
        margin-top: 0.2rem;
    }
    
    /* Clear button */
    .stButton button {
        background: linear-gradient(45deg, #ff0080, #ff4040) !important;
        border: none !important;
        border-radius: 8px !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 0.6rem 1rem !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        font-size: 0.85rem !important;
        margin-top: 1rem !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 0, 128, 0.4) !important;
    }
    
    /* Chat input - perfectly centered */
    .stChatInput {
        display: flex !important;
        justify-content: center !important;
        margin-top: -2rem !important;
        margin-bottom: 3rem !important;
    }

    .stChatInput input {
        background: rgba(15, 15, 35, 0.9) !important;
        border: 2px solid rgba(0, 255, 255, 0.3) !important;
        border-radius: 25px !important;
        color: white !important;
        font-size: 1rem !important;
        padding: 1rem 2rem !important;
        width: 90% !important;
        max-width: 700px !important;
        backdrop-filter: blur(20px) !important;
        transition: all 0.3s ease !important;
    }

    .stChatInput input:focus {
        border-color: rgba(0, 255, 255, 0.6) !important;
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.3) !important;
    }

    .stChatInput input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    /* Content padding for fixed input */
    .main-content {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        min-height: auto !important;
    }
    
    /* Responsive sidebar adjustment */
    .stChatInput {
        width: 95% !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
    }
</style>
""", unsafe_allow_html=True)

# Check if Groq API key is available
if not GROQ_API_KEY:
    st.error("🚨 GROQ_API_KEY not found! Please add it to your Streamlit secrets or .env file")
    st.stop()

# Optional: LangChain tracing
if LANGCHAIN_API_KEY:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

if "llm" not in st.session_state:
    try:
        # Initialize Groq using OpenAI-compatible endpoint
        st.session_state.llm = ChatOpenAI(
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=1000,
            openai_api_key=GROQ_API_KEY,
            openai_api_base="https://api.groq.com/openai/v1"
        )
        
        # Test the connection with a simple call
        test_response = st.session_state.llm.invoke("Hello")
        st.success("🚀 Groq API (Llama 3) initialized successfully!")
        
    except Exception as e:
        st.error(f"🚨 Groq API Error: {str(e)}")
        st.stop()

# LangChain setup
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are TechMind powered by Llama 3, an advanced AI assistant created by Meta and running on Groq. 
    You are witty, helpful, and knowledgeable about technology, programming, and various topics. Be engaging, 
    tech-savvy, and use emojis to make responses fun and friendly! You excel at coding, problem-solving, 
    and providing detailed technical explanations."""),
    ("user", "{question}")
])

# Create the chain
chain = prompt_template | st.session_state.llm | StrOutputParser()

# Sidebar
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <div class="sidebar-logo">🚀</div>
        <div class="sidebar-title">TechMind AI</div>
        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 0.5rem;">
            Powered by Llama 3 on Groq ⚡
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("### 💬 Recent Chats")
    
    if st.session_state.messages:
        for msg in st.session_state.messages[-3:]:
            if msg["role"] == "user":
                preview = msg["content"][:35] + "..." if len(msg["content"]) > 35 else msg["content"]
                st.markdown(f"""
                <div class="history-item">
                    <span class="history-text">💭 {preview}</span>
                    <div class="history-time">⏰ Recent</div>
                </div>
                """, unsafe_allow_html=True)
    else:
        for item in ["🤖 AI Introduction", "💡 Tech Tips", "🚀 Project Ideas"]:
            st.markdown(f"""
            <div class="history-item">
                <span class="history-text">{item}</span>
                <div class="history-time">⏰ Sample</div>
            </div>
            """, unsafe_allow_html=True)
    
    if st.button("🗑️ Clear History"):
        st.session_state.messages = []
        st.rerun()

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Display welcome message or chat history
if not st.session_state.messages:
    st.markdown("""
    <div class="welcome-hero">
        <div class="hero-avatar">🤖</div>
        <h1 class="hero-title">TechMind AI</h1>
        <p class="hero-subtitle">⚡ Your lightning-fast coding companion powered by Llama 3 on Groq! Ask me anything about tech, coding, or problem-solving!</p>
    </div>
    """, unsafe_allow_html=True)
else:
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-msg user">
                <div class="msg-avatar user">👨‍💻</div>
                <div class="msg-bubble">
                    <p>{message["content"]}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-msg bot">
                <div class="msg-avatar bot">🤖</div>
                <div class="msg-bubble">
                    <p>{message["content"]}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Chat input and processing
if user_input := st.chat_input("💭 Ask me anything - I'm powered by Llama 3 on Groq! ⚡"):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate response
    with st.spinner("🧠 Llama 3 is thinking at lightning speed..."):
        try:
            response = chain.invoke({"question": user_input})
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        except Exception as e:
            error_msg = f"🚨 Error: {str(e)}"
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
            st.rerun()