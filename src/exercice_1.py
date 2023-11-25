class Voiture():
  def __init__(self) -> None:
    self.marque = 'BMW'
  
  def afficher_marque(self):
    print('Marque:', self.marque)

def main():
  print('Exercice 1:')
  
  voiture_1 = Voiture()
  voiture_1.afficher_marque()

if __name__ == '__main__':
  main()