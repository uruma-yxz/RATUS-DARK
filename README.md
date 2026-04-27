# RATUS DARK

<p align="center">
<img width="300" height="250" alt="imagem" src="https://github.com/user-attachments/assets/de3395f0-fa09-4716-92fe-1b83aac2f556" />
</p>

---

## Aviso Legal
**ESSE PROJETO FOI FEITO 100 % EDUCATIVO O CRIADO DO PROJETO N TEM RESPOSABILIDADE SE O PROJETO FOR USADO DE MAL FORMAL OU PARA AREA CRIMINOSA**

## Arquitetura

O projeto RATUS DARK é organizado de forma modular para facilitar a extensão e personalização, especialmente para fins educacionais de desenvolvimento de malwares. A arquitetura segue um padrão de separação de responsabilidades, onde cada módulo tem uma função específica. Abaixo, uma descrição detalhada da estrutura e do fluxo de execução.

### Estrutura de Diretórios e Arquivos

```
Ratus Dark/
├── README.md
└── src/
    ├── Full/          # Pasta vazia para expansões futuras
    ├── bot/           # Contém a lógica do bot principal
    │   └── Ratus.py   # Classe responsável por coletar informações do sistema
    ├── database/      # Armazenamento de dados
    │   └── user.json  # Arquivo JSON com dados da vítima
    ├── logo/          # Elementos visuais
    │   └── logo.py    # Função que retorna o logo ASCII
    ├── main.py        # Ponto de entrada do programa
    ├── malweres/      # Diretório para malwares personalizados
    ├── menu/          # Interface de controle
    │   └── Menu.py    # Classe que gerencia o fluxo inicial
    ├── token/         # Armazenamento de credenciais
    │   └── token_webhook.txt  # URL do webhook do Discord
    └── webhook/       # Comunicação externa
        └── Discord.py # Classe para envio via Discord webhook
```

- **README.md**: Arquivo de documentação do projeto, contendo informações sobre instalação, uso e arquitetura.

- **src/**: Diretório raiz do código fonte.
  - **bot/**: Contém a lógica central do "bot" ou agente malicioso.
    - **Ratus.py**: Classe principal que representa o núcleo do malware.
      - **Métodos principais**:
        - `getOS()`: Coleta informações sobre o sistema operacional.
        - `getIP()`: Obtém o endereço IP público.
        - `user()`: Coleta o nome de usuário.
        - `malweres()`: Placeholder para malwares personalizados.
        - `execute()`: Coordena a coleta e salvamento de dados.

  - **database/**: Gerenciamento de dados persistentes.
    - **user.json**: Armazena dados coletados (username, OS, IP).

  - **logo/**: Elementos visuais.
    - **logo.py**: Retorna a arte ASCII do logo.

  - **main.py**: Ponto de entrada, inicia o menu.

  - **malweres/**: Destinado a scripts de malwares adicionais.

  - **menu/**: Controle de fluxo.
    - **Menu.py**: Exibe logo e inicia o bot.

  - **token/**: Credenciais.
    - **token_webhook.txt**: URL do webhook.

  - **webhook/**: Comunicação.
    - **Discord.py**: Envia dados via webhook.

  - **Full/**: Pasta reservada para futuras expansões.

### Fluxo de Execução Detalhado

1. **Inicialização**: `main.py` importa `Menu` e chama `init.execute()`.
2. **Exibição Inicial**: `Menu` exibe o logo.
3. **Ativação do Bot**: Inicia `Discord.execute()`.
4. **Coleta e Envio**: Coleta dados com `Ratus` e envia via webhook.

Essa arquitetura é modular e extensível para fins educacionais.

## Objetivo
**ESSE PROJETO FOI FEITO PRA CRIAR UM MALWERE, ELE E UM MALWERE PRE PRONTO PARA VC PEGAR O ESQUELETO E NA PASTA MALWERES VC FAZER ALGUNS SEUS MALWERES E NO BOT SO CHAMAR ELES, ELE NO INCIO CHAMA UM WEBHOOK PARA SEU SERVER FALADO AS INFOMAO DAS VITIMA ETC**

O projeto serve como um esqueleto para criação de malwares. Ele coleta informações básicas da vítima (nome de usuário, sistema operacional, IP) e envia para um webhook do Discord. A pasta `malweres` permite adicionar malwares personalizados, que podem ser chamados no método `malweres()` da classe `Ratus`.

## Requisitos

- **Python**: Versão 3.6 ou superior.
- **Bibliotecas**:
  - `requests`: Para fazer requisições HTTP (usado para obter IP e enviar webhook).
  - Outras dependências indiretas: `urllib3`, `charset_normalizer`, `chardet`, `cryptography` (geralmente instaladas com `requests`).

Para instalar as dependências, execute:
```
pip install requests
```

Certifique-se de que o arquivo `src/token/token_webhook.txt` contenha um URL válido de webhook do Discord.
