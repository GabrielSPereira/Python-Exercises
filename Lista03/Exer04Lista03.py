# Questão 4. Uma empresa de ônibus com 48 poltronas (24 nas janelas e 24 no corredor). 
# Faça um programa que controle o uso das poltronas ocupadas no corredor e na janela. Considere que 0 
# representa poltrona desocupada e 1, poltrona ocupada. Inicialmente, todas as poltronas estarão livres. 
# Depois disso, o programa deverá exibir as seguintes opções:
# --- 1 - Vender passagens
# --- 2 - Mostrar mapa de ocupações do ônibus
# --- Quando a opção escolhida for Vender passagens, deverá ser perguntado se o usuário deseja janela ou 
# corredor e o número da poltrona.
# --- O programa deverá dar uma das seguintes mensagens:
# --- --- Venda efetivada (se a poltrona solicitada estiver livre, marcando-a como ocupada).
# --- --- Poltrona ocupada (se a poltrona não estiver disponível para a venda).
# --- --- Ônibus lotado (quando todas as poltronas estiverem ocupadas).

corredor = list()
janelas = list()
for contador in range(1, 2):
    if contador % 2 == 0:
        corredor.append(contador)
    else:
        janelas.append(contador)
while True:
    print(f"1 - Vender passagens.\n"
        f"2 - Mostrar mapa de ocupações do ônibus.\n"
        f"3 - Sair.\n")
    escolha = int(input('Digite a opção:\n'))
    if escolha == 3:
        break
    elif escolha == 1:
        if len(janelas) == 0 and len(corredor) == 0:
            print("Ônibus cheio")
        else:
            while True:
                poltrona = int(input("Escolha sua poltrona:\n"))
                if poltrona in janelas:
                    confirmar = str(input("Confirma a compra da poltrona (S ou N)\n"))
                    if confirmar == 'S':
                        janelas.remove(poltrona)
                    break    
                elif poltrona in corredor:
                    confirmar = str(input("Confirma a compra da poltrona (S ou N)\n"))
                    if confirmar == 'S':
                        corredor.remove(poltrona)
                    break
                else:
                    if poltrona <= 48 and poltrona > 0:
                        print("Poltrona ocupada")
                    else:
                        print("Poltrona não encontrada")
    elif escolha == 2:
        print("---JANELA---")
        for cadeira in janelas:
            print(cadeira,"  ")
        print("\n---CORREDOR---")
        for cadeira in corredor:
            print(cadeira,"  ")
