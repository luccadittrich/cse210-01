#Tic-Tac-Toe
#Author: Lucca Dittrich
import os

table = [
"⬜", "⬜", "⬜",
"⬜", "⬜", "⬜",
"⬜", "⬜", "⬜"]

#optional:
#Uncomment this method/function and line 19 if you want to clear the terminal each time a player plays
#use "clear" in the parameter in line 15 if you are using linux, or "cls" if you are using windows

#def clear():
#    clear = lambda: os.system('clear')
#    clear()

def print_table(table):
    #clear()

    print()
    print(f"{table[0]}¹ {table[1]}² {table[2]}³")
    print()
    print(f"{table[3]}⁴ {table[4]}⁵ {table[5]}⁶")
    print()
    print(f"{table[6]}⁷ {table[7]}⁸ {table[8]}⁹")

def ask_player(player):
    ask = int(input(f"\nPlayer {player}, choose a square: ")) - 1

    if player == "❌":
       table[ask] = "❌"
    else:
        table[ask] = "🔵"

def winner():
    # check if squares are equal in diagonal
    for i in range(0, 9):
        if (table[0] == table[4] == table[8] != "⬜" ) or (table[2] == table[4] == table[6] != "⬜"):
            if table[i] == "❌":
                print("\n❌ is the winner 🥳")
                return True
            elif table[i] == "🔵":
                print("\n🔵 is the winner 🥳")
                return True

    if "⬜" not in table:
        print("\nDraw")
        return True
    # check if squares are equal in horizontal
    for i in range(0, 7, 3):
        if table[i] == table[i + 1] == table[i + 2] != "⬜":
            if table[i] == "❌":
                print("\n❌ is the winner 🥳")
                return True
            elif table[i] == "🔵":
                print("\n🔵 is the winner 🥳")
                return True

    # check if squares are equal in vertical
    for i in range(0, 2):
        if table[i] == table[i + 3] == table[i + 6] != "⬜":
            if table[i] == "❌":
                print("\n❌ is the winner 🥳")
                return True
            elif table[i] == "🔵":
                print("\n🔵 is the winner 🥳")
                return True

    return False

def main():
    print_table(table)

    while winner() == False:

        ask_player("❌")

        print_table(table)
        print("_" * 10)
        if winner() == True: break

        ask_player("🔵")
        print_table(table)

if __name__ == "__main__":
    main()
