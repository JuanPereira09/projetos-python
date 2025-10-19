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

### Resultados 🚀

<img width="1467" height="444" alt="image" src="https://github.com/user-attachments/assets/50b1df3d-ab69-452b-be81-03fbc31da837" />

<img width="1452" height="386" alt="image" src="https://github.com/user-attachments/assets/c354e1b0-e721-4b60-a576-67bd094c314e" />

<img width="1451" height="391" alt="image" src="https://github.com/user-attachments/assets/5c36482b-8082-4672-a791-ba9be48e68c9" />

---

## ⚙️ AutomaçãoPython

### 📝 Descrição
Script de automação de tarefas com a biblioteca PyAutoGUI, que realiza login em um sistema web, lê uma base de dados CSV com informações de produtos e cadastra automaticamente cada item no sistema.

---

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

---

## 🧠 InteligênciaArtificial

### 📝 Descrição

---

Projeto introdutório à Inteligência Artificial e Machine Learning, com notebooks demonstrando algoritmos de classificação, regressão e análise preditiva.
Ideal para estudo de modelos básicos e aplicações práticas com bibliotecas populares.

### 🧰 Tecnologias utilizadas
Python 3.x
Scikit-learn
Pandas
NumPy
Matplotlib / Seaborn

### 🗂️ Estrutura do projeto
InteligênciaArtificial/
│
├── modelo1.ipynb      # Exemplos de IA/ML
├── modelo2.ipynb      # Outros algoritmos
└── dados/             # Conjunto de dados utilizados

▶️ Como executar
1) Instale as dependências:
   pip install scikit-learn pandas numpy matplotlib seaborn jupyter
2) Abra e execute os notebooks:
   jupyter notebook

### Resultados 🚀

<img width="1422" height="226" alt="image" src="https://github.com/user-attachments/assets/c49e01cd-8ede-4869-9e03-986e7e71d29b" />
(Analisou o perfil de cada um dos 3 clientes e previu o score de cada um deles, usando árvore de decisão)
