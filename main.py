
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

data_in_dict = {row.letter:row.code for (index, row) in data.iterrows()}


name = input("Enter your name: ").upper()

output = [data_in_dict[letter] for letter in name]
print(output)
