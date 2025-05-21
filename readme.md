# SOFTEX-FACEBOOK

## Guia de Início Rápido

Este repositório contém o projeto de testes para o curso. Siga as instruções abaixo para configurar seu ambiente de desenvolvimento.

### 1. Clonando o Repositório

Para obter uma cópia local do projeto, execute o seguinte comando no terminal:

```bash
git clone https://github.com/usantyerleo/SOFTEX-FACEBOOK.git
cd SOFTEX-FACEBOOK
```

### 2. Instalando Dependências

Este projeto usa Python.

Para instalar todas as dependências necessárias, execute:

```bash
pip install -r requirements.txt
```

### 3. Criando sua Branch

Para trabalhar em um teste ou correção, crie sua própria branch:

```bash
# Atualize seu repositório local com as últimas alterações
git pull origin main

# Crie e mude para uma nova branch
git checkout -b nome-da-sua-branch
```

Sugestões para nomes de branches:
- `Task_JIRA_DATA__NOME_AUTOMACAO_TC` - Para cada teste
- Exemplo: `TASK-123_20052025_DAVID_AUTOMACAO_TC`

### 4. Salvando e Enviando suas Alterações

Depois de fazer suas alterações, siga estes passos para enviá-las:

```bash
# Verifique quais arquivos foram alterados
git status

# Adicione os arquivos que você deseja enviar
git add nome-do-arquivo
# Ou para adicionar todos os arquivos alterados:
git add .

# Commit das alterações
git commit -m "Descrição clara das alterações"

# Envie para o repositório remoto
git push origin nome-da-sua-branch
```

### 5. Criando um Pull Request

Após enviar suas alterações:
1. Vá para o [repositório no GitHub](https://github.com/usantyerleo/SOFTEX-FACEBOOK)
2. Clique em "Pull Requests" e depois em "New Pull Request"
3. Selecione sua branch para comparar com a main
4. Clique em "Create Pull Request"
5. Adicione uma descrição detalhada das suas alterações
6. Submeta o Pull Request para revisão

## Tecnologias Utilizadas

- Python
- Selenium
- WebDriver Manager
- Outras bibliotecas (ver `requirements.txt`)
