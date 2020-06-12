# Variables must be placed on the beginning of the file
# This is because some file may depend on these variables, so we must resolve it first
# Intended to be changeable by users
api_key = "w"

# Intended to not be changeable by users. Prefixxed with '_'
_base_url = "https://api.xendit.co/"

from xendit.models.balance import *
