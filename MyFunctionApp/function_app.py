import azure.functions as func
import logging
import json
from azure.cosmos import CosmosClient, PartitionKey

# Cosmos DB configuration
COSMOS_URI = "https://voltminuteserver.documents.azure.com/"
COSMOS_KEY = ""
DATABASE_NAME = "BatteryDatabase"
CONTAINER_NAME = "BatteryTable"

# Initialize Cosmos DB client
client = CosmosClient(COSMOS_URI, COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

app = func.FunctionApp()

@app.route(route="FuncVolt", auth_level=func.AuthLevel.ANONYMOUS)
def FuncVolt(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Azure Function triggered.')

    # Read the battery ID from the request
    battery_id = "battery001"
    

    # Retrieve the item from Cosmos DB
    try:
        item = container.read_item(item=battery_id, partition_key=battery_id)
    except Exception as e:
        logging.error(f"Error retrieving the item: {e}")
        return func.HttpResponse(
            f"Unable to find the battery with ID: {battery_id}.",
            status_code=404
        )

    # Update the isBorrowed field to False
    item["isBorrowed"] = "false"
    updated_item = container.replace_item(item=battery_id, body=item)

    logging.info(f"Battery updated: {updated_item}")
    return func.HttpResponse(
        f"Battery {battery_id} successfully updated.",
        status_code=200
    )