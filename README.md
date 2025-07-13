# Métodos Numéricos para Engenharia 

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/) [![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/) [![NumPy](https://img.shields.io/badge/NumPy-Library-green.svg)](https://numpy.org/) [![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-red.svg)](https://matplotlib.org/)

Este repositório contém implementações de métodos numéricos fundamentais para engenharia, desenvolvido como parte da disciplina de Métodos Numéricos da **Universidade de Brasília (UnB) - Faculdade de Ciências e Tecnologia em Engenharia (FCTE)**.

## 🎯 Sobre o Projeto

Este projeto apresenta soluções computacionais para problemas clássicos de métodos numéricos aplicados à engenharia, implementados em Python utilizando Jupyter Notebooks. As implementações focam em clareza didática e precisão numérica.

## 📚 Questões Implementadas

### 1️⃣ **Questão 1 - Método de Müller**
- **Arquivo**: `Questoes/Questao1.ipynb`
- **Objetivo**: Encontrar raízes de equações não-lineares
- **Função analisada**: `f(x) = x³ - 0.5x² + 4x - 2`
- **Características**:
  - Implementação pura em Python
  - Suporte a raízes complexas
  - Acompanhamento detalhado das iterações
  - Tolerância configurável (padrão: 1e-8)

### 2️⃣ **Questão 2 - Eliminação de Gauss para Análise de Circuitos**
- **Arquivo**: `Questoes/Questao2.ipynb`
- **Objetivo**: Resolver sistemas lineares aplicados à análise nodal de circuitos elétricos
- **Sistema analisado**: Rede resistiva com 4 nós
- **Características**:
  - Implementação com pivoteamento parcial
  - Cálculo de tensões nodais
  - Solução de sistemas Ax = B

### 3️⃣ **Questão 4 - Diagrama de Bifurcação do Mapa Logístico**
- **Arquivo**: `Questoes/Questao4.ipynb`
- **Objetivo**: Visualizar comportamento caótico em sistemas dinâmicos
- **Características**:
  - Análise do mapa logístico: x_{n+1} = rx_n(1-x_n)
  - Geração de diagramas de bifurcação
  - Visualização para diferentes intervalos de parâmetros
  - Identificação de regiões de caos e periodicidade

## 🛠 Tecnologias Utilizadas

- **Python 3.10+**: Linguagem principal
- **Jupyter Notebook**: Ambiente de desenvolvimento interativo
- **NumPy**: Computação numérica eficiente
- **Matplotlib**: Visualização de dados e gráficos
- **cmath**: Suporte a números complexos

## 🚀 Como Executar

### Pré-requisitos
```bash
# Instalar Python 3.10 ou superior
# Instalar Jupyter Notebook
pip install jupyter numpy matplotlib
```

### Executando os Notebooks

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/matheuslemesam/MetodosNumericos
   cd MetodosNumericos
   ```

2. **Inicie o Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

3. **Navegue até a pasta `Questoes/` e abra o notebook desejado**

4. **Execute as células sequencialmente** usando `Shift + Enter`

## 📁 Estrutura do Projeto

```
MetodosNumericos/
├── README.md                    # Documentação do projeto
├── listaE.pdf                   # Enunciado da lista de exercícios
└── Questoes/
    ├── Questao1.ipynb          # Método de Müller
    ├── Questao2.ipynb          # Eliminação de Gauss (Circuitos)
    ├── Questao3ListaE.pdf      # Enunciado da Questão 3
    └── Questao4.ipynb          # Diagrama de Bifurcação
```

## 🔬 Metodologias Implementadas

### Método de Müller
- **Aplicação**: Encontrar raízes de equações não-lineares
- **Vantagens**: Convergência quadrática, suporte a raízes complexas
- **Implementação**: Algoritmo completo com acompanhamento de iterações

### Eliminação Gaussiana com Pivoteamento
- **Aplicação**: Solução de sistemas lineares
- **Vantagens**: Estabilidade numérica, eficiência computacional
- **Uso prático**: Análise de circuitos elétricos

### Análise de Sistemas Dinâmicos
- **Aplicação**: Estudo de comportamento caótico
- **Ferramenta**: Diagrama de bifurcação
- **Insights**: Visualização da transição ordem-caos

## 👨‍💻 Autores

**Desenvolvido por**: Grupo E  
**Instituição**: Universidade de Brasília (UnB)  
**Faculdade**: Ciências e Tecnologia em Engenharia (FCTE)  
**Disciplina**: Métodos Numéricos para Engenharia - Prof. Rodrigo Cerda
