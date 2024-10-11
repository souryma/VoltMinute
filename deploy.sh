RESOURCE_GROUP="VoltMinute"
LOCATION="francecentral"
CONTAINERAPPS_ENVIRONMENT=""
APP_NAME="VoltMinuteRegistry"
REGISTRY_SERVER=""
az containerapp up \
  --name $APP_NAME \
  --source . \
  --location $LOCATION \
  --resource-group $RESOURCE_GROUP \
  --registry-server $REGISTRY_SERVER \
  --environment $CONTAINERAPPS_ENVIRONMENT
