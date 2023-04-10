import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def checkRegione():
    return render_template('form.html')

@app.route('/risultati', methods=['GET'])
def risultatiRegione():
    regione = request.args.get('regione')
    df = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv')
    datiRegione = df[df.denominazione_regione == regione.capitalize()]
    if len(datiRegione) == 0:
        table = 'Regione non trovata'
    else:
        table = datiRegione.to_html()
    return render_template('risultato.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)