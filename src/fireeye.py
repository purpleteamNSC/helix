import requests


class Helix:
    def __init__(self, helix_id, apikey):
        self.helix_id = helix_id
        self.apikey = apikey
        self.headers = {
            "Content-Type": "application/json",
            "x-fireeye-api-key": self.apikey,
        }
        self.base_url = f"https://apps.fireeye.com/helix/id/{self.helix_id}/api"


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


    def del_search(self, id):
        resource = f"{self.base_url}/v1/search/archive/{id}"
        try:
            res = requests.delete(url=resource, headers=self.headers)
            res.raise_for_status
            return res.json()
        except Exception as e:
            return "Erro ao buscar as pesquisas executadas"


    def del_search_all(self):
        resource = f"{self.base_url}/v1/search/archive/"
        try:
            res = requests.delete(url=resource, headers=self.headers)
            if res.status_code == 204:
                return "Todas as pesquisas executadas foram excluidas"
            return res.json()
        except:
            return "Error ao tentar excluir todas as pesquisas executadas"
