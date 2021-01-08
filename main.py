# Wandella Maia 
from pet_shop import Pet_Shop
from atendimento import Orcamento

def manipula_entrada(entrada):
    try:
        data = entrada.split(" ")[0]
        pequeno = entrada.split(" ")[1]
        grande = entrada.split(" ")[2]
        return [data,pequeno,grande]
    except:
        print("Verifique os parâmetro!")
    

def main():
    """Função principal da aplicação.
    """
    # Criando os 3 petshops
    pet_shop_1 = Pet_Shop("Meu Canino Feliz",2,20,40,24,48)
    pet_shop_2 = Pet_Shop("Vai Rex",1.7,15,50,20,55)
    pet_shop_3 = Pet_Shop("Chowchawgas",0.8,30,45,30,45)

    # Criando uma lista de petshops para adicionar mais Pet Shops
    pet_shops = list()
    
    # Adicionando Pet Shops a lista
    pet_shops.append(pet_shop_1)
    pet_shops.append(pet_shop_2)
    pet_shops.append(pet_shop_3)

    while(True):
        # Recebendo entrada do usuário
        teclado = input()

        try:
            # Inserindo dados no contrutor
            pet_atendimento = Orcamento(manipula_entrada(teclado)[0],manipula_entrada(teclado)[1],manipula_entrada(teclado)[2])

            # Resultado
            print("Pet Shop:", pet_atendimento.preco_total(pet_shops)[0], "Preço Total:",pet_atendimento.preco_total(pet_shops)[1])
            break
        except:
            print("ERROR")
            break

    
    
if __name__ == "__main__":
    main()
