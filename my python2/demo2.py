x = {
    "name": ["roka", "sola", "hima"],
    "math": [19, 18, 20],
    "since": [15, 17, 16],
    "arabic": [18, 19, 17]
}

total_scores = [sum(scores) for scores in zip(x["math"], x["since"], x["arabic"])]


average_scores = [total / 3 for total in total_scores]

for i in range(len(x["name"])):
    print(f"student: {x['name'][i]}, total: {total_scores[i]}, avarege: {average_scores[i]:.2f}")