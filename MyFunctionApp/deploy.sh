RESOURCE_GROUP="VoltMinute2"
LOCATION="westeurope"
STORAGE="voltminute29cfb"
az functionapp create \
    --resource-group $RESOURCE_GROUP \
    --consumption-plan-location $LOCATION \
    --runtime python \
    --runtime-version 3.11 \
    --functions-version 4 \
    --os-type Linux \
    --name FuncVolt \
    --storage-account $STORAGE