
import csv
with open("nato_phonetic_alphabet.csv", "r") as data_file:
    data = csv.reader(data_file)
    # print(data)
    # next(data)

    # --------below code is work just for list item -------

    # data = list(csv.reader(data_file))
    # for row in data[1:]:
    #     print(row)


# -------- another way to do this ---------

    # for row in data:
    #     if row[1] != "letter" and row[1] != "code":
    #         print(row)
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

letter = data.letter
# print(letter)

data_dict = data.to_dict()
# print(data_dict)

proper_dict = {row.letter : row.code for (index, row) in data.iterrows()}
# print(proper_dict)

series_list = data.code.to_list()
# print(series_list)



