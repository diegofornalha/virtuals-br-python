# 🚀 Deploy no Netlify - GAME SDK Landing Page

## Deploy Rápido (Opção 1 - Recomendado)

### Via GitHub:

1. **Faça fork ou crie um novo repositório** com os arquivos:
   - `index.html` (página principal)
   - `netlify.toml` (configuração)
   - `.env.example` (exemplo de variáveis)
   - Pasta `docs/imgs/` com as imagens

2. **Conecte ao Netlify:**
   - Acesse [app.netlify.com](https://app.netlify.com)
   - Clique em "Add new site" → "Import an existing project"
   - Escolha GitHub e autorize
   - Selecione seu repositório
   - Configurações de build:
     - Build command: (deixe vazio)
     - Publish directory: `.`
   - Clique em "Deploy site"

### Via Upload Direto:

1. **Acesse Netlify:**
   - Vá para [app.netlify.com/drop](https://app.netlify.com/drop)

2. **Arraste a pasta do projeto** ou clique para fazer upload dos arquivos:
   - `index.html`
   - `netlify.toml`
   - Pasta `docs/` (se tiver imagens locais)

3. **Pronto!** Seu site será publicado instantaneamente

## Deploy Manual (Opção 2)

### Usando Netlify CLI:

```bash
# Instalar Netlify CLI
npm install -g netlify-cli

# Login no Netlify
netlify login

# Deploy do site
netlify deploy --prod

# Ou deploy com preview primeiro
netlify deploy  # Preview
netlify deploy --prod  # Produção
```

## Configuração de Domínio Personalizado

1. No painel do Netlify, vá para "Domain settings"
2. Clique em "Add custom domain"
3. Digite seu domínio (ex: `game-sdk.seudominio.com`)
4. Configure os DNS:
   - **CNAME**: aponte para `seu-site.netlify.app`
   - Ou use os nameservers do Netlify

## Variáveis de Ambiente (Opcional)

Se você quiser adicionar analytics ou outras funcionalidades:

1. Vá para "Site settings" → "Environment variables"
2. Adicione variáveis como:
   - `GOOGLE_ANALYTICS_ID`
   - `SENTRY_DSN`
   - etc.

## URLs Após Deploy

Seu site estará disponível em:
- **URL temporária:** `https://[nome-aleatorio].netlify.app`
- **URL customizada:** `https://seu-dominio.com` (após configurar)

## Funcionalidades do Site

✅ **Landing page responsiva** com informações sobre o GAME SDK  
✅ **Seções organizadas:** Hero, Features, Exemplo de código, Plugins, Acesso  
✅ **Links diretos** para GitHub, Documentação e Discord  
✅ **Animações suaves** ao fazer scroll  
✅ **Design moderno** com gradientes e sombras  
✅ **SEO otimizado** com meta tags  
✅ **Performance otimizada** com cache headers  

## Estrutura de Arquivos

```
projeto/
├── index.html          # Página principal
├── netlify.toml        # Configuração do Netlify
├── .env.example        # Exemplo de variáveis de ambiente
├── README.md           # Documentação do SDK
├── README-DEPLOY.md    # Este arquivo
└── docs/
    └── imgs/          # Imagens do projeto
```

## Customização

Para personalizar o site, edite o `index.html`:

- **Cores:** Altere as variáveis CSS em `:root`
- **Textos:** Traduza ou modifique o conteúdo
- **Plugins:** Adicione/remova na seção de plugins
- **Links:** Atualize URLs de redes sociais

## Suporte

- **Netlify Docs:** https://docs.netlify.com
- **GAME SDK Docs:** https://docs.game.virtuals.io
- **Discord:** #builders-chat

---

💡 **Dica:** Após o deploy, compartilhe o link no Discord da comunidade Virtuals para feedback!