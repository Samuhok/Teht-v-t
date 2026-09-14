leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("\nAnna naulat.\n"))
luodit = float(input("\nAnna luodit.\n"))

luotien_maara = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat = luotien_maara * 13.3

kilogrammat = int(grammat // 1000)
grammat = grammat % 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat} grammaa.")