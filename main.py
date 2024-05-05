print("\033[34m", "---------> math game <--------------", "\033[0m")
print("\033[31m", "  --------------------------------", "\033[0m")
multi_table = (input("\nName the table of which i should take test? "))
player_score = 0
emoji = ["👍", "🫡", "🤯", "😍", "😎", "🥵", "💀", "😶‍🌫️", "🐐", "🤑", "🥳🏆🍾"]
comment = [
    "greak work", "Nice work", "Awesome", "you are a genius", "Mr stylish",
    "you are not from this planet", "are you human or ROBOT",
    "I am afraid of you", "you are the TRUE GOAT",
    "your future is money, sorry😅😅 i mean to say BRIGHT!!!",
    "you the CHAMPION!!!"
]
color = [
    "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[33m",
    "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[32m"
]
while True:
  if not multi_table.isdigit():
    print(
        "\033[31m",
        "Please enter only integer number (POSITIVE NUMBER) and TRY AGAIN😕😕",
        "\033[0m")
    multi_table = (input("\nName the table of which i should take test? "))
  elif multi_table.isdigit():
    break

for i in range(11):

  question = (input(f"\n{multi_table} x {i} = "))
  while True:
    if not question.isdigit():
      print(
          "\033[31m",
          "Please enter only integer number (POSITIVE NUMBER) and TRY AGAIN😕😕",
          "\033[0m")
      question = (input(f"\n{multi_table} x {i} = "))
    elif multi_table.isdigit()== True:
      break
  if int(question) % int(multi_table) == 0:
    print(color[i], comment[i], emoji[i], "\033[0m")
    player_score += 1
    if player_score == 10:
      print(f"you got {player_score} out of 10")
      print("\033[32m", "\n----------> GAME OVER <-----------", "\033[0m")

  else:
    print("😕wrong")
    print("your scored", player_score)
    break
