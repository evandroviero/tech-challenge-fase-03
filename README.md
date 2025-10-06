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
├── database.db
frontend/
├── analysis.py
├── app.py
├── db_connection.py
├── predict.py
migrations/
notebook/
├── analise_exploratoria..ipynb
├── modelagem.ipynb
├── testar_api.ipynb
model/
├── rend_model.pkl
pdf/
├── Pos_tech - Tech Challenge - Fase 3.pdf
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
uvicorn api.app:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

Documentação Swagger:

```
http://127.0.0.1:8000/docs
```

### 5. Rodar o servidor Streamlit
```bash
streamlit run frontend/app.py 
```

A aplicação estará disponível em:

```
http://localhost:8501
```