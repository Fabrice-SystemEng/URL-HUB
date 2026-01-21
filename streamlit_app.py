import streamlit as st
import pandas as pd
import os

# Configuration de la page
st.set_page_config(page_title="Nexus Hub", layout="wide")

# Style CSS pour améliorer l'apparence
st.markdown("""
    <style>
    .main {
        background-color: #0f111a;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #1e2130;
        color: #52a8ff;
        border: 1px solid #32415e;
    }
    </style>
    """, unsafe_allow_html=True)

def load_data(file_path):
    """Charge les données depuis un fichier CSV"""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return pd.DataFrame(columns=['Nom', 'Cible', 'Categorie', 'Couleur'])

def display_buttons(df):
    """Affiche les boutons organisés par catégories et sur 3 colonnes"""
    categories = df['Categorie'].unique()
    for category in categories:
        st.subheader(f"📂 {category}")
        df_category = df[df['Categorie'] == category]
        
        # Création des colonnes (3 colonnes)
        cols = st.columns(3)
        
        # Distribution des boutons dans les colonnes
        for i, (index, row) in enumerate(df_category.iterrows()):
            button_label = row['Nom']
            button_url = row['Cible']
            button_color = row.get('Couleur', '#3498db') # Valeur par défaut si absent

            # On utilise le modulo (%) pour alterner entre les 3 colonnes
            with cols[i % 3]:
                st.markdown(
                    f'<a href="{button_url}" target="_blank" style="text-decoration: none;">'
                    f'<div style="background-color: {button_color}; color: white; padding: 15px; '
                    f'border-radius: 10px; text-align: center; margin-bottom: 15px; font-weight: bold; '
                    f'transition: transform 0.2s; box-shadow: 2px 2px 5px rgba(0,0,0,0.2); min-height: 60px; '
                    f'display: flex; align-items: center; justify-content: center;">'
                    f'{button_label}</div></a>',
                    unsafe_allow_html=True
                )

def main():
    st.title("🌐 WEB NAVIGATION HUB")

    # Chemins des fichiers de données
    file1 = "data/Url_Liste_Modifiable.csv"
    file2 = "data/Url_Liste_Modifiable_2.csv"

    # Système d'onglets Streamlit
    tab1, tab2 = st.tabs(["LISTES CSV 1", "LISTES CSV 2"])

    with tab1:
        df1 = load_data(file1)
        if not df1.empty:
            display_buttons(df1)
        else:
            st.info("Aucune donnée trouvée dans Url_Liste_Modifiable.csv")

    with tab2:
        df2 = load_data(file2)
        if not df2.empty:
            display_buttons(df2)
        else:
            st.info("Aucune donnée trouvée dans Url_Liste_Modifiable_2.csv")

if __name__ == "__main__":
    main()