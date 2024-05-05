print("---------math game--------------")

multi_table = int(input("\nName the table of which i should take test? "))
player_score = 0
emoji = ["👍", "🫡", "🤯", "😍", "😎", "🥵", "💀", "😶‍🌫️", "🐐", "🤑", "🥳🏆🍾"]
comment = [
    "greak work", "Nice work", "Awesome", "you are a genius", "Mr stylish",
    "you are not from this planet", "are you human or ROBOT",
    "I am afraid of you", "you are the TRUE GOAT",
    "your future is money, sorry😅😅 i mean to say BRIGHT!!!",
    "you the CHAMPION!!!"
]
for i in range(11):
  # question = int(input(f"\n{multi_table} x {i} = "))
  print(f"\n{multi_table} x {i} = ", multi_table * i)
  print(comment[i], emoji[i])

# print("---------math game--------------")

# multi_table = int(input("\nName the table of which i should take test? "))
# player_score = 0

# for i in range(11):
#   question = int(input(f"\n{multi_table} x {i} = "))
#   if question % multi_table == 0:
#     print("great work 👍")
#     player_score += 1
#     if player_score ==2:
#       print("Nice move🫡")
#       break
#   else:
#     print("wrong")
#     print("your scored", player_score)
#     break

