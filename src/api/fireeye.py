import requests
import json

class Helix:
    def __init__(self, helix_id, apikey):
        self.helix_id = helix_id
        self.apikey = apikey
        self.headers = {
            "Content-Type": "application/json",
            "x-fireeye-api-key": self.apikey,
        }
        self.base_url = f"https://apps.fireeye.com/helix/id/{self.helix_id}/api"

    # ENVIROMENT
    def environment(self):
        resource = f"{self.base_url}/v1/environment"
        try:
            res = requests.get(url=resource, headers=self.headers)
            res.raise_for_status
            return res.json()
        except Exception as e:
            return 'Error ao buscar o environment'


    # PEGA TODAS AS QUERYS EXECUTADAS NA CONSOLE
    def get_archives(self):
        """
        _url web :
        https://apps.fireeye.com/helix/id/tenant_id/archive-search
        """
        resource = f"{self.base_url}/v1/search/archive"
        try:
            res = requests.get(url=resource, headers=self.headers)
            res.raise_for_status
            return res.json()
        except Exception as e:
            print(e)


    # DELETA UMA PESQUISA ESPECIFICA
    def del_search(self, id):
        resource = f"{self.base_url}/v1/search/archive/{id}"
        try:
            res = requests.delete(url=resource, headers=self.headers)
            res.raise_for_status
            return res.json()
        except Exception as e:
            return "Erro ao buscar as pesquisas executadas"


    # DELETA TODAS AS QUERY
    def del_search_all(self):
        resource = f"{self.base_url}/v1/search/archive/"
        try:
            res = requests.delete(url=resource, headers=self.headers)
            if res.status_code == 204:
                return "Todas as pesquisas executadas foram excluidas"
            return res.json()
        except:
            return "Error ao tentar excluir todas as pesquisas executadas"

    ## ALERTAS

    # PEGA TODOS OS ALERTAS NA VERSAO LEGACY
    def get_alerts_v1(self):
        resource = f"{self.base_url}/v1/alerts"

        query_filter = {"state": {"$in": ["Open"]}}

        query_str = json.dumps(query_filter)

        params = {"query": query_str}

        try:
            res = requests.get(url=resource, headers=self.headers, params=params)
            res.raise_for_status
            return res.json()
        except:
            return "Error ao tentar buscar os alertas na versao 2"

    
    # PEGA ALERTAS POR NOME DO ALERTA
    def get_alerts_by_name_v1(self, name):
        resource = f"{self.base_url}/v1/alerts"

        query_filter = {"state":{"$in":["Open"]},"message":f"{name}"}

        query_str = json.dumps(query_filter)

        params = {"query": query_str}

        try:
            res = requests.get(url=resource, headers=self.headers, params=params)
            res.raise_for_status
            return res.json().get('alerts',[])
        except:
            return f"Error ao tentar buscar os alertas como o nome {name}"

    
    # FECHA UM ALERTA POR ID
    def close_alert_by_id(self, id):
        payload = {
            "state" : "Closed"
        }
        
        try:
            resource = f"{self.base_url}/v1/alerts/{id}"
            res = requests.put(url=resource, headers=self.headers, json=payload)
            res.raise_for_status
            
            if res.status_code == 200:
                return f"Alerta {id} Fechado"
            
            return res.json()
        except:
            return f"Error ao tentar buscar os alertas como o id {id}"

    
    # FECHAR VARIOS ALERTAS ABERTOS POR NOME
    def close_alerts_by_name(self, name):
        data = self.get_alerts_v1()
        alertas = data.get('alerts', [])
        count = data['meta']['totalCount']

        if count != 0:
            for alerta in alertas:
                if f"{name}" in alerta['message']:
                    print(self.close_alert_by_id(alerta['displayId']))
        else:
            print('Não existe alerta a serem excluidos')
    
    
    def teste(self):
        resource = f"{self.base_url}/v3/alerts/"

        # query_filter = {
        #     "state": {"$in": ["Open"]}
        #     }

        # query_str = json.dumps(query_filter)

        # params = {
        #     "query":query_str
        # }
        # ---------------------------------------------------
        params = {
            "state": "open", 
            "order_by": "-createDate"
            }

        try:
            res = requests.get(url=resource, headers=self.headers, params=params)
            # res = requests.get(url=resource, headers=self.headers)
            res.raise_for_status
            return res.json()
        except:
            return "Error ao tentar buscar os alertas na versao 2"
