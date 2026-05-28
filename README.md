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

 - Navegação dinâmica entre as telas do sistema
 - Localização e Conversão da estrutura HTML
 - Extração de dados
 - Exportação para Excel com tabelas formatadas
 - Criação automática de diretórios (ano, mês, dia)


## Estrutura

```python
XDataBot/
│
├── Histórico/
│
├── src/
│   │
│   ├── pages/
│   │   ├── login.py
│   │   ├── menu.py
│   │   ├── form.py
│   │   └── list.py
│   │
│   ├── services/
│   │   ├── export_excel_service.py
│   │   ├── extraction_history_service.py
│   │   └── extract_date_service.py
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

## Como exercutar?

### 1) Clone o repositório
```bash
git clone https://github.com/CodePhsp/projeto-xdatabot.git
cd projeto-xdatabot
```

### 2) Crie seu ambiente virtual
Para o sistema operacional windows

> Dica: você pode escolher qualquer nome para seu ambiente virtual 
```bash
python -m venv .venv
venv\Scripts\activate  
```

Para o sistema operacional Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4) Execute
```bash
cd src
python main.py
```

### 5) Aguarde a aplicação
Ao iniciar, insira o CNPJ no qual deseja realizar a extração dos dados

```bash
Insira o CNPJ: 00.000.000/0001-00
```
| Após inserir o CNPJ e der "enter" a automação irá iniciar.
OBS.: Não é recomendável mexer no computador enquanto a automação está seno executada.

### 6) Extração realizada
Ao final da execução será gerado a seguinte estrutura de pasta:
```bash
Histórico/
    └── 202x/ # Ano
        └── 0x/ # mês
            └── xx/  # dia
                └── Relatório_xx-xx-xxxx.xlsx
```
