#!/bin/bash

# Script para executar o app Streamlit localmente

echo "🚀 Iniciando GAME SDK Interface..."
echo "=================================="

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.8+"
    exit 1
fi

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativar ambiente virtual
echo "🔄 Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -q -r requirements.txt

# Verificar se .env existe
if [ ! -f ".env" ]; then
    echo "⚠️  Arquivo .env não encontrado!"
    echo "📝 Criando .env a partir do exemplo..."
    cp .env.example .env
    echo "✏️  Por favor, edite o arquivo .env com sua GAME_API_KEY"
fi

# Executar Streamlit
echo "=================================="
echo "✅ Iniciando aplicação..."
echo "🌐 Acesse: http://localhost:8501"
echo "=================================="

streamlit run app.py