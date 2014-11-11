import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

nouns = ['mailman', 'bullfighter', 'sky', 'floor', 'beach', 'bucaneer']
adjetives = ['sexy', 'silky', 'gorgeous', 'deep', 'flying']

def type_of_drink(quest):
  """
  Returns a dictionary with booleans as values for the question's answers
  """
  answers = {}
  for q in quest:
      ans = raw_input(quest[q])
      if ans[0] == 'y':
          answers[q] = True
      else:
          answers[q] = False
  
  return answers

def make_drink(preferences):
  drink = []
  for flavor in preferences:
      if preferences[flavor] == True:
          drink.append(random.choice(ingredients[flavor]))
  return drink

def drink_name():
  return "Your drink's name is {} {}.".format(random.choice(adjetives),random.choice(nouns))
 
def main():
  select = type_of_drink(questions)
  drink = make_drink(select)
  name = drink_name()
  print "The ingredients in your drink are:"
  for item in drink:
    print "{}".format(item)
  print name

      
    

if __name__ == '__main__':
  main()
  