print("Welcome to Blackjack Advice!\n"
      "Enter 2-10 for numbered cards, 'A' for Aces, 'J' for Jacks, 'Q' for Queens and 'K' for Kings.")
card_one = input("What is your first card? ")
card_two = input("What is your second card? ")
card_three = input("What is your third card? ")




total_value = (card_one + card_two + card_three)
if total_value < 17:
      print("Hit!")
elif total_value < 20:
      print('Stay!')
elif total_value == 21:
      print("Blackjack, you win!")
print(total_value)
