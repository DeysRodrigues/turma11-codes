#09/23
#Está sendo desenvolvido um vaso de flores smart, este vaso será capaz de avisar o nível da água (Min, Medio, Max),
#avisar quantas flores estao no vaso, e o mais interessante poderá listar/mencionar os diferentes tipos de flores que
#que estao no vaso
#Identifique as classes, os atributos e métodos correspondentes para resolver o problema

#Flor
### nome
### cor
### altura

#VasoDeFlores
### cor
### nivel_de_agua 
### numero_max_flores
### flores

class Flor:
  def _init_(self, nome, cor, altura):
    self.nome = nome
    self.cor = cor
    self.altura = altura

  # def mostrar(self):
  #   print(f'Nome Flor: {self.nome}\nCor: {self.cor}\nAltura(cm): {self.altura}') 

  def _str_(self):
     return f'Nome Flor: {self.nome}\nCor: {self.cor}\nAltura(cm): {self.altura}'


class VasoDeFlores:
  def _init_(self, cor, numero_max_flores):
    self.cor = cor
    self.numero_max_flores = numero_max_flores
    self.nivel_de_agua = 'Vazio'
    self.flores = []


  def adicionar_flor(self, flor):
    self.flores.append(flor)
  
  def obter_numero_flores(self):
    return len(self.flores)
  
  def adicionar_agua(self, nivel):
    self.nivel_de_agua = nivel
  
  def mostrar_flores(self):
    for flor in self.flores:
      print(flor)

  def mostrar_informacao(self):
    print(f'Informacao do Vaso: \nCor: {self.cor}\nNumero Max Flores: {self.numero_max_flores}\nNumero de Flores: {len(self.flores)}')


vaso_de_flores = VasoDeFlores('Verde', 10)
vaso_de_flores.adicionar_flor(Flor('Rosa','vermelha', 30))
vaso_de_flores.adicionar_flor(Flor('Rosa','Branca', 30))
vaso_de_flores.adicionar_flor(Flor('Margarida','branca', 30))

vaso_de_flores.mostrar_informacao()
vaso_de_flores.mostrar_flores()