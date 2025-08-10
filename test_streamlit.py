#!/usr/bin/env python3
"""
Script de teste para verificar se o app Streamlit está funcional
"""

import sys
import os

def test_imports():
    """Testa se todas as importações funcionam"""
    print("🔍 Testando importações...")
    
    try:
        import streamlit as st
        print("✅ Streamlit importado")
    except ImportError as e:
        print(f"❌ Erro ao importar Streamlit: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv importado")
    except ImportError as e:
        print(f"❌ Erro ao importar dotenv: {e}")
        return False
    
    try:
        from game_sdk.game.agent import Agent
        print("✅ GAME SDK importado")
    except ImportError as e:
        print(f"⚠️  GAME SDK não encontrado (normal se não instalado): {e}")
    
    return True

def test_env():
    """Testa se as variáveis de ambiente estão configuradas"""
    print("\n🔍 Testando variáveis de ambiente...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GAME_API_KEY")
    if api_key:
        print(f"✅ GAME_API_KEY encontrada: {api_key[:10]}...")
    else:
        print("⚠️  GAME_API_KEY não encontrada no .env")
    
    return True

def test_streamlit_config():
    """Testa se a configuração do Streamlit existe"""
    print("\n🔍 Testando configuração do Streamlit...")
    
    if os.path.exists(".streamlit/config.toml"):
        print("✅ Arquivo config.toml encontrado")
    else:
        print("❌ Arquivo config.toml não encontrado")
        return False
    
    return True

def main():
    print("=" * 50)
    print("🚀 TESTE DO APP STREAMLIT - GAME SDK")
    print("=" * 50)
    
    all_tests_passed = True
    
    # Testa importações
    if not test_imports():
        all_tests_passed = False
    
    # Testa variáveis de ambiente
    if not test_env():
        all_tests_passed = False
    
    # Testa configuração
    if not test_streamlit_config():
        all_tests_passed = False
    
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("✅ TODOS OS TESTES PASSARAM!")
        print("\n🎉 App está pronto para deploy!")
        print("\n📝 Próximos passos:")
        print("1. Local: streamlit run app.py")
        print("2. Deploy: https://streamlit.io/cloud")
    else:
        print("⚠️  Alguns testes falharam")
        print("Verifique os erros acima")
    print("=" * 50)

if __name__ == "__main__":
    main()