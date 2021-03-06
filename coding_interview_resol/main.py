import sys
import json
from service import SPService
from conv_parser import SPParser



if __name__ == "__main__":

    try:
        debt_option = sys.argv[1]
        license_plate = sys.argv[2]
        renavam = sys.argv[3]
        assert len(sys.argv) == 4
    except NameError as erro:
        print('Argumentos inválidos... Erro encontrado: ', erro)
        sys.exit(1)
 #   print(sys.argv[2])
    service = SPService(
        license_plate=license_plate,
        renavam=renavam,
        debt_option=debt_option
    )
    try:
        search_result = service.debt_search()
    except Exception as exc:
        print(exc)
        sys.exit(1)

    parser = SPParser(search_result)

    if debt_option == "ticket":
        result = parser.collect_ticket_debts()
    elif debt_option == "ipva":
        result = parser.collect_ipva_debts()
    elif debt_option == "dpvat":
        result = parser.collect_insurance_debts()
    elif debt_option == "geral":           # Q1 *** -- Para listar as três opções   
        result = parser.collect_geral_debts()
    elif debt_option == "licensing":         # Q2 *** -- Para listar a opção de Licenciamento anual    
        result = parser.collect_licensing_debts()
    else:
        print("Opção inválida")
        sys.exit(1)

    print(json.dumps(result, indent=4, ensure_ascii=False))
    sys.exit(0)