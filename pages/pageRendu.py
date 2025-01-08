import streamlit as st
from azure.cosmos import CosmosClient
import datetime as dt

#st.image("img/VoltMinuteLogo.png", width=146)
st.title("⚡ VOLTMINUTE ⚡")
st.write("______")

st.write("**Votre batterie a bien été rendue !**")

# Configuration des informations de la base Cosmos DB
secrets = st.secrets["cosmosdb"]
COSMOS_URI = secrets["uri"]
COSMOS_KEY = secrets["key"]
DATABASE_NAME = secrets["database"]
CONTAINER_NAME = secrets["container"]

client = CosmosClient(COSMOS_URI, COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

# Lire un item spécifique
item_id = "battery001"  # ID de l'item
partition_key = item_id  # Remplacez ceci par la vraie clé de partition si applicable

item = container.read_item(item_id, partition_key=partition_key)

# Accéder à une valeur spécifique
date_taken = item.get("DateTaken", "Clé introuvable")  # Remplacez "name" par la clé souhaitée

dateSplit = date_taken.split(':')

hours_taken = dateSplit[0]
minutes_taken = dateSplit[1]

total_minutes = dt.datetime.now().minute - int(minutes_taken)
total_hours = dt.datetime.now().hour - int(hours_taken)

if total_hours==0:
    st.write(f"Vous avez utilisé votre batterie **{total_minutes}** minutes.")
else:
    st.write(f"Vous avez utilisé votre batterie **{total_hours}** heures et {total_minutes} minutes.")

total_minutes = total_minutes + total_hours * 60
total_minutes -= 10
if total_minutes > 0:
    price = total_minutes*0.04
else:
    price = 0

st.write(f"Un montant de **{price} euros** sera débité de votre compte dans les 3 prochain jours.")

st.header("Merci d'avoir utilisé VoltMinute")

st.write("______")
if st.button("Contester"):
    st.write("Non.")