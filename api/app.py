from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        anexo = int(request.form.get("anexo"))

        rbt12 = float(request.form.get("rbt12").replace(".","").replace(",","."))
        receita_mensal = float(request.form.get("receita_mensal").replace(".","").replace(",","."))

        resultado = calcular_impostos(anexo, rbt12, receita_mensal)
        return render_template("index.html", resultado=resultado)

    return  render_template("index.html")

def calcular_impostos(anexo, rbt12, receita_mensal):
    resultado = {
        'anexo': anexo,
        'rbt12': rbt12,
        'aliquota_efetiva': 0.0,
        'receita_mensal': receita_mensal,
        'imposto_das': 0.0
    }
# ANEXO I -  COMÉRCIO
    if anexo == 1:
        if rbt12 > 0 and rbt12 <= 180000:
            aliq_efet = 0.04
        elif rbt12 > 180000 and rbt12 <= 360000:
            aliq_efet = (rbt12 * 0.073 - 5940) / rbt12
        elif rbt12 > 360000 and rbt12 <= 720000:
            aliq_efet = (rbt12 * 0.095 - 13860) / rbt12
        elif rbt12 > 720000 and rbt12 <= 1800000:
            aliq_efet = (rbt12 * 0.107 - 22500) / rbt12
        elif rbt12 > 1800000 and rbt12 <= 3600000:
            aliq_efet = (rbt12 * 0.143 - 87300) / rbt12
        elif rbt12 > 3600000 and rbt12 <= 4800000:
            calc_iss = ((rbt12 * 0.19 - 378000) / rbt12) * 0.335
            iss_excedente = calc_iss * receita_mensal
            aliq_efet = ((rbt12 * 0.33 - 648000) / rbt12) + calc_iss
        resultado['imposto_das'] = receita_mensal * aliq_efet
        resultado['aliquota_efetiva'] = aliq_efet

        print("Anexo III - Alíquota Efetiva:", aliq_efet)
        print("Anexo III - Imposto DAS: {:.2f}".format(resultado['imposto_das']))

    # ANEXO II -  INDUSTRIA
    elif anexo == 2:
        if rbt12 > 0 and rbt12 <= 180000:
            aliq_efet = 0.045
        elif rbt12 > 180000 and rbt12 <= 360000:
            aliq_efet = (rbt12 * 0.078 -  5940) / rbt12
        elif rbt12 > 360000 and rbt12 <= 720000:
            aliq_efet = (rbt12 * 0.10 - 13860) / rbt12
        elif rbt12 > 720000 and rbt12 <= 1800000:
            aliq_efet = (rbt12 * 0.112 - 22500) / rbt12
        elif rbt12 > 1800000 and rbt12 <= 3600000:
            aliq_efet = (rbt12 * 0.147 - 85500) / rbt12
        elif rbt12 > 3600000 and rbt12 <= 4800000:
            calc_iss = ((rbt12 * 0.21 - 125640) / rbt12) * 0.335
            iss_excedente = calc_iss * receita_mensal
            aliq_efet = ((rbt12 * 0.33 - 648000) / rbt12) + calc_iss
        resultado['imposto_das'] = receita_mensal * aliq_efet
        resultado['aliquota_efetiva'] = aliq_efet

        print("Anexo III - Alíquota Efetiva:", aliq_efet)
        print("Anexo III - Imposto DAS: {:.2f}".format(resultado['imposto_das']))


    elif anexo == 3:
        if rbt12 > 0 and rbt12 <= 180000:
            aliq_efet = 0.06
        elif rbt12 > 180000 and rbt12 <= 360000:
            aliq_efet = (rbt12 * 0.112 - 9360) / rbt12
        elif rbt12 > 360000 and rbt12 <= 720000:
            aliq_efet = (rbt12 * 0.135 - 17640) / rbt12
        elif rbt12 > 720000 and rbt12 <= 1800000:
            aliq_efet = (rbt12 * 0.16 - 35640) / rbt12
        elif rbt12 > 1800000 and rbt12 <= 3600000:
            aliq_efet = (rbt12 * 0.21 - 125640) / rbt12
        elif rbt12 > 3600000 and rbt12 <= 4800000:
            calc_iss = ((rbt12 * 0.21 - 125640) / rbt12) * 0.335
            iss_excedente = calc_iss * receita_mensal
            aliq_efet = ((rbt12 * 0.33 - 648000) / rbt12) + calc_iss
        resultado['imposto_das'] = receita_mensal * aliq_efet
        resultado['aliquota_efetiva'] = aliq_efet

        print("Anexo III - Alíquota Efetiva:", aliq_efet)
        print("Anexo III - Imposto DAS: {:.2f}".format(resultado['imposto_das']))

    elif anexo == 4:
        if rbt12 > 0 and rbt12 <= 180000:
            aliq_efet = 0.045
        elif rbt12 > 180000 and rbt12 <= 360000:
            aliq_efet = (rbt12 * 0.09 - 8100) / rbt12
        elif rbt12 > 360000 and rbt12 <= 720000:
            aliq_efet = (rbt12 * 0.102 - 12420) / rbt12
        elif rbt12 > 720000 and rbt12 <= 1800000:
            aliq_efet = (rbt12 * 0.14 - 39780) / rbt12
        elif rbt12 > 1800000 and rbt12 <= 3600000:
            aliq_efet = (rbt12 * 0.22 - 183780) / rbt12
        elif rbt12 > 3600000 and rbt12 <= 4800000:
            aliq_efet = (rbt12 * 0.33 - 828000) / rbt12
        resultado['imposto_das'] = receita_mensal * aliq_efet
        resultado['aliquota_efetiva'] = aliq_efet

        print("Anexo IV - Alíquota Efetiva:", aliq_efet)
        print("Anexo IV - Imposto DAS: {:.2f}".format(resultado['imposto_das']))

    elif anexo == 5:
        if rbt12 > 0 and rbt12 <= 180000:
            aliq_efet = 0.155
        elif rbt12 > 180000 and rbt12 <= 360000:
            aliq_efet = (rbt12 * 0.18 - 4500) / rbt12
        elif rbt12 > 360000 and rbt12 <= 720000:
            aliq_efet = (rbt12 * 0.195 - 9900) / rbt12
        elif rbt12 > 720000 and rbt12 <= 1800000:
            aliq_efet = (rbt12 * 0.205 - 17100) / rbt12
        elif rbt12 > 1800000 and rbt12 <= 3600000:
            aliq_efet = (rbt12 * 0.23 - 62100) / rbt12
        elif rbt12 > 3600000 and rbt12 <= 4800000:
            aliq_efet = (rbt12 * 0.305 - 540000) / rbt12
        resultado['imposto_das'] = receita_mensal * aliq_efet
        resultado['aliquota_efetiva'] = aliq_efet

        print("Anexo V - Alíquota Efetiva:", aliq_efet)
        print("Anexo V - Imposto DAS: {:.2f}".format(resultado['imposto_das']))

    return resultado

if __name__ == '__main__':
    app.run()