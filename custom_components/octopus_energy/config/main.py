from ..const import CONFIG_MAIN_ACCOUNT_ID, CONFIG_MAIN_API_KEY, CONFIG_MAIN_LIVE_ELECTRICITY_CONSUMPTION_REFRESH_IN_MINUTES, CONFIG_MAIN_LIVE_GAS_CONSUMPTION_REFRESH_IN_MINUTES, CONFIG_MAIN_SUPPORTS_LIVE_CONSUMPTION
from ..api_client import OctopusEnergyApiClient


async def async_validate_main_config(data):
  errors = {}

  client = OctopusEnergyApiClient(data[CONFIG_MAIN_API_KEY])
  account_info = await client.async_get_account(data[CONFIG_MAIN_ACCOUNT_ID])
  
  if (account_info is None):
    errors[CONFIG_MAIN_API_KEY] = "account_not_found"

  if data[CONFIG_MAIN_SUPPORTS_LIVE_CONSUMPTION] == True:

    if data[CONFIG_MAIN_LIVE_ELECTRICITY_CONSUMPTION_REFRESH_IN_MINUTES] < 1:
      errors[CONFIG_MAIN_LIVE_ELECTRICITY_CONSUMPTION_REFRESH_IN_MINUTES] = "value_greater_than_zero"

    if data[CONFIG_MAIN_LIVE_GAS_CONSUMPTION_REFRESH_IN_MINUTES] < 1:
      errors[CONFIG_MAIN_LIVE_GAS_CONSUMPTION_REFRESH_IN_MINUTES] = "value_greater_than_zero"

  return errors