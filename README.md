# Sistema de Atendimento Bancário

Este projeto é uma simulação de sistema de atendimento com senhas prioritárias e normais, desenvolvido em Python com interface gráfica usando Tkinter.

## 🌟 Funcionalidades

- Geração de senhas normais e prioritárias.
- Simulação de chamada de senhas para guichês.
- Interface separada para cliente e atendente.
- Painel com som e histórico das últimas chamadas.
- Suporte a múltiplos guichês.

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- Tkinter (interface gráfica)
- pygame (para som)

## 📁 Estrutura de Pastas

```
sistema_atendimento/
│
├── core/               # Lógica principal de senhas e filas
│   ├── senha.py
│   └── fila.py
│
├── gui/                # Interfaces gráficas
│   ├── painel.py
│   ├── painel_cliente.py
│   └── painel_chamadas.py
│
├── services/           # Regras de negócio (serviços)
│   └── atendimento_service.py
│
├── utils/              # Utilitários auxiliares
│   └── audio.py
│
├── assets/             # Recursos como arquivos de som
│   └── ding.mp3
│
├── main.py             # Arquivo principal para execução
├── requirements.txt    # Lista de dependências
└── README.md           # Este arquivo
```

## 🚀 Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema_atendimento.git
   cd sistema_atendimento
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o projeto:
   ```bash
   python3 main.py
   ```

## 🔊 Requisitos

- Certifique-se de ter o `pygame` instalado para reproduzir o som das chamadas.
- O arquivo `ding.mp3` deve estar na pasta `assets`.

## 📌 Observações

- O sistema foi desenvolvido para fins educacionais.
- Pode ser expandido para simular múltiplas filas, relatórios, integração com banco de dados etc.

## 📄 Licença

MIT License © 2025 Eduardo Firmino