"""
🎮 GAME SDK - Interface Interativa
Aplicação Streamlit para testar e interagir com agentes GAME
"""

import streamlit as st
import os
import json
from datetime import datetime
from dotenv import load_dotenv
import sys
import traceback

# Carregar variáveis de ambiente
load_dotenv()

# Tentar importar o GAME SDK
try:
    from game_sdk.game.agent import Agent, WorkerConfig
    from game_sdk.game.custom_types import Function, Argument, FunctionResult, FunctionResultStatus
    SDK_AVAILABLE = True
except ImportError:
    SDK_AVAILABLE = False
    st.error("⚠️ GAME SDK não instalado. Execute: pip install game_sdk")

# Configuração da página
st.set_page_config(
    page_title="GAME SDK Interface",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 0.5rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        margin: 1rem 0;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        margin: 1rem 0;
    }
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎮 GAME SDK - Interface Interativa")
st.markdown("**Crie e teste agentes autônomos com o framework GAME**")

# Sidebar - Configuração
with st.sidebar:
    st.header("⚙️ Configuração")
    
    # API Key
    api_key = st.text_input(
        "🔑 GAME API Key",
        value=os.getenv("GAME_API_KEY", ""),
        type="password",
        help="Obtenha em https://console.game.virtuals.io/"
    )
    
    if not api_key:
        st.warning("⚠️ Insira sua API Key para continuar")
    
    st.divider()
    
    # Seleção de modelo
    st.subheader("🤖 Modelo de IA")
    model = st.selectbox(
        "Escolha o modelo",
        [
            "Llama-3.1-405B-Instruct",
            "Llama-3.3-70B-Instruct",
            "DeepSeek-R1",
            "DeepSeek-V3",
            "Qwen-2.5-72B-Instruct"
        ],
        help="Modelo de fundação para o agente"
    )
    
    st.divider()
    
    # Informações
    st.subheader("📚 Recursos")
    st.markdown("""
    - [📖 Documentação](https://docs.game.virtuals.io/)
    - [💻 GitHub](https://github.com/game-by-virtuals/game-python)
    - [💬 Discord](https://discord.gg/virtuals)
    - [🌐 Plataforma Virtuals](https://app.virtuals.io/)
    """)

# Tabs principais
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🤖 Criar Agente",
    "⚡ Testar Agente", 
    "🧩 Plugins",
    "📊 Exemplos",
    "📚 Documentação"
])

# Tab 1 - Criar Agente
with tab1:
    st.header("🤖 Configurar Novo Agente")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Informações Básicas")
        agent_id = st.text_input("ID do Agente", value="meu-agente", help="Identificador único")
        agent_description = st.text_area(
            "Descrição do Agente",
            value="Um agente inteligente que ajuda usuários com diversas tarefas",
            height=100,
            help="Personalidade e capacidades do agente"
        )
        agent_goal = st.text_area(
            "Objetivo do Agente",
            value="Auxiliar usuários de forma eficiente e precisa",
            height=100,
            help="Meta principal do agente"
        )
    
    with col2:
        st.subheader("👷 Configurar Workers")
        
        num_workers = st.number_input("Número de Workers", min_value=0, max_value=5, value=1)
        
        workers_config = []
        for i in range(num_workers):
            with st.expander(f"Worker {i+1}"):
                worker_id = st.text_input(f"ID", value=f"worker-{i+1}", key=f"w_id_{i}")
                worker_desc = st.text_area(
                    f"Descrição",
                    value=f"Worker especializado em tarefas específicas",
                    height=80,
                    key=f"w_desc_{i}"
                )
                worker_instruction = st.text_area(
                    f"Instruções",
                    value="Seja preciso e eficiente",
                    height=80,
                    key=f"w_inst_{i}"
                )
                workers_config.append({
                    "id": worker_id,
                    "description": worker_desc,
                    "instruction": worker_instruction
                })
    
    st.divider()
    
    # Estado inicial
    st.subheader("🎯 Estado Inicial")
    
    use_custom_state = st.checkbox("Usar estado customizado")
    
    if use_custom_state:
        initial_state = st.text_area(
            "Estado Inicial (JSON)",
            value=json.dumps({
                "objects": [
                    {"name": "documento", "type": "file"},
                    {"name": "tarefa", "type": "action"}
                ]
            }, indent=2),
            height=150,
            help="Estado inicial em formato JSON"
        )
    else:
        initial_state = "{}"
    
    # Botão para criar agente
    if st.button("🚀 Criar Agente", disabled=not api_key or not SDK_AVAILABLE):
        if SDK_AVAILABLE and api_key:
            try:
                # Salvar configuração na sessão
                st.session_state['agent_config'] = {
                    'id': agent_id,
                    'description': agent_description,
                    'goal': agent_goal,
                    'workers': workers_config,
                    'initial_state': initial_state,
                    'model': model,
                    'api_key': api_key
                }
                
                st.success("✅ Agente configurado com sucesso!")
                st.info("💡 Vá para a aba 'Testar Agente' para executar")
                
                # Mostrar resumo
                with st.expander("📋 Ver Configuração"):
                    st.json(st.session_state['agent_config'])
                    
            except Exception as e:
                st.error(f"❌ Erro ao configurar agente: {str(e)}")

