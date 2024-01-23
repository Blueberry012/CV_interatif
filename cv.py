import streamlit as st
from streamlit_timeline import st_timeline

CURRENT_THEME = "blue"
IS_DARK_THEME = True

with st.sidebar:
    st.image("Images\ThomChhun.jpg")
    st.title("Coordonnées")
    st.write("📞 06 29 56 57 82")
    st.write("✉️ thom.chhun@gmail.com")
    st.write("📍 Courbevoie (92400)")
    st.write("📅 20 ans")
    st.link_button("Accéder à mon Linkedin", "https://www.linkedin.com/in/thom-chhun-b7a587233/")
    st.link_button("Accéder à mon Porfolio", "https://fancy-trifle-4c29ba.netlify.app/")
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
items = [
    {"id": 1, "content": "BAC Général", "Diplôme":"BAC Spécialités Mathématiques et Sciences Économiques et Sociales", "Mention": "Admis Mention Bien", "Etablissement": "Lycée privé Montalembert", "Lieu": "Courbevoie (92400)","start": "2021-07-01"},
    {"id": 2, "content": "BUT SD (ex. STID)", "Formation":"BUT Sciences des Données, Statistique et Informatique Décisionnelle", "Parcours": "Visualisation et Conception d'Outils Décisionnel","Etablissement": "IUT de Paris – Rives de Seine", "Lieu": "Paris 16e", "start": "2021-09-01"},
    {"id": 3, "content": "Mise en œuvre d’une enquête", "Formation":"BUT Sciences des Données, Statistique et Informatique Décisionnelle", "Etablissement": "IUT de Paris – Rives de Seine", "Lieu": "Paris 16e", "start": "2021-11-01"},
    {"id": 4, "content": "Création d'un reporting", "Formation":"BUT Sciences des Données, Statistique et Informatique Décisionnelle", "Etablissement": "IUT de Paris – Rives de Seine", "Lieu": "Paris 16e", "start": "2022-01-01"},
    {"id": 5, "content": "Analyse de données et datavisualisation", "Formation":"BUT Sciences des Données, Statistique et Informatique Décisionnelle", "Etablissement": "IUT de Paris – Rives de Seine", "Lieu": "Paris 16e", "start": "2022-04-01"},
    {"id": 6, "content": "Alternance", "Poste": "Alternant Data Analyst" ,"Entreprise":"Gan Assurances", "Lieu": "Nanterre (92000)", "start": "2022-09-01"},
    {"id": 7, "content": "Mise en œuvre d’un processus de Datamining", "Formation":"BUT Sciences des Données, Statistique et Informatique Décisionnelle", "Etablissement": "IUT de Paris – Rives de Seine", "Lieu": "Paris 16e", "start": "2023-11-01"},
    {"id": 8, "content": "Conception d'un outil décisionnel", "Formation":"BUT Sciences des Données, Statistique et Informatique Décisionnelle", "Etablissement": "IUT de Paris – Rives de Seine", "Lieu": "Paris 16e", "start": "2024-01-01"},
    {"id": 9, "content": "Migration de données vers ou depuis un environnement NoSQL", "Formation":"BUT Sciences des Données, Statistique et Informatique Décisionnelle", "Etablissement": "IUT de Paris – Rives de Seine", "Lieu": "Paris 16e", "start": "2024-02-01"}
]

timeline = st_timeline(items, groups=[], options={}, height="300px")
st.write(timeline)

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


st.subheader("Projet Universitaire")

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

with st.expander("Mise en œuvre d’une enquête"):
    st.write("- Réalisation d’un questionnaire sur LimeSurvey à propos du devenir d’anciens")
    st.write("- Conception et nettoyage de la base de données.")
    st.write("- Modélisation d’études sur Excel pour réaliser une enquête statistique.")
    st.write("- Présentation orale des résultats.")

with st.expander("Création d'un reporting"):
    st.write("- Récupération des données d’un loueur pour développer une entreprise fictive.")
    st.write("- Exploitation de la base de données en créant des requêtes sur SQL.")
    st.write("- Conduite d’une étude statistique à l’aide d’Excel pour réaliser des synthèses numériques et graphiques.")

with st.expander("Analyse de données et datavisualisation"):
    st.write("- Web scrapping d’un site avec python pour étudier la performance de coureurs du 800m.")
    st.write("- Exportation et nettoyage de la base de données sur R pour créer une base de données propre à partir des données brutes sous format CSV.")
    st.write("- Création des codes pour l’analyse statistique des données nécessitant la gestion des librairies, packages, listes et dictionnaires.")
st.divider()
st.write("Pour plus d'information concernant mes projets et mon parcours, je vous invite à conculter mon Portfolio")
st.link_button("Accéder à mon Porfolio", "https://fancy-trifle-4c29ba.netlify.app/")