import unittest
from unittest.mock import patch 
from service import SPService

# Q6 *** Usando mocks

ipva = {"IPVAs": {
                    "IPVA": [
                                {
                                    "Cota": 8,
                                    "Valor": 136569,
                                    "Exercicio": 2021,
                                },
                                {
                                    "Cota": 2,
                                    "Valor": 101250,
                                    "Exercicio": 2020,
                                }
                            ]
                 },
        }
            

'''
Utilizando Mock para testar o módulo debt_search() do SPService --- sem usar a API / opção débitos de IPVA
'''


service = SPService(
                      debt_option = "ipva",
                      renavam = "11111111111",
                      license_plate = "ABC1C34",    
                    )

@patch('service.SPService.get_json_response')
class MockTest1(unittest.TestCase):
    
    def test_get_json(self, solicit_mock):
        
        make_mock = solicit_mock.start()
        make_mock.return_value = ipva
        
        print(service.debt_search())
        make_mock.stop()
        
        # chamando esse método com esse parâmetro, ele retorna.. ok
        assert bool(service.debt_search()['IPVAs']) == True


# dpvat = {
#             "DPVATs":   {
#                             "DPVAT": [
#                                             {
#                                             "Valor": 523,
#                                             "Exercicio": 2020,
#                                             }
#                                     ]
#                         }
#         }


# '''
# Utilizando Mock para testar o módulo debt_search() do SPService --- sem usar a API / opção débitos de seguro DPVAT
# '''


# service = SPService(
#                         debt_option = "dpvat",
#                         renavam = "11111111111",
#                         license_plate = "ABC1C34",    
#                     )


# @patch('service.SPService.get_json_response')
# class MockTest4(unittest.TestCase):

#     def test4_get_json(self, solicit_mock):
        
#         make_mock = solicit_mock.start()
#         make_mock.return_value = dpvat
        
#         print(service.debt_search())
#         make_mock.stop()
        
#         # chamando esse método com esse parâmetro, ele retorna.. ok
#         assert bool(service.debt_search()['DPVATs']) == True


