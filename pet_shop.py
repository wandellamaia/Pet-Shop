# Wandella Maia 

from datetime import date

class Pet_Shop:

    def __init__(self,nome, distancia, preco_cao_pequeno, preco_cao_grande, preco_fds_p,preco_fds_g):# Construtor
        self.nome = nome
        self.distancia = distancia
        self.preco_cao_pequeno = preco_cao_pequeno
        self.preco_cao_grande = preco_cao_grande
        self.preco_fds_p = preco_fds_p
        self.preco_fds_g = preco_fds_g

    # Getters
    def get_nome(self):
        return self.nome

    def get_distancia(self):
        return self.distancia

    def get_preco_cao_pequeno(self):
        return self.preco_cao_pequeno

    def get_preco_cao_grande(self):
        return self.preco_cao_grande

    def get_preco_fds_p(self):
        return self.preco_fds_p

    def get_preco_fds_g(self):
        return self.preco_fds_g

    # Setters
    def set_nome(self,nome):
        self.nome = nome

    def set_distancia(self,distancia):
        self.distancia = distancia

    def set_preco_cao_pequeno(self,preco_cao_pequeno):
        self.preco_cao_pequeno = preco_cao_pequeno

    def set_preco_cao_grande(self,preco_cao_grande):
        self.preco_cao_grande = preco_cao_grande

    def set_preco_fds_p(self,preco_fds_p):
        self.preco_fds_p = preco_fds_p