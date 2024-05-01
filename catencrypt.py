import lib.catencrypt

catencrypt = lib.catencrypt

cat_writing = """
  ___      ___      _________
 /        /   \\         |
|        /     \\        |
|       /_______\\       |
|      /         \\      |
 \\___ /           \\     |
"""

encrypt_writing = """
 ____ |\\    |   ____  ___    |  /  ___ _______
|     | \\   |  /     |   |   | /  |   |   |
|____ |  \\  | |      |___|   |/   |___|   |
|     |   \\ | |      |   \\   |    |       |
|____ |    \\|  \\____ |    \\  |    |       |
"""

writings = """
  ___      ___      _________
 /        /   \\         |
|        /     \\        |
|       /_______\\       |
|      /         \\      |
 \\___ /           \\     |
 ____ |\\    |   ____  ___    |  /  ___ _______
|     | \\   |  /     |   |   | /  |   |   |
|____ |  \\  | |      |___|   |/   |___|   |
|     |   \\ | |      |   \\   |    |       |
|____ |    \\|  \\____ |    \\  |    |       |
##############################################
"""

def print_logo():
    print(writings)

def main():
    print_logo()
    while True:
        print("")
        print("")
        print("Welcame to catencrypt, select an option: ")
        print("1) generate a key")
        print("2) encrypt data")
        print("3) decrypt data")
        print("exit) exit")
        action = input("action: ")
        print("")
        print("")
        if action == "1":
            print("key: " + catencrypt.generate())
        elif action == "2":
            key = input("insert the encrypt key: ")
            text = input("insert the text to encrypt: ")
            print("encrypted text: " + catencrypt.encrypt(str(text), int(key)))
        elif action == "3":
            key = input("insert the decrypt key: ")
            text = input("insert the text to decrypt: ")
            print("decrypted text: " + catencrypt.decrypt(str(text), int(key)))
        elif action.lower() == "exit":
            break
        else:
            print(f"no action found with ID {action}, please retry")

if __name__ == "__main__":
    main()