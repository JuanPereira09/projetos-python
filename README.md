# 🐍 Projetos em Python

Repositório com três projetos desenvolvidos em **Python**, abordando desde **automação de tarefas** até **análise de dados** e **aplicações de inteligência artificial**.  
Cada projeto está organizado em sua respectiva pasta:

- **AnáliseDadosPython/**
- **AutomaçãoPython/**
- **InteligênciaArtificial/**

---

## 📚 Sumário

- [📊 AnáliseDadosPython](#-análisedadospython)
- [⚙️ AutomaçãoPython](#️-automaçãopython)
- [🧠 InteligênciaArtificial](#-inteligênciaartificial)
- [📁 Estrutura geral do repositório](#-estrutura-geral-do-repositório)
- [🧾 Licença](#-licença)
- [👨‍💻 Autor](#-autor)

---

## 📊 AnáliseDadosPython

### 📝 Descrição
Projeto voltado à **análise e visualização de dados** utilizando ferramentas da biblioteca **Pandas** e outras auxiliares.  
O notebook demonstra o processo de leitura, limpeza, manipulação e extração de insights a partir de bases de dados reais.

### 🧰 Tecnologias utilizadas
- Python 3.x  
- Jupyter Notebook  
- Pandas  
- Matplotlib / Seaborn (para gráficos e visualizações)

### 🗂️ Estrutura do projeto
AnáliseDadosPython/
│
├── inicial.ipynb # Notebook principal com toda a análise
└── datasets/ # (opcional) Bases de dados utilizadas

### ▶️ Como executar
1. Instale as dependências:
   pip install pandas matplotlib seaborn jupyter
Abra o notebook:
  jupyter notebook inicial.ipynb



## ⚙️ AutomaçãoPython

### 📝 Descrição
Script de automação de tarefas com a biblioteca PyAutoGUI, que realiza login em um sistema web, lê uma base de dados CSV com informações de produtos e cadastra automaticamente cada item no sistema.

### ⚡ Funcionalidades
- Acesso automático ao navegador e ao site da empresa
- Login automatizado com usuário e senha
- Leitura da base de dados via pandas
- Cadastro automatizado de produtos
- Rolagem e repetição do processo para todos os registros

### 🧰 Tecnologias utilizadas
- Python 3.x
- PyAutoGUI
- Pandas

### 🗂️ Estrutura do projeto
AutomaçãoPython/
│
├── automação.py    # Script principal
└── produtos.csv    # Base de dados dos produtos

### ▶️ Como executar
⚠️ Importante: Ajuste as coordenadas de clique (x, y) no script conforme a resolução da sua tela.
1)
pip install pyautogui pandas
2)
python automação.py


