RESOURCE_GROUP="VoltMinute"
LOCATION="francecentral"
CONTAINERAPPS_ENVIRONMENT="VoltMinuteContainerAppEnvironment"
APP_NAME="VoltMinuteContainerApp"
REGISTRY_SERVER="VoltMinuteRegistry"
az containerapp up \
  --name $APP_NAME \
  --source . \
  --location $LOCATION \
  --resource-group $RESOURCE_GROUP \
  --registry-server $REGISTRY_SERVER \
  --environment $CONTAINERAPPS_ENVIRONMENT
