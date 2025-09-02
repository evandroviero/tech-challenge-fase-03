# TECH CHALLENGE FASE 03

## 📋 Descrição do Projeto 
* API REST criada com FastAPI permite realizar operações CRUD.
* Utiliando modelo aprendizado supervisionado para identificar o valor de imoveis.
* Dashboard em streamlit apresentando os resultados

Tecnologias usadas:

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Alembic
- Ruff (linter/formatter)
- Pandas
- Sklearn
- Streamlit

## 📦 Estrutura do Projeto

```
api/
├── app.py
├── database.py
├── models.py
├── routers.py
├── schemas.py
db/
migrations/
pdf/
alembic.ini
pyproject.toml
requirements.txt
```

---

## ▶️ Como rodar o projeto

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```
---

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

---
### 3. Rodar as migrações do banco de dados (Alembic)

```bash
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

---

### 4. Rodar o servidor FastAPI

```bash
task run_api
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

Documentação Swagger:

```
http://127.0.0.1:8000/docs
```


## Estrutura do Tech Challenge

1) Qual é o seu problema?
    * Reg.
    * Class
    * Série temporal

2) Coleta de dados
    * Data SUS
    * Kaggle
    * Crawler e varrer a internet
    * Trabalhar com APIs
    * Banco de dados estruturados
    * Dados OMS
    * Drive Org
    * ETC (infinitas fontes de dados)

3) Armazenamento    
    * Estruturado
        * MySQL
        * Postgres
        * SQL Server
        * XLSX
    * Não estruturado
        * JSON
        * Avro
        * E-mails
        * MP3
        * PDF

4) Analisar
    * Qual é o comportamento do seu dado?
    * Quais são as particularidades?
    * Como são as distribuições?
    * Como são as correlações entre as variáveis?
    * Existem sazonalidades?
    * Sempre de acordo com o contexto!
    * Análises estatísticas: médias, medianas, desvios, outliers, etc

5) Processamento dos dados (se necessário)
    * Enriquecimento dos dados
    * Tratamento de registros nulos
    * Enriquecimento de chave x valor
    * Cálculo
    * Escalas (alguns modelos não trabalham bem com os dados em escalas diferentes)

6) Modelagem
    * Escolher o modelo
    * Testar os modelos (entendendo as métricas de avaliação adequada)
    * Comparar as "versões" do modelo (baseado nas métricas)
    * Interpretar os resultados: Escolha seu modelo "campeão"

7) Deploy
    * Fazer uso do modelo criado
    * Páginas Web com input para o modelo
    * Modelo respondendo input de API
    * PowerBI (normalmente para classificação)