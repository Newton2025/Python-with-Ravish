# Given the participants' score sheet, find the runner-up score

n = 6
scores = [2, 3, 6, 6, 5, 4]
unique_scores = list(set(scores))
runner_up_score = sorted(unique_scores)[-2]
print(runner_up_score)
