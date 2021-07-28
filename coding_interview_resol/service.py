from api import API


class SPService:
    
    """
    Conecta com o webservice do Detran-SP.
    """

    def __init__(self, **kwargs):
    
        """
        Construtor.
        """
        self.params = kwargs


    def get_json_response(self, method):
    
        """
        Pega a resposta da requisição em json.
        """
    
        api = API(self.params["license_plate"], self.params["renavam"], method)        
        
        return api.fetch()


    def converte_placa(self):

        """
        Converte string da placa do modelo Mercosul em modelo Placa Cinza, conforme a opção passada.
        """

        lista_placa = list(self.params["license_plate"])
        #print(lista_placa) # Lista placa antes da conversão

        verif = str(lista_placa[4]) # Selecionando o quarto caracter da lista da placa "0","1","2","4","5","6","7"
        #print(verif)

            # Q3 *** --- Implementação da conversão entre modelos de placa: Mercosul ----> Cinza  
            # Embora existam outras formas simples de realizar esta conversão, como utilizar a tabela ASCII, optei por implementar seguinte solução:     
        
        if (verif == 'A' or verif == '0'):
            lista_placa[4] = 0

        elif (verif == 'B' or verif == '1'):            
            lista_placa[4] = 1

        elif (verif == 'C' or verif == '2'): 
            lista_placa[4] = 2
            #print(lista_placa)
        
        elif (verif == 'D' or verif == '3'):
            lista_placa[4] = 3

        elif (verif == 'E' or verif == '4'):
            lista_placa[4] = 4

        elif (verif == 'F' or verif == '5'):
            lista_placa[4] = 5

        elif (verif == 'G' or verif == '6'):
            lista_placa[4] = 6

        elif (verif == 'H' or verif == '7'):
            lista_placa[4] = 7

        elif (verif == 'I' or verif == '8'):
            lista_placa[4] = 8
        
        elif (verif == 'J' or verif == '9'):
            lista_placa[4] = 9
        
        else:
            raise Exception("veículo ñ encontrado") # or: return None

            # temos então a string da lista da placa convertida
        Convertida = ''.join(str(e) for e in lista_placa)
        #print(Convertida)
        
            # Atualizando a informação equivalente:
        self.license_plate = Convertida
        #print(self.license_plate)
      #  print(self.params) # Dicionário com os dados antes de atualizar 
            
        self.params.update({'license_plate':self.license_plate}) # Substituindo o value da chave 'placa' no Dicionário           
      #  print(self.params) # Vemos o Dicionário foi atualizado: Placa Mercosul ---> Placa Cinza 


    def debt_search(self):

        # Converte o value da placa modelo mercosul ---> modelo cinza
        self.converte_placa()

        """
        Pega os débitos de acordo com a opção passada.
        """

        if self.params['debt_option'] == 'ticket':
                response_json = self.get_json_response("ConsultaMultas")
                debts = {'Multas': response_json.get('Multas')}

        # Q2 *** -- Adicionando a opção de Licenciamento:   
            # Retornando as chaves “amount”, “title”, “description”, “year" e “type”. Seu “debt_option” e seu “type" devem ser “licensing”.  
        elif self.params['debt_option'] == 'licensing':
                response_json = self.get_json_response("ConsultaLicenciamento")
                debts = {'licenciamentos': [{'TaxaLicenciamento': response_json.get('TaxaLicenciamento'), 'Exercicio': response_json.get('Exercicio')}]}


        elif self.params['debt_option'] == 'ipva':
                response_json = self.get_json_response("ConsultaIPVA")
                debts = {'IPVAs':  response_json.get('IPVAs')}                

        elif self.params['debt_option'] == 'dpvat':
                response_json = self.get_json_response("ConsultaDPVAT")
                debts = {'DPVATs': response_json.get('DPVATs')}
        
            # Q1 *** -- Para listar as três opções:    
        elif self.params['debt_option'] == 'geral':
                response_json1 = self.get_json_response("ConsultaDPVAT")
                response_json2 = self.get_json_response("ConsultaIPVA")
                response_json3 = self.get_json_response("ConsultaMultas")
        
                debts = {   'DPVATs': response_json1.get('DPVATs'),
                            'IPVAs':  response_json2.get('IPVAs'),    
                            'Multas': response_json3.get('Multas')}      
                
                    
        else:
            raise Exception("opçãoo inválida")


        for debt in debts:
            if debts[debt] == {}:
                debts[debt] = None

        return debts