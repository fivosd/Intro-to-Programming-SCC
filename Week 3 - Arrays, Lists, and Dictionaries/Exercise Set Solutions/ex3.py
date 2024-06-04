# the list and dictionary
list = ["VB", "V0-", "V0", "V0+", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10"]
dict = {"VB": 1,
        "V0-": 2,
        "V0": 3,
        "V0+": 4,
        "V1": 5,
        "V2": 6,
        "V3": 7,
        "V4": 8,
        "V5": 9,
        "V6": 10,
        "V7": 11,
        "V8": 12,
        "V9": 13,
        "V10": 14
        }
# loop using range since we need numbers
for i in range(0, len(list)):
    # replace with a dict reference
    list[i] = dict[list[i]]

# print used for debugging
for j in list:
    print(j)
