def recipe_to_list():

  recipes = []

  with open("recipes.txt", "r") as f:
    line = f.readline().rstrip()

    while (line != ""):
      recipes.append(line)
      line = f.readline().rstrip()

  return recipes

def url_to_list():

  urls = []

  with open("urls.txt", "r") as f:
    line = f.readline().rstrip()

    while (line!=""):
      urls.append(line)
      line = f.readline().rstrip()

  return urls

def get_ingredients(filename):
  ingredients = []

  with open(filename, mode="r",encoding="utf-8") as f:
    line = f.readline().rstrip()

    while (line!=""):
      ingredients.append(line)
      line = f.readline().rstrip()
  return ingredients

def check_matches(filename, match):
  
  the_filename = filename + ".txt"
  
  ingredients = get_ingredients(the_filename)
  

  return any(ingredients[i] == match for i in range(len(ingredients)))

def recipe_search():
  recipes = recipe_to_list()
  urls = url_to_list()
  matches = []
  num_matches = 0
  max_matches = 0
  closest_match = ""
  closest_url = ""

  num_ingredients = int(input("How many ingredients do you have? "))

  if num_ingredients == 0:
    for i in range(len(recipes)):
      print(f"{(i + 1)}. {recipes[i]}")

  else:
    print("Please enter one ingredients one at a time: ")
    num = 0
    while num<num_ingredients:
      match = input()
      matches.append(match)
      num += 1

    for i in range(len(recipes)):
      for j in range(len(matches)):
        if check_matches(recipes[i],matches[j]):
          num_matches+=1

      if num_matches > max_matches:
        max_matches = num_matches
        closest_match = recipes[i] 
        closest_url = urls[i]
      num_matches = 0

    if max_matches == 0:
      print("No bites matched.")
    else:
      print(F"The most optimal recipe for the ingredients you have is: {closest_match} with {max_matches}/{len(matches)} met.")
      print("")
      print("Link to recipe:",closest_url)
      print("")


  return closest_match, closest_url
  

def main():

  my_bites = []
  print("Hello! Welcome to sustainaBite!")

  exit = False

  while not exit:
    choice = input("Would you like to search for a recipe, view saved Bites or exit? (search/Bites/exit) ")

    if choice == "search":

      closest_match, closest_url = recipe_search()
      saved = input ("Would you like to save this recipe? (Y/N) ")

      if saved == "Y":
        my_bites.append(closest_match + " " + closest_url)
        print("Bite saved!")

    elif choice == "Bites":
      for i in range(len(my_bites)):
        print(" ")
        print(f"{(i + 1)}. {my_bites[i]}")
        print(" ")

    elif choice == "exit":
      print("Thanks for using sustainaBite!")
      exit = True
      
main()