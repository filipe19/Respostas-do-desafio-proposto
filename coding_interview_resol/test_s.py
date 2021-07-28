from service import SPService
from conv_parser import SPParser
from api import API

# Q4 *** --- Realizando testes por meio do framework pytest

   # Testando o método API para tratamento de dados de débito do licenciamento
def test_api_debito_licenciamento():
    api = API("ABC1234", "11111111111", "ConsultaLicenciamento")   
    result = api.fetch() 
    assert bool(result['TaxaLicenciamento']) == True

    # Testando o método função de débito de multa
def test_search_ticket():
    service = SPService(
        debt_option = "ticket",
        license_plate = "ABC1234",
        renavam = "11111111111",
    )
    result = service.debt_search()
    assert bool(result['Multas']) == True


    # Testando o método função de conversão da placa do Mercosul
def test_conversão_placa():
    service = SPService(
        debt_option = "licensing",
        license_plate = "ABC1C34",
        renavam = "11111111111",        
    )
    service.converte_placa()
    result = service.params["license_plate"]
    assert result == "ABC1234"    

