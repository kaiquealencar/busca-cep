import requests
class ConsultaCep:

    def __init__(self):
        self.url_base = "https://viacep.com.br/ws/"

    def consultar_cep(self, cep):
        if not cep.isdigit() or len(cep) != 8:
            return {"Erro: CEP deve conter 8 digitos numéricos"}
        
        url = f"{self.url_base}{cep}/json"
        response = requests.get(url)
        
        if response.status_code != 200:
            return {"Erro: Falha ao acessar o ViaCEP"}
        
        data = response.json()

        if "erro" in data:
            return {"Erro: CEP não encontrado"}
        
        return data
        
        


        