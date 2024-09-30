## [ THESE ARE DEBUG VALUES ] ##

# The Google user ids of the teachers (for the /admin page)
teacher_ids = ['109529716394546071085']
# Random secret key used for encrypting JWT tokens
secret_key = b"&P^B3B4>d;4xs2:n.hbz"
# The address of the database
db_address = "sqlite:///users.db"

## [OAUTH] ##

# The external URL of the server used for oauth
external_url = "http://localhost:8080"
# Google OAuth2 client id and secret
client_id = "416427214351-34b5ajfor3i8mbd13dp7ku3av4tscqlc.apps.googleusercontent.com"
client_secret = "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"
# Logins with emails that don't end with this will be rejected
required_email_prefix = "" # @bernardsboe.com

## [SERVER] ##

host = "localhost"
port = 8080
debug = True
