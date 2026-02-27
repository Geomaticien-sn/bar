import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="CV - Mamadou Lamine FALL",
    page_icon="📍",
    layout="wide"
)

# Sidebar pour Profil, Contact, Centres d'intérêt
with st.sidebar:
    st.markdown("---")
    
    # Icône diplôme + PROFIL
    st.markdown("""
    <div style='text-align: center;'>
        <h2 style='color: #1f77b4; margin-bottom: 10px;'>📚 PROFIL</h2>Étudiant en BTS Géomatique, sérieux, motivé et dynamique, disposant de solides compétences en cartographie, SIG et traitement de données spatiales. Passionné par la topographie, l’aménagement du territoire, l’agriculture et l’environnement.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='font-size: 14px; line-height: 1.4; color: #333;'>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # CONTACT
    st.markdown("""
    <div style='text-align: center;'>
        <h3 style='color: #ff7f0e; margin-bottom: 15px;'>📞 CONTACT</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
        <div style='font-size: 13px; color: #555;'>
            <strong>📧</strong> barafall5359@gmail.com<br>
            <strong>📱</strong> https://www.linkedin.com/in/mamadou-lamine-fall-385153283<br>
            <strong>📍</strong> Rue CA 192, Cambérène, Dakar, Sénégal
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # CENTRES D'INTÉRÊT
    st.markdown("""
    <div style='text-align: center;'>
        <h3 style='color: #2ca02c; margin-bottom: 15px;'>🎯 CENTRES D'INTÉRÊT</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='font-size: 13px; color: #555; text-align: center;'>
        <strong>🏃‍♂️</strong> Sport<br>
        <strong>🎭</strong> Musique
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<style>
.title {
    font-size: 32px;
    font-weight: bold;
    text-align: center;
}

.subtitle {
    font-size: 14px;
    letter-spacing: 3px;
    text-align: center;
    color: gray;
}

.section {
    font-size: 18px;
    font-weight: bold;
    margin-top: 30px;
    letter-spacing: 2px;
}

.line {
    width: 60px;
    height: 3px;
    background-color: black;
    margin-bottom: 15px;
}

.item-title {
    font-weight: bold;
}

.date {
    font-size: 13px;
    color: gray;
}

ul {
    margin-left: 20px;
}
</style>
""", unsafe_allow_html=True)


# En-tête
st.markdown('<div class="title">Mamadou Lamine FALL</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">TECHNICIEN SUPÉRIEUR EN GÉOMATIQUE</div>', unsafe_allow_html=True)

st.write("")

# Formations
st.markdown('<div class="section">FORMATIONS</div>', unsafe_allow_html=True)
st.markdown('<div class="line"></div>', unsafe_allow_html=True)

st.markdown("""
**BTS Géomatique**  
Baccalauréat S2 – Sciences Expérimentales
""")


# Expériences
st.markdown('<div class="section">EXPÉRIENCES</div>', unsafe_allow_html=True)
st.markdown('<div class="line"></div>', unsafe_allow_html=True)


# DSCOS
st.markdown("""
<div class="item-title">Stage à la Direction Générale de la Surveillance et du Contrôle de l’Occupation du Sol (DGSCOS)</div>
<div class="date">17/07/2025 – 17/10/2025</div>
<ul>
<li>Collecte et traitement des données spatiales</li>
<li>Suivi de l’occupation du sol</li>
<li>Appui aux travaux cartographiques</li>
<li>Participation aux missions de contrôle du territoire</li>
<li>Utilisation des outils SIG</li>
<li>Numérisation des parcelles</li>
<li>Renseignement des informations foncières</li>
<li>Génération des fichiers KML</li>
</ul>
""", unsafe_allow_html=True)


# SOTRACOM
st.markdown("""
<div class="item-title">Assistant Topographe – SOTRACOM SA</div>
<div class="date">2021 – 2023</div>
<ul>
<li>Participation aux levés topographiques</li>
<li>Implantation et contrôle des ouvrages</li>
<li>Utilisation des instruments (niveau, GPS, station totale)</li>
<li>Traitement des données topographiques</li>
<li>Appui aux équipes terrain</li>
</ul>
""", unsafe_allow_html=True)
# Titre de la section
st.markdown("## COMPÉTENCES")

# Colonnes pour séparer logiciels et SIG/DAO
col1, col2 = st.columns(2)

with col1:
    st.markdown("**LOGICIELS MAÎTRISÉS :**")
    logiciels = [
        "ArcMap",
        "Qgis",
        "Looping",
        "PowerAMC",
        "Pix4D Mapper",
        "Erdas Imagine",
        "Agisoft",
        "Metashape",
        "Microstation",
        "AutoCAD"
    ]
    for logiciel in logiciels:
        st.write(f"- {logiciel}")

with col2:
    st.markdown("**:**")
    autres = [
        "SIG : QGIS, ArcGIS",
        "DAO : AutoCAD, SketchUp",
        "Cartographie et topographie",
        "Levés topographiques et implantation",
        "Télédétection et photogrammétrie",
        "Traitement de données spatiales",
        "Bases de données géographiques",
        "Bureautique : Word, Excel, PowerPoint",
        "Télédétection",
        "Planification de vol de drone",
        "Traitement d’images de drone"
    ]
    for item in autres:
        st.write(f"- {item}")

# Section langues
st.markdown("**LANGUES :**")
st.write("- Anglais : Parlé et écrit")
st.write("- Italien : Moyen")
