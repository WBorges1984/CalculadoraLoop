def calculadora():
    while True:
        
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        
        escolha = input("Digite o número para a operação desejada: ")

        
        if escolha not in ['0', '1', '2', '3', '4']:
            print("Essa opção não existe. Tente novamente.\n")
            continue

        
        if escolha == '0':
            print("Programa encerrado.")
            break

        try:
            
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

    
            if escolha == '1':
                resultado = num1 + num2
            elif escolha == '2':
                resultado = num1 - num2
            elif escolha == '3':
                resultado = num1 * num2
            elif escolha == '4':
            
                resultado = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"

        
            print("Resultado:", resultado)
        
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números.\n")
            continue

if __name__ == "__main__":
    calculadora()
