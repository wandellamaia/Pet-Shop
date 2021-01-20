********************************************************************
			 				Conteúdo
********************************************************************
A pasta contém 3 arquivos cujos nomes são: "main.py", "pet_shop.py" e 
"atendimento.py"

********************************************************************
							Alguns detalhes
********************************************************************
Premissas assumidas:

- Na descrição do projeto há apenas 3 Pet Shops. Eles tem alguns preços
pre-definidos mas pra alguns deixei seus respectivos valores calculado.
Pode-se usar como exemplo o Pet Shop "Meu Canino Feliz". A descri_
ção diz que aos finais de semana há um acrescimo de 20% no preço. Com
isso, pode-se assumir que os Pet Shops já terão seus valores definidos.
Vale ressaltar que os 20% foram calculados ao colocar no projeto.

Segue exemplo abaixo:

EX: Pet_Shop("Meu Canino Feliz",2,20,40,24,48)

- Assume-se que só número inteiros para a quantidade de cachorro.

Decisões de projeto: 

- A linguagem escolhida foi o Python e a biblioteca utlizado foi 
datetime para trabalhar melhor com o dado do tipo data.

- Na descrição cada Pet Shop tem sua política de preço e cada uma pos_
sui 4 tipos de preço(cachorro pequeno e grande nos dias úteis e final_
de semana) e não menciona explicitamente qual estrutura e como se deve
 aramazenar as informações. Sendo assim, tomou-se a decisão de adicionar
os atributos à classe Pet Shop para facilitar a manipulação.

- A decisão mais importante foi manipular o resultado
para que o algoritmo conseguisse tomar a decisão de qual Pet Shop
melhor atende os critérios.

********************************************************************
		Informações técnicas (ATENÇÃO!!!)
********************************************************************
- Python 3
- Linux Ubuntu 16.04 LTS

****************************************************************************
	Instruções para executar o sistema (ATENÇÃO!!!)
****************************************************************************
Passo a Passo para a execução do programa:

1 - Ao descompactar a pasta de nome "prova_dti" clique com o botão
direito sobre esta pasta e clique na opção "Abrir em um terminal".
OBSERVAÇÃO:VAI ABRIR UM TERMINAL COM UM DIRETORIO PARECIDO COM o
exemplo abaixo:
wandella@wandella-Lenovo-ideapad-310-15ISK:~/Área de Trabalho/prova_dti$ 

2 - Na frente deste caminho digite o seguinte comando: "Python3 main.py"
EX: wandella@wandella-Lenovo-ideapad-310-15ISK:~/Área de Trabalho/prova_dti$ python3 main.py
OBSERVAÇÃO: O programa estará em execução e precisará de entradas.
	
	2.1 - Digite a Data, quantidade de cachorros pequenos e quan_
		tidade de cachorros grandes, separados com espaço. Em seguida,
		digite ENTER para que a execução comece.
		EX: 06/08/1994 28 25

 	2.2 Por fim sairá um resultado parecido com o exemplo abaixo:
		Ex: Pet Shop: Meu Canino Feliz Preço Total: 1872

****************************************************************************
			Testes (ATENÇÃO!!!)
****************************************************************************
O programa consegue tratar alguns erros como:
- Digitar número float
- Falta de informação como o exemplo: "29/11/2019"

Testes realizados:
- Os preços foram mudados para teste e o resultado foi satisfatório.
- Números grandes
	- "30/11/2019 700 106"
	- "30/11/2019 100 700"


roteiros de teste:

- "30/11/2019 1 1" -> Meu Canino Feliz Valor Total : 72 
- "30/11/2019 0 1" -> ChowChawgas Valor Total : 45 
- "01/12/2019 1 0" -> Vai Rex Valor Total : 20 
- "06/08/1994 0 1" -> Meu Canino Feliz Valor Total : 40

@copyright Wandella Maia
- "25/11/2019 1 0" -> Vai Rex Valor Total : 15 

@copyrigth Wandella Maia
