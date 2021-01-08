# Wandella Maia 

from datetime import date

class Orcamento:

    def __init__(self,data, qt_pequeno,qt_grande):
        self.data = data
        self.qt_pequeno = qt_pequeno
        self.qt_grande = qt_grande

    def dia_semana(self,data):
        dia = data.split('/')[0]
        mes = data.split('/')[1]
        ano = data.split('/')[2]
       
        dias = ['Segunda-feira','Terça-feira',
        'Quarta-feira','Quinta-Feira',
        'Sexta-feira','Sábado','Domingo']

        diaSemana = date(year=int(ano), month=int(mes), day=int(dia))
        
        return dias[diaSemana.weekday()]

    def is_final_semana(self,day):# Retorno booleano para falar se é fds
        
        if (day == "Sábado") or (day == "Domingo"):
            return True
        else:
            return False


    def calcula_preco(self,flag, pet_shops):# Retorna uma lista de preços e cada posição corresponde ao pet shop
       
        try:

            precos = list()
        
            if flag == True: # se a condição for verdadeira, é porque é final de semana
                
                for key in range(len(pet_shops)):
                
                    total = (pet_shops[key].get_preco_fds_g() * int(self.qt_grande)) +\
                        (pet_shops[key].get_preco_fds_p() * int(self.qt_pequeno))

                    
                    precos.append(total)

                return precos
            else:
                for key in range(len(pet_shops)):
                    
                    total = (pet_shops[key].get_preco_cao_grande() * int(self.qt_grande)) +\
                        (pet_shops[key].get_preco_cao_pequeno() * int(self.qt_pequeno))
                    
                    
                    precos.append(total)

                return precos
        except ValueError:
            print ('Só é permitido valores inteiros!!!!!!!\n')

    def melhor_pet_shop(self,precos):
        menor_preco = precos[0] # Peguei o menor preço
        
        melhores=list()
        for i in range(len(precos)):
            if precos[i]<=menor_preco: # Verifica se tem valores iguais
                melhores.append(i) # Armazema a posição dos melhor(es)
            
        return melhores

    def o_melhor(self,colocacao,orcamentos,pet_shops):
        #Orcamento é uma lista só com a posição
       
        if len(colocacao)==1:
            # Se tiver somente um elemento na lista, ele será o resultado
            return [pet_shops[colocacao[0]].get_nome(), orcamentos[colocacao[0]]]
        else:
            menor = pet_shops[colocacao[0]].get_distancia()
            posicao = colocacao[0]

            for i in colocacao:
                
                if pet_shops[i].get_distancia() <= menor:
                    menor = pet_shops[i].get_distancia()
                    posicao = i  
            return [pet_shops[posicao].get_nome(), orcamentos[posicao]]


    # Método principal que fará todo o cálculo
    def preco_total(self,lista_pet_shops):
        dia_semana = self.dia_semana(self.data) # Descobre o dia da semana
        final_semana = self.is_final_semana(dia_semana) # Verifica se é final de semana
        orcamentos = self.calcula_preco(final_semana,lista_pet_shops) # Calcula o orçamento
        posicionamento = self.melhor_pet_shop(orcamentos) # Descobre se tem ou não valores iguai
        resultado =  self.o_melhor(posicionamento,orcamentos,lista_pet_shops) # Recebe todo o resultado

        return resultado
