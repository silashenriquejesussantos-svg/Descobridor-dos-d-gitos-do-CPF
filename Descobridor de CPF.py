CPF_enviado_usuario = "746824890"

if len(CPF_enviado_usuario) != 9:
    print("CPF inválido (precisa ter 9 dígitos iniciais)")

else:
    soma = 0

    for i in range(9):
        numero = int(CPF_enviado_usuario[i])
        multiplicador = 10 - i
        resultado = numero * multiplicador
        soma += resultado

    digito1 = soma * 10 % 11

    if digito1 > 9: 
        digito1 = 0

    cpf_base = CPF_enviado_usuario[:9]
    cpf_com_d1 = cpf_base + str(digito1)

    soma = 0 

    for i in range(10):
        numero = int(cpf_com_d1[i])  
        multiplicador = 11 - i
        resultado = numero * multiplicador
        soma += resultado

    digito2 = soma * 10 % 11

    if digito2 > 9: 
        digito2 = 0

    print(f"Dígitos: {digito1},{digito2}")

    # monta CPF final
    cpf_final = cpf_com_d1 + str(digito2)

    
    if cpf_final[-2:] == f"{digito1}{digito2}":
        print(f"{cpf_final} é válido")
    else:
        print("CPF inválido")
