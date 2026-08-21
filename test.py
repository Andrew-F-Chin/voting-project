import numpy as np
np.array

def first_past_post(b):
    results = np.zeros_like(b[0])
    for ballot in b:
        for canadate in range(len(ballot)):
            if ballot[canadate] == 1:
                results[canadate] += 1
    return(results)


def bourda_count(b):
    results = np.zeros_like(b[0])
    for ballot in b:
        for canadate in range(len(ballot)):
            results[canadate] += ballot[canadate]
    for canadate in range(len(ballot)):
        results[canadate] = len(ballot) * (len(b) + 1) - results[canadate]
    return(results)

test_ballots = [[1, 2, 3],
                [3, 2, 1],
                [1, 2, 3]]

first_past_post(test_ballots)
winners_list = first_past_post(test_ballots)
bourda_winner = bourda_count(test_ballots)

print(winners_list, bourda_winner)
