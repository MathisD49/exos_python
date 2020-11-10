from texte import HideText, FindText

print("""
 _   __                         _____ _
| | / /                        /  ___| |
| |/ /  ___ _ __  _ __  _   _  \ `--.| |_ ___  __ _  __ _
|    \ / _ \ '_ \| '_ \| | | |  `--. \ __/ _ \/ _` |/ _` |
| |\  \  __/ | | | | | | |_| | /\__/ / ||  __/ (_| | (_| |
\_| \_/\___|_| |_|_| |_|\__, | \____/ \__\___|\__, |\__,_|
                         __/ |                 __/ |
                        |___/                 |___/       """)

print("1 - Hide text")
print("2 - Find text")
print("3 - Hide Image")
print("4 - Find Image")
choice = input("> ")

if choice == "1":
    imagepath = input("image path > ")
    text = input("text > ")

    HideText(imagepath, text)

elif choice == "2":
    imagepath = input("image path > ")
    key = int(input("key > "))

    FindText(imagepath, key)

elif choice == "3":
    pass

elif choice == "4":
    pass 

else:
    print("wrong input")
