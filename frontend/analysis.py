import pandas as pd
import sqlalchemy as db
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import squarify 
import math



DATABASE_URL = "sqlite:///db/database.db"
ENGINE = db.create_engine(DATABASE_URL)

def load_data():
    query = "SELECT * FROM houses"
    return pd.read_sql(query, con=ENGINE)


def plot_categorical_counts(df, cat_cols):
    """
    Plota gráficos de contagem para colunas categóricas com fundo escuro (modo dark).
    """
    n = len(cat_cols)
    cols = 2
    rows = math.ceil(n / cols)

    fig, ax = plt.subplots(rows, cols, figsize=(10*cols, 5*rows))
    
    # Garantir que ax seja sempre 2D
    if rows == 1 and cols == 1:
        ax = [[ax]]
    elif rows == 1:
        ax = [ax]
    elif cols == 1:
        ax = [[a] for a in ax]

    # Loop para plotar cada gráfico
    for i, col_name in enumerate(cat_cols):
        row, col_pos = divmod(i, cols)
        sns.countplot(
            data=df,
            x=col_name,
            palette="pastel",
            order=df[col_name].value_counts().index,
            ax=ax[row][col_pos]
        )
        ax[row][col_pos].set_title(f'Contagem por {col_name}', fontsize=14, color='white')
        ax[row][col_pos].set_xlabel(col_name, fontsize=12, color='white')
        ax[row][col_pos].set_ylabel('Contagem', fontsize=12, color='white')
        ax[row][col_pos].tick_params(axis='x', rotation=45, colors='white')
        ax[row][col_pos].tick_params(axis='y', colors='white')
        ax[row][col_pos].set_facecolor('#0E1117')  # fundo do gráfico

    fig.patch.set_facecolor('#0E1117')  # fundo da figura
    plt.tight_layout()
    st.pyplot(fig)

def plot_graphical(cat_col, value_col="rent_amount", top_n=5):
    df = load_data()
    if cat_col in ["animal", "furniture"]:
        df[cat_col] = df[cat_col].map({1: 'Sim', 0: 'Não'})

    if pd.api.types.is_numeric_dtype(df[cat_col]):
        n_charts = 2 if value_col is None else 3
    else:
        n_charts = 3

    fig, axes = plt.subplots(n_charts, 1, figsize=(10, 5*n_charts))  # largura fixa, altura proporcional
    
    if n_charts == 1:
        axes = [axes]  # Garantir lista
    
    idx = 0
    if pd.api.types.is_numeric_dtype(df[cat_col]):
        plot_histogram(df, cat_col, ax=axes[idx])
        idx += 1
        plot_boxplot(df, cat_col, ax=axes[idx])
        idx += 1
        if value_col:
            plot_bar_chart(df, cat_col, value_col=value_col, ax=axes[idx])
    else:
        plot_bar_chart(df, cat_col, value_col=value_col, ax=axes[idx])
        idx += 1
        plot_pie_chart(df, cat_col, value_col=value_col, ax=axes[idx], top_n=top_n)
        idx += 1
        plot_treemap(df, cat_col, value_col=value_col, ax=axes[idx])
        axes[idx].set_title("Treemap")
        axes[idx].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    st.pyplot(fig)

def plot_treemap(df, cat_col, value_col="rent_amount", ax=None, top_n=10):
    if value_col:
        df_grouped = df.groupby(cat_col)[value_col].sum().reset_index()
    else:
        df_grouped = df[cat_col].value_counts().reset_index()
        df_grouped.columns = [cat_col, value_col or "count"]
    df_grouped = df_grouped.sort_values(by=value_col or "count", ascending=False).head(top_n)
    
    sizes = df_grouped[value_col or "count"]
    labels = df_grouped[cat_col] + "\n" + sizes.astype(str)
    squarify.plot(sizes=sizes, label=labels, ax=ax, alpha=0.8)
    ax.axis('off')
    ax.set_title(f"Treemap {cat_col}")



def plot_bar_chart(df, cat_col, value_col="rent_amount", ax=None):
    df_grouped = df.groupby(cat_col)[value_col].mean().reset_index()
    df_grouped = df_grouped.sort_values(by=value_col, ascending=False)
    sns.barplot(data=df_grouped, x=cat_col, y=value_col, ax=ax)
    ax.set_title(f"Valor {cat_col} x {value_col}")
    ax.set_xlabel(cat_col)
    ax.set_ylabel(value_col)
    ax.tick_params(axis='x', rotation=45)

def plot_boxplot(df, col, ax=None):
    sns.boxplot(y=df[col], ax=ax, color='lightgreen')
    ax.set_title(f"Boxplot de {col}")
    ax.set_ylabel(col)

def plot_pie_chart(df, cat_col, value_col="rent_amount", ax=None,  top_n=5):
    df_grouped = df.groupby(cat_col)[value_col].sum().reset_index()

    df_grouped = df_grouped.sort_values(by=value_col, ascending=False)
    top_categories = df_grouped.head(top_n)
    other_categories = df_grouped.iloc[top_n:]

    if not other_categories.empty:
        other_sum = other_categories[value_col].sum()
        top_categories = pd.concat([top_categories, pd.DataFrame({cat_col: [f'+ {top_n}'], value_col: [other_sum]})], ignore_index=True)

    ax.pie(top_categories[value_col], labels=top_categories[cat_col], autopct='%1.1f%%', startangle=140)
    ax.set_title(f"Distribuição {cat_col} x {value_col}")

def plot_histogram(df, col, ax=None):
    sns.histplot(df[col], kde=True, ax=ax, color='skyblue')
    ax.set_title(f"Distribuição de {col}")
    ax.set_xlabel(col)