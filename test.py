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

def instant_runoff(b):
    results = np.zeros_like(b[0])
    max_votes = 0
    elim_list = []
    elim_round = 1
    while max_votes/len(b) < .5:
        min = [0, 0]
        for ballot in b:
            remainders = [ ix for ix in range(len(ballot)) if ix not in elim_list]
            for canadate in remainders:
                if ballot[canadate] == elim_round:
                    results[canadate] += 1
        for canadate in range(len(results)):
            if results[canadate] < min[1]:
                min =  results[canadate] #finish tie handler and make sure all edge cases are covered
        for canadate in range(len(results)):
            if results[canadate] > max_votes:
                max_votes =  results[canadate] #finish tie handler and make sure all edge cases are covered
        elim_list.append(min[0])
    return(results)

def condorcet_method(b):
    results = np.zeros_like(b[0])



first_past_post(test_ballots)
winners_list = first_past_post(test_ballots)
bourda_winner = bourda_count(test_ballots)
instant_runoff_winner = instant_runoff(test_ballots)

print(winners_list, bourda_winner, instant_runoff_winner)
 