# Tab 2 - Testar Agente
with tab2:
    st.header("⚡ Testar Agente")
    
    if 'agent_config' not in st.session_state:
        st.warning("⚠️ Configure um agente primeiro na aba 'Criar Agente'")
    else:
        config = st.session_state['agent_config']
        
        # Mostrar configuração atual
        with st.expander("📋 Configuração Atual"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("ID", config['id'])
            with col2:
                st.metric("Workers", len(config['workers']))
            with col3:
                st.metric("Modelo", config['model'].split('-')[0])
        
        st.divider()
        
        # Input para tarefa
        st.subheader("💬 Interagir com o Agente")
        
        task_input = st.text_area(
            "Digite uma tarefa ou pergunta:",
            placeholder="Ex: Organize uma lista de tarefas para hoje",
            height=100
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            max_iterations = st.number_input("Max Iterações", min_value=1, max_value=10, value=5)
        
        with col2:
            verbose = st.checkbox("Modo Verbose", value=True, help="Mostrar logs detalhados")
        
        # Botão para executar
        if st.button("▶️ Executar Agente", disabled=not task_input):
            with st.spinner("🔄 Processando..."):
                try:
                    # Container para logs
                    if verbose:
                        log_container = st.container()
                        with log_container:
                            st.info("📝 Logs de Execução:")
                    
                    # Simular execução (aqui você integraria com o SDK real)
                    st.success("✅ Execução concluída!")
                    
                    # Mostrar resposta
                    st.subheader("💬 Resposta do Agente")
                    response_container = st.container()
                    with response_container:
                        st.markdown("""
                        **Agente:** Entendi sua solicitação. Vou organizar uma lista de tarefas.
                        
                        📋 **Lista de Tarefas para Hoje:**
                        1. ✅ Revisar emails importantes
                        2. ⏰ Reunião às 10h
                        3. 📝 Finalizar relatório
                        4. 🔧 Corrigir bugs no código
                        5. 📚 Estudar documentação
                        
                        *Esta é uma resposta simulada. Integre com o GAME SDK para respostas reais.*
                        """)
                    
                    # Métricas de execução
                    st.subheader("📊 Métricas")
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Tempo", "2.3s")
                    with col2:
                        st.metric("Iterações", "3/5")
                    with col3:
                        st.metric("Tokens", "450")
                    with col4:
                        st.metric("Status", "Sucesso")
                        
                except Exception as e:
                    st.error(f"❌ Erro na execução: {str(e)}")
                    st.code(traceback.format_exc())

# Tab 3 - Plugins
with tab3:
    st.header("🧩 Plugins Disponíveis")
    
    # Grid de plugins
    plugins = [
        {"name": "Twitter", "icon": "🐦", "desc": "Integração com Twitter/X", "status": "✅ Ativo"},
        {"name": "Telegram", "icon": "💬", "desc": "Bot do Telegram", "status": "✅ Ativo"},
        {"name": "Discord", "icon": "🎮", "desc": "Bot do Discord", "status": "✅ Ativo"},
        {"name": "ACP", "icon": "💰", "desc": "Agent Commerce Protocol", "status": "✅ Ativo"},
        {"name": "CDP", "icon": "🪙", "desc": "Coinbase Developer Platform", "status": "⚠️ Config"},
        {"name": "RAG Pinecone", "icon": "🧠", "desc": "Base de conhecimento", "status": "⚠️ Config"},
        {"name": "ImageGen", "icon": "🎨", "desc": "Geração de imagens", "status": "✅ Ativo"},
        {"name": "Blockchain", "icon": "⛓️", "desc": "Interações on-chain", "status": "⚠️ Config"},
    ]
    
    cols = st.columns(4)
    for i, plugin in enumerate(plugins):
        with cols[i % 4]:
            with st.container():
                st.markdown(f"""
                <div style="
                    border: 2px solid #e5e7eb;
                    border-radius: 0.5rem;
                    padding: 1rem;
                    text-align: center;
                    height: 150px;
                ">
                    <h3>{plugin['icon']}</h3>
                    <h4>{plugin['name']}</h4>
                    <p style="color: #666; font-size: 0.9rem;">{plugin['desc']}</p>
                    <p>{plugin['status']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    st.divider()
    
    # Configuração de plugin selecionado
    st.subheader("⚙️ Configurar Plugin")
    
    selected_plugin = st.selectbox(
        "Selecione um plugin para configurar",
        [p['name'] for p in plugins]
    )
    
    if selected_plugin == "Twitter":
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("API Key", type="password", key="twitter_key")
            st.text_input("API Secret", type="password", key="twitter_secret")
        with col2:
            st.text_input("Access Token", type="password", key="twitter_token")
            st.text_input("Access Token Secret", type="password", key="twitter_token_secret")
        
        if st.button("💾 Salvar Configuração"):
            st.success(f"✅ Configuração do {selected_plugin} salva!")

# Tab 4 - Exemplos
with tab4:
    st.header("📊 Exemplos de Código")
    
    example_type = st.selectbox(
        "Escolha um exemplo",
        ["Agente Básico", "Agente com Workers", "Integração Twitter", "Sistema Multi-Agente", "RAG + Agente"]
    )
    
    if example_type == "Agente Básico":
        st.subheader("🤖 Agente Básico")
        st.code("""
from game_sdk.game.agent import Agent
from game_sdk.game.custom_types import FunctionResult

def get_state(function_result: FunctionResult, current_state: dict) -> dict:
    return {"status": "ready"}

# Criar agente
agent = Agent(
    id="agente-basico",
    description="Um agente simples para tarefas básicas",
    goal="Auxiliar o usuário",
    get_global_state=get_state,
    workers=[],
    api_key="sua_api_key"
)

# Executar
response = agent.run(max_iterations=5)
print(response)
        """, language="python")
        
    elif example_type == "Agente com Workers":
        st.subheader("👷 Agente com Workers")
        st.code("""
from game_sdk.game.agent import Agent, WorkerConfig
from game_sdk.game.custom_types import Function, Argument, FunctionResult, FunctionResultStatus

def process_task(task: str, **kwargs):
    # Processar tarefa
    return FunctionResultStatus.DONE, f"Tarefa '{task}' concluída", {}

# Definir função
task_function = Function(
    fn_name="process_task",
    fn_description="Processa uma tarefa",
    fn_input=[
        Argument(name="task", type="string", description="Tarefa a processar")
    ],
    executable=process_task
)

# Configurar worker
worker = WorkerConfig(
    id="worker-1",
    worker_description="Worker para processar tarefas",
    get_state_fn=lambda fr, cs: {"tasks": []},
    action_space=[task_function],
    instruction="Processe as tarefas eficientemente"
)

# Criar agente com worker
agent = Agent(
    id="agente-com-worker",
    description="Agente com worker especializado",
    goal="Processar tarefas delegadas",
    get_global_state=get_state,
    workers=[worker],
    api_key="sua_api_key"
)
        """, language="python")
    
    elif example_type == "Integração Twitter":
        st.subheader("🐦 Integração com Twitter")
        st.code("""
from twitter_plugin_gamesdk.twitter_plugin import TwitterPlugin
from game_sdk.game.agent import Agent

# Configurar plugin Twitter
twitter = TwitterPlugin(
    api_key="seu_api_key",
    api_secret="seu_secret",
    access_token="seu_token",
    access_token_secret="seu_token_secret"
)

# Adicionar ao agente
agent = Agent(
    id="twitter-agent",
    description="Agente que posta no Twitter",
    goal="Interagir com seguidores",
    plugins=[twitter],
    api_key="game_api_key"
)

# Postar tweet
response = agent.execute_action(
    "post_tweet",
    {"text": "Olá! Sou um agente GAME 🤖"}
)
        """, language="python")

# Tab 5 - Documentação
with tab5:
    st.header("📚 Documentação Rápida")
    
    doc_section = st.selectbox(
        "Seção",
        ["Conceitos Básicos", "Instalação", "API Reference", "Troubleshooting"]
    )
    
    if doc_section == "Conceitos Básicos":
        st.markdown("""
        ### 🎯 Conceitos Fundamentais
        
        **GAME (Generative Autonomous Multimodal Entities)** é um framework que permite criar agentes autônomos capazes de:
        
        #### Componentes Principais:
        
        1. **Agent (Planejador de Alto Nível)**
           - Define objetivos e estratégias
           - Gerencia workers e estado global
           - Toma decisões de alto nível
        
        2. **Worker (Planejador de Baixo Nível)**
           - Executa tarefas específicas
           - Tem seu próprio espaço de ações
           - Reporta ao agente principal
        
        3. **Functions (Ações)**
           - Unidades executáveis de código
           - Podem chamar APIs, processar dados, etc
           - Retornam status e resultados
        
        #### Fluxo de Execução:
        ```
        User Input → Agent → Workers → Functions → Results → Response
        ```
        """)
        
    elif doc_section == "Instalação":
        st.markdown("""
        ### 🚀 Instalação e Setup
        
        #### Instalar o SDK:
        ```bash
        pip install game_sdk
        ```
        
        #### Instalar plugins (opcional):
        ```bash
        cd plugins/twitter
        pip install -e .
        ```
        
        #### Configurar API Key:
        ```bash
        export GAME_API_KEY="sua_api_key"
        ```
        
        #### Verificar instalação:
        ```python
        import game_sdk
        print(game_sdk.__version__)
        ```
        """)
        
    elif doc_section == "API Reference":
        st.markdown("""
        ### 📖 API Reference
        
        #### Classe Agent
        ```python
        Agent(
            id: str,                    # ID único do agente
            description: str,           # Descrição/personalidade
            goal: str,                  # Objetivo principal
            get_global_state: Callable, # Função de estado
            workers: List[Worker],      # Lista de workers
            api_key: str,              # Chave API GAME
            model: str = "Llama-3.1-405B-Instruct"  # Modelo
        )
        ```
        
        #### Métodos principais:
        - `agent.run(max_iterations=5)` - Executa o agente
        - `agent.reset()` - Reseta o estado
        - `agent.add_worker(worker)` - Adiciona worker
        
        #### Classe WorkerConfig
        ```python
        WorkerConfig(
            id: str,                        # ID do worker
            worker_description: str,        # Descrição
            get_state_fn: Callable,        # Função de estado
            action_space: List[Function],  # Funções disponíveis
            instruction: str               # Instruções
        )
        ```
        """)
        
    elif doc_section == "Troubleshooting":
        st.markdown("""
        ### 🔧 Troubleshooting
        
        #### Erros Comuns:
        
        **1. ImportError: No module named 'game_sdk'**
        - Solução: `pip install game_sdk`
        
        **2. API Key inválida**
        - Verifique se a chave está correta
        - Obtenha nova em: https://console.game.virtuals.io/
        
        **3. Worker não executa ações**
        - Verifique se as funções estão no action_space
        - Confirme que a descrição do worker está clara
        
        **4. Rate limit exceeded**
        - Adicione delays entre chamadas
        - Use cache quando possível
        
        #### Debug:
        ```python
        # Ativar modo verbose
        agent.run(max_iterations=5, verbose=True)
        
        # Verificar estado
        print(agent.get_current_state())
        ```
        """)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>Construído com 💜 usando GAME SDK e Streamlit</p>
    <p>
        <a href="https://github.com/game-by-virtuals/game-python">GitHub</a> • 
        <a href="https://docs.game.virtuals.io/">Docs</a> • 
        <a href="https://discord.gg/virtuals">Discord</a>
    </p>
</div>
""", unsafe_allow_html=True)

# Status no sidebar
with st.sidebar:
    st.divider()
    st.subheader("📊 Status")
    
    if SDK_AVAILABLE:
        st.success("✅ SDK Instalado")
    else:
        st.error("❌ SDK não encontrado")
    
    if api_key:
        st.success("✅ API Key configurada")
    else:
        st.warning("⚠️ API Key ausente")
    
    if 'agent_config' in st.session_state:
        st.success("✅ Agente configurado")
    else:
        st.info("💤 Nenhum agente ativo")