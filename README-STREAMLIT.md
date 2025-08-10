# 🚀 Deploy Streamlit - GAME SDK Interface

## 📋 Visão Geral

Interface interativa em Streamlit para testar e gerenciar agentes GAME SDK com:
- ✅ Criar e configurar agentes
- ✅ Testar execução com interface visual
- ✅ Gerenciar plugins
- ✅ Exemplos de código prontos
- ✅ Documentação integrada

## 🎯 Funcionalidades

### 1. **Criar Agente** 
- Configure ID, descrição e objetivo
- Adicione múltiplos workers
- Defina estado inicial customizado
- Escolha o modelo de IA

### 2. **Testar Agente**
- Execute tarefas interativamente
- Visualize logs em tempo real
- Métricas de performance
- Histórico de conversas

### 3. **Plugins**
- Visualize plugins disponíveis
- Configure credenciais
- Status de ativação
- Integração fácil

### 4. **Exemplos**
- Código pronto para copiar
- Diferentes casos de uso
- Integração com Twitter, Telegram, etc

### 5. **Documentação**
- Referência de API
- Troubleshooting
- Guias rápidos

## 🛠️ Instalação Local

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Configurar variáveis de ambiente
cp .env.example .env
# Edite .env com suas chaves

# 3. Executar aplicação
streamlit run app.py

# Ou com configurações customizadas
streamlit run app.py --server.port 8080 --server.address localhost
```

## ☁️ Deploy no Streamlit Cloud (GRÁTIS)

### Passo 1: Preparar Repositório

```bash
# Commit dos arquivos
git add app.py requirements.txt .streamlit/
git commit -m "Add Streamlit interface for GAME SDK"
git push
```

### Passo 2: Deploy no Streamlit Cloud

1. **Acesse:** https://streamlit.io/cloud
2. **Faça login** com GitHub
3. **Clique em** "New app"
4. **Configure:**
   - Repository: `diegofornalha/virtuals-br-python`
   - Branch: `main` ou `diegofornalha/entender-projeto`
   - Main file path: `app.py`
5. **Advanced settings:**
   - Python version: 3.10
   - Adicione secrets (variáveis de ambiente):
     ```
     GAME_API_KEY = "sua_api_key_aqui"
     TWITTER_API_KEY = "opcional"
     TELEGRAM_BOT_TOKEN = "opcional"
     ```
6. **Clique em** "Deploy!"

### Passo 3: URL do App

Após deploy, você receberá uma URL como:
```
https://game-sdk-interface.streamlit.app
```

## 🔧 Configuração de Secrets

No Streamlit Cloud, vá em **"Settings"** → **"Secrets"** e adicione:

```toml
# Obrigatório
GAME_API_KEY = "apt-2f56110d8d6213ad19ddc368f84edef1"

# Opcional - Plugins
TWITTER_API_KEY = "sua_chave"
TWITTER_API_SECRET = "seu_secret"
TWITTER_ACCESS_TOKEN = "seu_token"
TWITTER_ACCESS_TOKEN_SECRET = "seu_token_secret"

TELEGRAM_BOT_TOKEN = "seu_bot_token"

# Outros plugins...
```

## 🐳 Deploy com Docker (Alternativa)

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
# Build e run
docker build -t game-sdk-ui .
docker run -p 8501:8501 --env-file .env game-sdk-ui
```

## 🌐 Outras Opções de Deploy

### Hugging Face Spaces
1. Crie um Space em https://huggingface.co/spaces
2. Escolha Streamlit como SDK
3. Upload dos arquivos
4. Configure secrets

### Render.com
1. Conecte GitHub
2. Escolha "Web Service"
3. Configure como Python app
4. Adicione start command: `streamlit run app.py`

### Railway.app
1. Conecte GitHub
2. Deploy automático
3. Configure variáveis
4. URL gerada automaticamente

## 📊 Uso da Interface

### Criar um Agente:
1. Insira sua API Key no sidebar
2. Vá para aba "Criar Agente"
3. Configure ID, descrição e objetivo
4. Adicione workers se necessário
5. Clique em "Criar Agente"

### Testar o Agente:
1. Vá para aba "Testar Agente"
2. Digite uma tarefa ou pergunta
3. Clique em "Executar Agente"
4. Veja a resposta e métricas

### Configurar Plugins:
1. Vá para aba "Plugins"
2. Selecione o plugin desejado
3. Insira as credenciais
4. Salve a configuração

## 🔒 Segurança

- **Nunca** commite API keys no código
- Use **secrets** do Streamlit Cloud
- Configure **variáveis de ambiente** localmente
- Use **.env** para desenvolvimento
- Adicione **.env** ao **.gitignore**

## 🆘 Troubleshooting

### Erro: "GAME SDK não instalado"
```bash
pip install game_sdk
```

### Erro: "API Key inválida"
- Verifique se a key está correta
- Obtenha nova em https://console.game.virtuals.io/

### App não carrega
- Verifique requirements.txt
- Confirme versão do Python (>=3.8)
- Limpe cache: `streamlit cache clear`

### Deploy falha no Streamlit Cloud
- Verifique logs de build
- Confirme que requirements.txt está correto
- Use Python 3.10 nas configurações

## 📚 Recursos

- **GAME SDK Docs:** https://docs.game.virtuals.io/
- **Streamlit Docs:** https://docs.streamlit.io/
- **GitHub Repo:** https://github.com/game-by-virtuals/game-python
- **Discord:** https://discord.gg/virtuals

## 🎉 Pronto!

Sua interface Streamlit está pronta para:
1. **Desenvolvimento local:** `streamlit run app.py`
2. **Deploy gratuito:** Streamlit Cloud
3. **Produção:** Docker, Railway, Render

---

💡 **Dica:** Comece com Streamlit Cloud - é grátis e fácil!