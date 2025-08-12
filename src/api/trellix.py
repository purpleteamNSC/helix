import requests

class Helix:
    def __init__(self, helix_id,client_id,secret,scope):
        self.helix_id=helix_id
        self.client_id=client_id
        self.secret=secret
        self.scope=scope
    
    # GERA O TOKEN 
    def token(self):
        scope_xdr = 'xdr.alr.r xdr.alr.rw xdr.cc.r xdr.cc.rw xdr.dbr.r xdr.dbr.rw xdr.dp.r xdr.dp.rw xdr.fed.r xdr.fed.rw xdr.hidden.rw xdr.ind.r xdr.ind.rw xdr.intel.rw xdr.org.adm xdr.rul.r xdr.rul.rw xdr.so.r xdr.so.rw xdr.srh.adv xdr.srh.r xdr.srh.rw'
        
        scope_hlx = 'hlx.alr.r hlx.alr.rw hlx.cc.r hlx.cc.rw hlx.dbr.r hlx.dbr.rw hlx.dp.r hlx.dp.rw hlx.fed.r hlx.fed.rw hlx.hidden.rw hlx.ind.r hlx.ind.rw hlx.intel.rw hlx.org.adm hlx.rul.r hlx.rul.rw hlx.so.r hlx.so.rw hlx.srh.adv hlx.srh.r hlx.srh.rw'
        
        scopes = scope_xdr if self.scope.lower() == 'xdr' else scope_hlx
        
        url='https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token'
        
        auth=(self.client_id,self.secret)
        
        headers = {
            "content-type":"application/x-www-form-urlencoded"
        }
        
        data = {
            "scope": scopes,
            "grant_type": "client_credentials"
        }
        
        try:
            res = requests.post(url, auth=auth, headers=headers, data=data)
            res.raise_for_status()
            token = res.json().get('access_token',[])
            return token
        except:
            return 'Error ao gerar token'
        
    def environment(self):
        url = f'https://xdr.trellix.com/helix/id/{self.helix_id}/api/v1/environment'
        
        headers = {
            'x-trellix-api-token': f'Bearer {self.token()}'
        }
        
        try:
            res = requests.get(url, headers=headers)
            res.raise_for_status()
            data = res.json()
            return data
        except:
            return 'Error ao requisitar environment'
    
    def __str__(self):
        return "Helix Trellix - SECDEVOPS TEAM"
