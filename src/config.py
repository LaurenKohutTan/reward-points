import tomllib

raw_config = open("config.toml").read()
config = tomllib.loads(raw_config)

# The Google user ids of the teachers (for the /admin page)
teacher_ids = config["teacher_ids"]
# Random secret key used for encrypting JWT tokens
secret_key = config["secret_key"]
# The address of the database
db_address = config["db_address"]

## [OAUTH] ##

# The external URL of the server used for oauth
external_url = config["external_url"]
# Google OAuth2 client id and secret
client_id = config["client_id"]
client_secret = config["client_secret"]
# Logins with emails that don't end with this will be rejected
required_email_prefix = config["required_email_prefix"]

## [SERVER] ##

host = config["host"]
port = config["port"]
debug = config["debug"]
