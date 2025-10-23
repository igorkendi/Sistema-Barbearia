funcionarios = []

while True:
    print(" MENU ")
    print("1. cadastrar funcionário")
    print("2. gerar relatório")
    print("3. sair")

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        nome = input("nome: ")
        tipo = input("tipo\n 1. estagiario\n 2. clt\n 3. freelancer\n ")

        if tipo == "1":
            salario = float(input("salário fixo: "))
            salario_bruto = salario
            desconto_inss = 0
            desconto_irrf = 0
            salario_liquido = salario

        elif tipo == "2":
            salario = float(input("salário bruto: "))
            salario_bruto = salario
            desconto_inss = salario * 0.08
            if salario > 2000:
                desconto_irrf = salario * 0.10
            else:
                desconto_irrf = 0
            salario_liquido = salario - desconto_inss - desconto_irrf

        elif tipo == "3":
            valor_hora = float(input("valor da hora: "))
            horas = float(input("horas trabalhadas: "))
            salario_bruto = valor_hora * horas
            desconto_inss = salario_bruto * 0.05
            desconto_irrf = 0
            salario_liquido = salario_bruto - desconto_inss

        else:
            print("tipo inválido")
            continue

        funcionario = {
            "nome": nome,
            "tipo": tipo,
            "salario_bruto": salario_bruto,
            "desconto_inss": desconto_inss,
            "desconto_irrf": desconto_irrf,
            "salario_liquido": salario_liquido
        }

        funcionarios.append(funcionario)
        print("funcionário cadastrado\n")
elif opcao == "2":
        if len(funcionarios) == 0:
            print("nenhum funcionário cadastrado\n")
        else:
            print("\n relatório de folha de pagamento ")
            total = 0
            for f in funcionarios:
                print("nome:", f["nome"])
                print("tipo:", f["tipo"])
                print(f"salário bruto: R$ {f['salario_bruto']:.2f}")
                print(f"desconto INSS: R$ {f['desconto_inss']:.2f}")
                print(f"desconto IRRF: R$ {f['desconto_irrf']:.2f}")
                print(f"salário líquido: R$ {f['salario_liquido']:.2f}")

                total += f["salario_liquido"]

                print(f"total pago pela empresa: R$ {total:.2f}\n")

    elif opcao == "3":
        print("saindo...")
        break

    else:
      print("opção inválida\n")