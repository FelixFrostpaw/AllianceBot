from src.configs.configs import configs


def valid_api_key(response):
  if configs['required_api_key_name_string'].lower(
  ) not in response["name"].lower():
    return False

  permissions_set = set(response["permissions"])

  if "account" not in permissions_set:
    return False

  if "characters" not in permissions_set:
    return False

  if "guilds" not in permissions_set:
    return False

  if "progression" not in permissions_set:
    return False

  return True
