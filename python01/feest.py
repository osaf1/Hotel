vragen = [
  "Wat is je voornaam?",
  "Wat is je achternaam?",
  "Wat neem je mee aan drank?",
  "Wat neem je mee aan eten?"

]



persoon = {
  "voornaam": "",
  "achternaam": "",
  "drank": "",
  "eten": "",
}

persoon["voornaam"] = input("1. Wat is je voornaam?\n")
persoon["achternaam"] = input("2. wat is je achternaam?\n")
persoon["drank"] = input("3. wat neem je mee aan drank?\n")
persoon["achternaam"] = input("4. wat neem je aan eten?\n")
print("Bedankt voor het invullen!")
print("see you at the party\n")
with open("feestgangers.txt", "a") as f:
    f.write("----\n")
    f.write(f"voornaam: {persoon['voornaam']}\n")
    f.write(f"achternaam: {persoon['achternaam']}\n")
    f.write(f"drank: {persoon['drank']}\n")
    f.write(f"eten: {persoon['eten']}\n")


