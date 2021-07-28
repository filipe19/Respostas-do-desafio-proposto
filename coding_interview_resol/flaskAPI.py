from flask import Flask
from flask import jsonify
from conv_parser import SPParser
from service import SPService

# Q5 *** Criando uma api simplesutilizando Flask:

# Escrevendo a URL a http://licalhost:portatcp 
# http://12X.0.0.1:5000/
# http://12X.0.0.1:????/debitos
# http://12X.0.0.1:????/debitos/ipva
# http://12X.0.0.1:????/debitos/multas
# http://12X.0.0.1:????/debitos/dpvat
# http://12X.0.0.1:????/debitos/licenciamento

app = Flask(__name__)

service = SPService(
        debt_option = 'geral',
        license_plate = 'ABC1234',
        renavam = '11111111111',
    )

@app.route('/debitos', methods=['GET'])
def debts_geral():
    parser = SPParser(service.debt_search())
    return jsonify(parser.collect_geral_debts()), 200

@app.route('/debitos/<string:debts_option>', methods=['GET'])
def debts_ticket(debts_option):
    if debts_option == 'dpvat':
        service.params['debt_option'] = 'dpvat'
        parser = SPParser(service.debt_search())
        return jsonify(parser.collect_insurance_debts()), 200

    elif debts_option == 'multas':
        service.params['debt_option'] = 'ticket'
        parser = SPParser(service.debt_search())
        return jsonify(parser.collect_ticket_debts()), 200

    elif debts_option == 'ipva':
        service.params['debt_option'] = 'ipva'
        parser = SPParser(service.debt_search())
        return jsonify(parser.collect_ipva_debts()), 200

    elif debts_option == 'licenciamento':
        service.params['debt_option'] = 'licensing'
        parser = SPParser(service.debt_search())
        return jsonify(parser.collect_licensing_debts()), 200

    else:
        return jsonify({'error': 'not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

#@app.route('/debitos', methods=['GET','POST',...])
#def debts_geral():
#    html = ['<ul>']
#    for multas, opcao in api.fetch():
#        html.append(
#            f"<li>a href='/debitos/{multas}'>{opcao['debt_option']}</a></li>"
#        )
#        html.append('</ul>')
#    return '\n' .join(html)

    