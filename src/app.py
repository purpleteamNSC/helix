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

# v1 ------- 
# alertas_keys = fireeye_tennat.teste().keys()
# alertas= fireeye_tennat.teste().get('alerts',[])
# alerta= fireeye_tennat.teste().get('alerts',[])[0]

# pprint(alerta)

# v2 -------
alertas_keys = fireeye_tennat.teste().keys()
alertas = fireeye_tennat.teste().get('results',[])
alerta = fireeye_tennat.teste().get('results',[])[0]
pprint(alerta)