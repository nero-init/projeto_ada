import main
from datetime import datetime

def main_menu():
    print('=' * 30)
    print('{:^30}'.format('BEM VINDO - SANTA FINANCEIRA'))
    print('=' * 30)
    while True:
        print("\n----- Menu Principal -----")
        print("1. Adicionar novo registro.")
        print("2. Ler registros.")
        print("3. Atualizar rendimentos.")
        print("4. Exportar relatório em CSV.")
        print("5. Exportar relatório em JSON.")
        print("6. Consultar por data.")
        print("7. Consultar por tipo.")
        print("8. Consultar por valor.")
        print("9. Deletar registro.")
        print("0. Sair")

        escolha = input("\nEscolha a opção desejada (0-9): ")

        if escolha == '1':
            solicitar_registro()
        elif escolha == '2':
            print(main.ler_registros())
        elif escolha == '3':
            main.atualizar_rendimentos()
        elif escolha == '4':
            print("\nExportando relatório em CSV:")
            main.exportar_relatorio('csv')
        elif escolha == '5':
            print("\nExportando relatório em JSON:")
            main.exportar_relatorio('json')
        elif escolha == '6':
            data_consulta = input("Informe a data no formato YYYY-MM-DD: ")
            resultados_por_data = main.consultar_por_data(datetime.strptime(data_consulta, '%Y-%m-%d'))
            print(resultados_por_data)
        elif escolha == '7':
            tipo_consulta = input("Informe o tipo a ser consultado: ")
            resultados_por_tipo = main.consultar_por_tipo(tipo_consulta)
            print(resultados_por_tipo)
        elif escolha == '8':
            valor_consulta = float(input("Informe o valor a ser consultado: "))
            resultados_por_valor = main.consultar_por_valor(valor_consulta)
            print(resultados_por_valor)
        elif escolha == '9':
            indice = int(input("Informe o índice do registro a ser deletado: "))
            main.deletar_registro(indice)
        elif escolha == '0':
            print('=' * 30)
            print('{:^30}'.format('Agradecemos pela preferência - SANTA FINANCEIRA'))
            print('=' * 30)
            break
        else:
            print("Opção inválida. Tente novamente.")


def solicitar_registro():
    tipo = input("\n(1) Receita.\n(2) Despesa.\n(3) Investimento.\n \nInforme o tipo digitando a opção por extenso ou número:")
    valor = float(input("Informe o valor: "))
    data_str = input("Informe a data no formato YYYY-MM-DD: ")
    data = datetime.strptime(data_str, '%Y-%m-%d')
    
    main.criar_registro(data, tipo, valor)

if __name__ == "__main__":
    main_menu()
