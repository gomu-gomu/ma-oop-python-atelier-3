import datetime

class Animal():
  def __init__(self, race, anne_naissance) -> None:
    self.race= race
    self.anne_naisance = anne_naissance
  
  def calculer_age(self):
    return datetime.date.today().year - self.anne_naisance

def main():
  print('Exercice 2:')

  chien = Animal('Bulldog', 2017)
  age = chien.calculer_age()
  print(f'le chien est {age} an(s)')

if __name__ == '__main__':
  main()