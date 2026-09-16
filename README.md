# Xdatabot

Automação desenvolvida em Python para extração de históricos processuais em sistema web legado.

## Objetivo

O projeto foi desenvolvido com foco em automatizar consultas operacionais em sistema web legado, reduzindo trabalho manual de navegação, coleta e organização de dados históricos.


## Tecnologias Utilizadas

- Python 3.14+
- Selenium 4.44.0
- beautifulsoup4 4.14.3
- openpyxl 3.1.5
- pydantic-settings 2.14.1
- pathlib
- Programação Orientada a Objetos

## Funcionalidades

- Navegação entre as telas do sistema
- Localização e Conversão da estrutura HTML
- Extração de dados
- Exportação para Excel com tabelas formatadas
- Criação automática de diretórios (ano, mês, dia)


## Estrutura

```cmd
XDataBot/
│
│
├── src/
│   └── data/
│   │   └── ano/
│   │        └── mês/
│   │             └── dia/
│   │
│   ├── pages/
│   │   ├── login.py
│   │   ├── menu.py
│   │   ├── form.py
│   │   └── data_list.py
│   │
│   ├── services/
│   │   ├── export_excel_service.py
│   │   └── extraction_history_service.py
│   │
│   ├── settings/
│   │   └── config.py
│   │
│   └── main.py
│
├── .env
├── .gitignore
└── README.md

```
