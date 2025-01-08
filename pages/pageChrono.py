import streamlit as st
import time
import datetime as dt

def chronometer():
    ts = 1
    if st.button("Go to 10min"):
        ts = 600
    if st.button("Go to 30min"):
        ts = 1800
    with st.empty():
        while ts:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            
            if mins >= 10:
                price = (mins-10) * 0.04
            else:
                price = 0

            st.header(f"⏰ Temps d'utilisation : {time_now}  \n 💸 Prix à payer : {price} €  \n _______")

            time.sleep(1)
            ts += 1

        st.write("Fin du chrono")

from azure.cosmos import CosmosClient

# Mettre à jour un item
def update_item(item_id, date_start):

    # Paramètres de connexion Cosmos DB
    secrets = st.secrets["cosmosdb"]
    COSMOS_URI = secrets["uri"]
    COSMOS_KEY = secrets["key"]
    DATABASE_NAME = secrets["database"]
    CONTAINER_NAME = secrets["container"]

    # Connexion
    client = CosmosClient(COSMOS_URI, COSMOS_KEY)
    database = client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)

    # Rechercher l'item existant
    item = container.read_item(item_id, partition_key=item_id)  # Remplacez 'item_id' par votre clé de partition si nécessaire

    # Modifier l'attribut de l'item
    item["DateTaken"] = date_start

    # Mettre à jour l'item dans Cosmos DB
    updated_item = container.replace_item(item_id, item)
    return updated_item

def main():
    #st.image("img/VoltMinuteLogo.png", width=146)
    st.title("⚡ VOLTMINUTE ⚡")
    st.write("______")

    st.write("Vous pouvez récupérer la batterie.")

    st.page_link("pages/pageMap.py", label="Où déposer ma batterie ?", icon="🗺️")
    with st.popover("🆘 J'ai besoin d'aide"):
        st.write("Pour arrêter le chronomètre, veuillez déposer votre batterie **VoltMinute** dans l'une des bornes **VoltMinute** disponibles dans votre ville.")
    st.write("______")

    # Construction de la date : YYYY-MM-DD/HH:mm
    #time = f"{dt.datetime.now().year}-{dt.datetime.now().month}-{dt.datetime.now().day}/{dt.datetime.now().hour}:{dt.datetime.now().minute}"
    # Construction de la date : HH:mm
    time = f"{dt.datetime.now().hour}:{dt.datetime.now().minute}"

    item_id = "battery001"  # ID de l'item à mettre à jour
    date_start = time

    # Mettre à jour l'heure à laquelle a été prise la batterie dans la BDD
    updated_item = update_item(item_id, date_start)
    print(f"Item mis à jour: {updated_item}")

    chronometer()
    
if __name__ == '__main__':
    main()