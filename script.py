print("********************************************************")
print("****** CALCULADORA DE IMPOSTOS DO SIMPLES NACIONAL *****")
print("********************************************************")


# Opções de anexos do SN
print("----------------- Escolha um anexo -----------------")

while True:
    try:
        anexo = input("Selecione qual Anexo deseja:\n1 - Anexo I\n2 - Anexo II\n3 - Anexo III\n4 - Anexo IV\n5 - Anexo V\n")
        anexo = int(anexo)
        if anexo in [1, 2, 3, 4, 5]:
            break
        else:
            print("Anexo inválido! Escolha um anexo entre 1 e 5.")
    except ValueError:
        print("Entrada inválida! Escolha um anexo entre 1 e 5.")

# Solicita Receita Bruta Acumulada dos últimos 12 meses
rbt12 = float(input("Informe a Receita Bruta Acumulada dos últimos 12 meses: "))

# Solicita a Receita Mensal
receita_mensal = float(input("Informe a Receita Mensal: "))


# Anexo III

# Prestadores de Serviço | Participantes: empresas que oferecem serviços de instalação, de reparos e de manutenção etc.

# Até R$ 180.000,00	6%	0
# De R$ 180.000,01 a R$ 360.000,00	11,2%	R$ 9.360,00
# De R$ 360.000,01 a R$ 720.000,00	13,5%	R$ 17.640,00
# De R$ 720.000,01 a R$ 1.800.000,00	16%	R$ 35.640,00
# De R$ 1.800.000,01 a R$ 3.600.000,00	21%	R$ 125.640,00
# De R$ 3.600.000,01 a R$ 4.800.000,00	33%	R$ 648.000,00

# Calcula a Alíquota Efetiva
if anexo == 3:
# 1º faixa
    if rbt12 > 0 and rbt12 <= 180000:
        aliq_efet = 0.06
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        # Solicita a Receita Mensal
        receita_mensal = float(input("Informe a Receita Mensal: "))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é {:.2f}".format(das))
    # 2º faixa
    elif rbt12 >180000 and rbt12 <= 360000:
        aliq_efet = (rbt12 * 0.112 - 9360) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R${:.2f} ".format(das))
        # 3º faixa
    elif rbt12 > 360000 and rbt12 <= 720000:
        aliq_efet = (rbt12 * 0.135 - 17640) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R$ {:.2f}".format(das))
    # 4º faixa
    elif rbt12 > 720000 and rbt12 <= 1800000:
        aliq_efet = (rbt12 * 0.16 - 35640) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R$ {:.2f}".format(das))
    # 5º faixa
    elif rbt12 > 1800000 and rbt12 <= 3600000:
        aliq_efet = (rbt12 * 0.21 - 125640) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R$ {:.2f}".format(das))
    # 6º faixa
    elif rbt12 > 3600000 and rbt12 <= 4800000:
        calc_iss = ((rbt12 * 0.21 - 125640) / rbt12) * 0.335
        iss_excedente = calc_iss * receita_mensal
        aliq_efet = ((rbt12 * 0.33 - 648000) / rbt12) + calc_iss
        print("A Alíquota Efetiva é {:.2%}".format(aliq_efet))
        das = (receita_mensal * aliq_efet)
        print("O imposto DAS é R$ {:.2f}".format(das))



# Anexo IV

# Prestadores de Serviço | Participantes: empresas que fornecem serviço de limpeza, vigilância, obras, construção de imóveis, serviços advocatícios

# Até R$ 180.000,00	4,5%	0
# De R$ 180.000,01 a R$ 360.000,00	9%	R$ 8.100,00
# De R$ 360.000,01 a R$ 720.000,00	10,2%	R$ 12.420,00
# De R$ 720.000,01 a R$ 1.800.000,00	14%	R$ 39.780,00
# De R$ 1.800.000,01 a R$ 3.600.000,00	22%	R$ 183.780,00
# De R$ 3.600.000,01 a R$ 4.800.000,00	33%	R$ 828.000,00

# Verfica o anexo escolhido
if anexo == 4:
    # 1º faixa
    if rbt12 > 0 and rbt12 <= 180000:
        aliq_efet = 0.045
        print("A alíquota efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R$ {:.2f}".format(das))
    # 2º faixa
    elif rbt12 > 180000 and rbt12 <= 360000:
        aliq_efet = (rbt12 * 0.09 - 8100) / rbt12
        print("A alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R$ {:.2f}".format(das))
    # 3º faixa
    elif rbt12 >360000 and rbt12 <= 720000:
        aliq_efet = (rbt12 * 0.102 - 12420) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R$ {:.2f}".format(das))
    # 4º faixa
    elif rbt12 > 720000 and rbt12 <= 1800000:
        aliq_efet = (rbt12 * 0.14 - 39780) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R$ {:.2f}".format(das))
    # 5º faixa
    elif rbt12 > 1800000 and rbt12 <= 3600000:
        aliq_efet = (rbt12 * 0.22 - 183780) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R$ {:.2f}".format(das))
    # 6º faixa
    elif rbt12 > 3600000 and rbt12 <= 4800000:
        aliq_efet = (rbt12 * 0.33 - 828000) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O imposto DAS é R$ {:.2f}".format(das))


# ANEXO V

# Prestadores de Serviço | Participantes: empresas que fornecem serviço de auditoria, jornalismo, tecnologia, publicidade, engenharia, entre outros

# Até R$ 180.000,00	15,5%	0
# De 180.000,01 a 360.000,00	18%	R$ 4.500,00
# De 360.000,01 a 720.000,00	19,5%	R$ 9.900,00
# De 720.000,01 a 1.800.000,00	20,5%	R$ 17.100,00
# De 1.800.000,01 a 3.600.000,00	23%	R$ 62.100,00
# De 3.600.000,01 a 4.800.000,00	30,50%	R$ 540.000,00

# Calcula a Alíquota Efetiva

# 1º faixa
if anexo == 5:
    # 1º faixa
    if rbt12 > 0 and rbt12 <= 180000:
        aliq_efet = 0.155
        print("Sua Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O valor do imposto DAS é R$ {:.2f}".format(das))
    # 2º faixa
    elif rbt12 > 180000 and rbt12 <= 360000:
        aliq_efet = (rbt12 * 0.18 - 4500) / rbt12
        print("Sua Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O valor do imposto DAS é R$ {:.2f}".format(das))
    # 3º faixa
    elif rbt12 > 360000 and rbt12 <= 720000:
        aliq_efet = (rbt12 * 0.195 - 9900) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O valor do imposto DAS é R$ {:.2f}".format(das))
    # 4º faixa
    elif rbt12 > 720000 and rbt12 <= 1800000:
        aliq_efet = (rbt12 * 0.205 - 17100) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O valor do imposto DAS é R$ {:.2f}".format(das))
    # 5º faixa
    elif rbt12 > 1800000 and rbt12 <= 3600000:
        aliq_efet = (rbt12 * 0.23 - 62100) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O valor do imposto DAS é R$ {:.2f}".format(das))
    # 6º faixa
    elif rbt12 > 3600000 and rbt12 <= 4800000:
        aliq_efet = (rbt12 * 0.305 - 540000) / rbt12
        print("A Alíquota Efetiva é {}".format(aliq_efet))
        das = receita_mensal * aliq_efet
        print("O valor do imposto DAS é R$ {:.2f}".format(das))
else:
    print("Programa finalizado!")


