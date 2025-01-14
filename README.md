# Visualizador da Fase da Lua

Este projeto foi desenvolvido para visualizar a fase atual da Lua com base em uma data fornecida pelo usuário. A interface gráfica foi construída com **Tkinter**, e as fases da Lua são calculadas usando a biblioteca **Astronomy**. O programa permite que o usuário insira uma data específica e receba a fase da Lua correspondente a esse dia, acompanhada de uma imagem que representa a fase.

## Funcionalidades

- **Calcula a fase da Lua** com base em dados astronômicos para qualquer data inserida.
- **Interface gráfica simples** com um campo para inserir a data e exibir a fase da Lua.
- **Exibe a imagem correspondente à fase** da Lua, mostrando visualmente o estado atual da Lua.
- **Suporte para datas passadas e futuras**, permitindo consultas a qualquer momento.

## Tecnologias Usadas

- **Python 3.12**: Linguagem de programação principal.
- **Tkinter**: Biblioteca para construção da interface gráfica.
- **Pillow (PIL)**: Biblioteca para manipulação de imagens.
- **Astronomy**: Biblioteca para cálculos das fases da Lua.

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/<seu-usuario>/<nome-do-repositorio>.git
   cd <nome-do-repositorio>
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # No Windows: env\Scripts\activate
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
4. Execute o script:
   ```bash
   python moon.py
5. Abra o aplicativo, insira uma data no formato AAAA-MM-DD, e veja a fase da Lua correspondente!
   
   
