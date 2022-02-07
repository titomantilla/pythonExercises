#Piedra, papel o tijera

welcomeMessage = "Piedra Papel o Tijera"
userName = 0
userWins = 0
cpuWins = 0
userPick = 0
cpuPick = ["Rock", "Paper", "Scissors"] # List so the random library can choose the CPU options at random

print(welcomeMessage.center(20,"+"))
print("What is your name?")
userName = input()
print("Welcome %s to the rock paper scissors game")
print("Choose - Rock - Paper - Scissors")
try:
    print("%sRock, paper or Scissors?",userName)
    userPick = input()


