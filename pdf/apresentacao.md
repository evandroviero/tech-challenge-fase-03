# Introdução
Objetivo: Contextualizar o problema.
* Problema que estamos resolvendo: previsão do valor do aluguel de imóveis com base em características do imóvel e da localização.
* Tipo de problema: Regressão (valor contínuo).
* Motivação: permitir que proprietários e imobiliárias tenham uma estimativa confiável do valor de aluguel, otimizando decisões.


# Coleta de Dados
Objetivo: Explicar a origem dos dados.
    * https://www.kaggle.com/code/mehdislim01/data-analysis-on-brasilian-houses-to-rent
* Dados estruturados: banco de dados SQLite/Postgres com a tabela houses.
* Features disponíveis:
    * Localização: city
    * Estrutura: area, rooms, bathroom, parking_spaces, floor
    * Características adicionais: animal, furniture
    * Custos adicionais: hoa, property_tax, fire_insurance
    * Target: rent_amount
* Possibilidade de dados em tempo real: coletar via API ou integração com sistemas de imobiliárias.

# Armazenamento
Objetivo: Mostrar como os dados são organizados.
* Banco relacional: SQLite/Postgres para CRUD (Create, Read, Update, Delete).
* Estrutura da tabela: houses com índice em campos importantes (animal, furniture).
* Alternativa: Data Lake ou Data Warehouse para histórico e análises mais complexas.

# Análise Exploratória
Objetivo: Mostrar insights visuais do dataset.
Sugestão de gráficos no Streamlit:
* Distribuição do valor de aluguel → histograma do rent_amount.
* Correlação entre variáveis → heatmap das correlações (area, rooms, bathroom, etc).
* Boxplots por cidade → entender variações de aluguel por localização.
* Impacto de features binárias (animal, furniture) → comparação de médias de aluguel.
* Distribuição de custos adicionais → hoa, property_tax, fire_insurance.
* Pontos a destacar: tendências, outliers e padrões interessantes.

# Processamento de Dados
Objetivo: Explicar limpeza e preparação.
* Tratamento de nulos: preencher com 0 ou mediana.
* Escalonamento: opcional para alguns modelos, mas RandomForest não precisa.
* Transformações: codificação de variáveis categóricas (city) via One-Hot Encoding.
* Enriquecimento: cálculo de total_cost = hoa + property_tax + fire_insurance.

# Modelagem
Objetivo: Apresentar o modelo escolhido e justificativa.
* Modelo: RandomForestRegressor
* Motivo: robusto, lida bem com dados não lineares, pouco sensível a outliers.
* Treinamento: dados divididos em treino/teste + cross-validation.
* Métricas no teste:
    * MAE: 58.33
    * RMSE: 200.40
    * R²: 0.995 → excelente ajuste.
* Cross-validation:
    * R² médio: 0.9943
    * MAE médio: 61.28
* Conclusão: modelo está consistente e pronto para produção.


# Aplicação Frontend (Streamlit)
Objetivo: Mostrar como o modelo alimenta uma aplicação.
Funcionalidades da aplicação:
1. Visualização de dados e gráficos interativos (histogramas, boxplots, correlações).
2. Cadastro de imóveis → formulário com campos city, area, rooms, etc.
3. Edição e exclusão de imóveis → manutenção do banco de dados.
4. Previsão de aluguel → input das características do imóvel e output do valor previsto pelo modelo.
5. Filtros por cidade, área, número de quartos para análises exploratórias.

# Arquitetura do Sistema
Objetivo: Explicar integração entre os componentes.
* API (FastAPI) → CRUD + endpoint de previsão (/predict).
* Banco de dados → SQLite/Postgres, armazenando imóveis e histórico de previsões.
* Modelo ML → RandomForest treinado, carregado pela API.
* Frontend (Streamlit) → interface interativa, gráficos, cadastro e previsão.
Fluxo: Usuário → Streamlit → FastAPI → Modelo → Retorno da previsão.

# Conclusão
Objetivo: Resumir resultados e próximos passos.
* Modelo robusto para previsão de aluguel, R² > 0.99.
* Aplicação completa com CRUD e dashboards interativos.
* Possíveis melhorias:
    * Coleta de dados em tempo real via API externa.
    * Implementação de alertas para imóveis com preços fora da média.
    * Integração com Data Lake para análises históricas e tendências.