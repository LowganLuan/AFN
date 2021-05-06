
# Leitura dos Arquivos
fileReadState     = open('entrada.txt.txt' , 'r')
fileReadAlphabet  = open('automato.txt.txt', 'r')

#Cria arquivo para escrita
fileWrite         = open('saida.txt.txt'   , 'w')

# Leitura das linhas dos arquivos
ReadState    = fileReadState.read()
ReadAlphabet = fileReadAlphabet.read()

# Vetores Que guardam as linhas dos txts
States       = []
StateList    = []
InputList = []

#Vetor que guarda encadeamento
EncadList = []

# Variaveis inicial e final
initial = "i"
final   = "f"

# Colocando as linhas do txt nos vetores
ListStateLines    = ReadState.splitlines()
ListInputLines = ReadAlphabet.splitlines()


EstadoAtual =  0
AntEstado   = 't'
PrxEstado   = 't'
ValAtual    = 't'
AntVal      = 't'
PrxVal      = 't'
boolean     = False
ValAntEst   = 0

# Separando os dados de cada linha por colunas
for line in ListStateLines:
    StateList.append(line.split())

for line in ListInputLines:
    InputList.append(line.split())

#Descobrindo o estado inicial e final
for line in StateList:
    count = len(line) - 1
    if (line[count] == "i" or line[count] == "I"):
        initial = line[0]
        del(line[count])

for line in StateList:
    count = len(line) - 1
if (line[count] == "f" or line[count] == "F"):
    final = line[0]
    del(line[count])

    #Guarda os estados
    States.append(line[0])




#Leitura do alfabeto
for lineInput in InputList:
	if(ValAtual == "Break"):
		print('teste')
		fileWrite.close
		break;
	for lineI in lineInput:
		if(ValAtual == "Break"):
			break;
		for lineState in range(len(StateList)):
			if(PrxVal == 'True'):
				PrxVal = StateList[EstadoAtual][2]
				if(PrxVal == StateList[EstadoAtual][3]):
					EstadoAtual = EstadoAtual + 1
					break
				else:
					EstadoAtual = EstadoAtual + 1
			else:
				PrxVal = StateList[EstadoAtual][1]
			if(lineI == PrxVal):
				PrxVal = 'True'
				boolean = True
				break
			else:
				fileWrite.write(str(InputList[0]) + " -> " + StateList[EstadoAtual][0]+ " -> Rejeitado")
				EstadoAtual = 8
				print('teste2')
				ValAtual = 'Break'
				break;
		if(EstadoAtual == 8):
			EstadoAtual = 0
			break;











