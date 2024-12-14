# Chatbot Simples em Python

Este é um projeto simples de um chatbot desenvolvido em Python, utilizando a API da OpenAI para gerar respostas com base em mensagens fornecidas pelo usuário. O chatbot mantém um histórico de conversa para tornar as respostas mais contextuais.

---

## **Tecnologias Utilizadas**
- **Python** (>=3.8)
- **Bibliotecas**:
  - `openai`
  - `dotenv`

---

## **Como Configurar o Projeto**

### **1. Clonar o Repositório**

### **2. Criar e Ativar um Ambiente Virtual**

No Windows:
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

No Linux/Mac:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **3. Instalar Dependências**

```bash
pip install -r requirements.txt
```

### **4. Configurar Variáveis de Ambiente**

1. Crie um arquivo `.env` na raiz do projeto.
2. Adicione a chave de API da OpenAI:

```
API_KEY=your_openai_api_key_here
```

### **5. Executar o Projeto**

```bash
python chatbot.py
```

---

## **Como Usar o Chatbot**
1. Ao executar o programa, o terminal irá solicitar que você insira uma mensagem.
2. Digite uma mensagem e pressione **Enter**.
3. O chatbot irá responder com base na entrada fornecida.
4. Digite `exit` para encerrar a conversa.

---

## **Estrutura do Projeto**

```plaintext
.
├── chatbot.py          # Arquivo principal do chatbot
├── .env                # Arquivo de variáveis de ambiente (API Key)
├── .gitignore          # Arquivo para ignorar arquivos no Git
├── requirements.txt    # Dependências do projeto
```

---

## **Possíveis Problemas e Soluções**

### **1. `ModuleNotFoundError` ao importar `openai`**
Certifique-se de que o ambiente virtual está ativado e que as dependências foram instaladas corretamente com o comando:
```bash
pip install -r requirements.txt
```

### **2. Chave de API Inválida**
Verifique se o arquivo `.env` está configurado corretamente e se a chave de API fornecida é válida.

---

## **Melhorias Futuras**
- Adicionar interface gráfica.
- Melhorar o gerenciamento do histórico de conversa.
- Implementar logging para depuração.

---

## **Licença**
Este projeto está licenciado sob a [MIT License](LICENSE).

