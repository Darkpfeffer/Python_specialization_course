test_scores = 45, 23, 89, 78, 98, 55, 74, 87, 95, 75

# converting the sequence to a list
test_scores = list(test_scores)

# Sorting the list in reverse
test_scores.sort(reverse=True)

for i in range(0, 3):
    print(test_scores[i])

# expected output: 98, 95, 89