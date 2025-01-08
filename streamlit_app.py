import streamlit as st

st.image("img/VoltMinuteLogo.png", width=146)
st.title("⚡ VOLTMINUTE ⚡")
st.write("______")

st.write(
    "Borne : **Champ de Mars (Angoulême)**"
)

from azure.cosmos import CosmosClient, exceptions

# Configuration des informations de la base Cosmos DB
secrets = st.secrets["cosmosdb"]
COSMOS_URI = secrets["uri"]
COSMOS_KEY = secrets["key"]
DATABASE_NAME = secrets["database"]
CONTAINER_NAME = secrets["container"]

# Fonction pour se connecter à Cosmos DB
@st.cache_resource
def connect_to_cosmos_db():
    try:
        client = CosmosClient(COSMOS_URI, COSMOS_KEY)
        database = client.get_database_client(DATABASE_NAME)
        container = database.get_container_client(CONTAINER_NAME)
        return container
    except exceptions.CosmosHttpResponseError as e:
        st.error(f"Erreur de connexion à Cosmos DB: {e}")
        return None

# Initialisation de la connexion
container = connect_to_cosmos_db()
#if container:
    #st.success("Connexion à Cosmos DB établie avec succès !")

# Exemple : Lire tous les éléments d'un conteneur
def read_items():
    if container:
        items = list(container.read_all_items())
        return items
    return []

# Afficher les données dans Streamlit
items = read_items()
if items:
    for item in items:
        battery_name = item.get("name", "Clé non trouvée")  # Remplacez "name" par la clé que vous cherchez
        battery_level = item.get("BatteryLevel", "Clé non trouvée")  # Remplacez "name" par la clé que vous cherchez
        if st.button(f"{battery_name} - 🔋 Chargée à {battery_level}"):
            st.page_link("pages/pageChrono.py", label="Je choisis cette batterie", icon="⚡")
    