import os
from dotenv import load_dotenv
from pprint import pprint
from fireeye import Helix as hf
from trellix import Helix as ht

# VARIABLES
load_dotenv()
HELIX_ID = os.getenv("HELIX_ID")
APIKEY = os.getenv("APIKEY")


# EXECUTION
fireeye_tennat = hf(HELIX_ID, APIKEY)
trellix_tennat = ht()

print(trellix_tennat)
