# 🎬 HashFlix — Plataforma de Streaming com Django

O **HashFlix** é uma aplicação web inspirada em serviços de streaming (como a Netflix), desenvolvida para gerenciar e disponibilizar catálogos de vídeos/cursos com controle total de usuários, buscas dinâmicas e perfis personalizados.

---

## 🛠️ Tecnologias Utilizadas

### **Back-end**
* **Python 3.14**: Linguagem principal do ecossistema.
* **Django**: Framework web para toda a regra de negócio, roteamento, ORM e views.
* **Django Crispy Forms**: Renderização e estilização simplificada de formulários.
* **SQLite**: Banco de dados relacional para armazenamento de usuários, filmes e episódios.

### **Front-end**
* **HTML5 / CSS3**: Estruturação semântica e customizações visuais.
* **Tailwind CSS**: Estilização utilitária responsiva para componentes modernos (Navbar, Showcase, Cards).
* **Django Template Language (DTL)**: Integração dinâmica entre o Python e as páginas web.

### **DevOps & Versionamento**
* **Git & GitHub**: Versionamento de código e hospedagem do repositório.

---

## ✨ Funcionalidades do Projeto

* 🔐 **Sistema Completo de Autenticação**:
  * Cadastro de novos usuários (`criarconta`).
  * Autenticação via Login/Logout seguro (`POST` com tokens CSRF).
  * Redirecionamentos automáticos por estado de autenticação (`LOGIN_REDIRECT_URL`).
* 👤 **Gerenciamento de Perfil**:
  * Edição de dados de perfil (`edita_perfil`).
  * Troca de senha integrada.
* 🎥 **Catálogo de Filmes/Cursos**:
  * Exibição dinâmicas de thumbs e mídias.
  * Página de detalhes de cada conteúdo com episódios vinculados.
* 🔍 **Sistema de Pesquisa**:
  * Busca em tempo real de conteúdos por títulos/termos.
* 🎨 **Interface Responsiva**:
  * Layout escuro no estilo streaming com menu fixo (`navbar`) condicional para usuários logados e visitantes.

---

## 📁 Estrutura de Pastas Resumida

```text
Projeto 6- Desenvolvimento com Django (Netflix)/
├── HashFlix/              # Configurações globais do projeto Django (settings, urls, etc.)
├── filme/                 # App principal (models, views, forms, urls e novos_contextos)
│   ├── migrations/        # Histórico do banco de dados
│   └── templates/         # Páginas HTML (login, logout, perfil, home, etc.)
├── templates/             # Templates globais (base.html, navbar.html)
├── static/                # Arquivos estáticos (imagens da interface, logos)
├── media/                 # Uploads de mídias/thumbs enviados no projeto
├── requirements.txt       # Dependências de bibliotecas Python
└── manage.py              # Utilitário de comando do Django