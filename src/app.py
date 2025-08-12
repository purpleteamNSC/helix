import os
from dotenv import load_dotenv
from pprint import pprint
from api.fireeye import Helix as hf
from api.trellix import Helix as ht


# VARIABLES
load_dotenv()
# FIREEYE
HELIX_ID_FIREEYE = os.getenv("HELIX_ID_FIREEYE")
APIKEY_FIREEYE = os.getenv("APIKEY_FIREEYE")

# XDR
HELIX_ID_XDR = os.getenv("HELIX_ID_XDR") 
CLIENT_ID_XDR = os.getenv("CLIENT_ID_XDR") 
SECRET_XDR = os.getenv("SECRET_XDR") 

# HLX
HELIX_ID_HLX = os.getenv("HELIX_ID_HLX") 
CLIENT_ID_HLX = os.getenv("CLIENT_ID_HLX") 
SECRET_HLX = os.getenv("SECRET_HLX") 


# EXECUTION --------------------------

# FIREEYE
fireeye = hf(HELIX_ID_FIREEYE, APIKEY_FIREEYE)
print(fireeye.environment()) 

# TRELLIX XDR
# trellix_xdr = ht(HELIX_ID_XDR,CLIENT_ID_XDR,SECRET_XDR,'XDR')
# print(trellix_xdr.environment())

# TRELLIX HLX
# trellix_hlx = ht(HELIX_ID_HLX,CLIENT_ID_HLX,SECRET_HLX,'HLX')
# print(trellix_hlx.environment())
