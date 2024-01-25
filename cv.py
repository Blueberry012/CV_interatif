import streamlit as st
from streamlit_timeline import timeline

CURRENT_THEME = "blue"
IS_DARK_THEME = True

with st.sidebar:
    st.image("Images/ThomChhun.jpg")
    st.title("Coordonnées")
    st.write("📞 06 29 56 57 82")
    st.write("✉️ thom.chhun@gmail.com")
    st.write("📍 Courbevoie (92400)")
    st.write("📅 20 ans")
    st.link_button("Consulter mon Porfolio", "https://thom-chhun-portfolio.netlify.app")
    st.link_button("Consulter mon Linkedin", "https://www.linkedin.com/in/thom-chhun-b7a587233")
    st.download_button(
            label="Télécharger mon CV",
            key="download_button",
            on_click=None,
            file_name="CV_CHHUN_Thom.pdf",
            data="Images\CV_CHHUN_Thom.pdf",
            help="Mon CV",
        )

    with st.expander("Outils"):
        st.subheader("Data Mining et Analyse de données :")
        st.write("- Python (pandas, NumPy, matplotlib)")
        st.write("- R Studio (shiny, tidyverse, caret, factoextra, rpart)")
        st.subheader("Requêtage et Nettoyage de données :")
        st.write("- SAS")
        st.write("- SQL")
        st.write("- Dataiku")
        st.subheader("Langages de  programmation :")
        st.write("- Shell Unix")
        st.write("- Html et CSS")
        st.write("- Streamlit (folium)")
        st.subheader("Reporting et datavisualisation:")
        st.write("- Qlik Sense")
        st.write("- Power BI")
        st.write("- Tableau")
        st.write("- Github et GitLab")
        st.subheader("Logiciels Pack Office:")
        st.write("- Excel")
        st.write("- Word")
        st.write("- PowerPoint")
        st.write("- Access")

    with st.expander("Langues"):
        st.write("Anglais (C1)")
        st.write("Chinois Mandarin (B1, diplômé HSK 3)")

st.title("Thom Chhun")
st.subheader("Alternant Data Analyst")
st.write("Après 2 ans en tant qu'alternant Data Analyst, je recherche une nouvelle alternance en tant que Data Scientist à partir de septembre 2024 sur une période de 3 ans.")

st.subheader("Diplômes, Formations et Projets")

with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=300)

st.subheader("Expérience Professionnel")
st.write("- Création d'un robot automatisant les tâches récurrentes avec Rstudio")
st.write("- Réalisation d'une application QlikSense à partir de données Jira")
st.write("- Datamining et Textmining de classification d'assureurs adverses avec Python")
st.write("- Traitement et jointure de données avec SAS")

st.subheader("Compétences")

with st.expander("Informatique décisionnelle"):
    st.write("- Création d'outil décisionnel et Dataviz Web (publication d'applications Streamlit, projet Github)")
    st.write("- Développement Logiciel (Versioning, tests unitaires, configuration de l'environnement, Modélisation UML)")
    st.write("- Migration de données (MongoDB, SQL, SQLite, NoSQL)")

with st.expander("Machine Learning"):
    st.write("- Application des mécanismes de bases de l’intelligence artificielle (apprentissage statistique supervisé, échantillons d'apprentissage et échantillons de test)")
    st.write("- Réalisation de modèle de Machine Learning (k-plus proches voisins, Régression, Classification, arbres de décision CART)")
    st.write("- Mise en œuvre d'un processus de Datamining (Construction de la base d'étude, Discrétisation, Modélisation, Exploitation du score)")


st.subheader("Projets Universitaires")

with st.expander("Conception d'un outil décisionnel"):
    st.write("- Transformation de la donnée pour la mettre en conformité avec des normes (anonymisation, normalisation)")
    st.write("- Intégration la vision de l’interlocuteur (transversalité, international, multiculture, niveau d’expertise…)")
    st.write("- Conception de mon outil décisionnel sous la forme d’une application Streamlit programmée en Python")
    st.write("- Publication mon application hébergée par Streamlit en créant un repository sur GitHub")

with st.expander("Mise en œuvre d’un processus de Datamining"):
    st.write("- Réalisation d'un modèle CART sous R en Classification")
    st.write("- Réalisation d'un modèle CART sous R en Regression")
    st.write("- Déroulement d'une procédure d'apprentissage automatique (échantillons d'apprentissage, développement, test)")
    st.write("- Application des arbres de décisions CART, de la méthode des K plus proches voisins,")

with st.expander("Migration de données vers ou depuis un environnement NoSQL"):
    st.write("- Appropriation du modèle source pour créer le modèle de la base cible adapté")
    st.write("- Portage d'une base de données relationnelles vers un environnement NoSQL")
    st.write("- Développement des programmes de migration des données")
    st.write("- Réalisation des scripts de requêtage de la nouvelle base de données")

st.divider()
st.write("Pour plus d'information concernant mes projets et mon parcours, je vous invite à conculter mon Portfolio")
st.link_button("Consulter mon Porfolio", "https://thom-chhun-portfolio.netlify.app")
