'''
You're given the scores of players on a leaderboard, already sorted in descending order, and your own scores.
ranked = [100, 100, 50, 40, 40, 20, 10]
alice scores = [5, 25, 50, 120]

What is dense ranking?
Dense ranking is a ranking system where players with equal scores receive the same rank, and the next
Example: If the ranked scores are [100, 100, 50, 40, 40, 20, 10], then the ranks would be [1, 1, 2, 3, 3, 4, 5].

First, we need to create a list of unique scores from the ranked list and assign ranks to them. Then, for each of Alice's scores, we will determine her rank by comparing her score to the unique scores.
Alice = 5
Leaderboard: 
100 → 1
50  → 2
40  → 3
20  → 4
10  → 5
5 is below 10. Therefore, Alice's rank is 6.

Alice = 25
Leaderboard:
100 → 1
50  → 2
40  → 3
20  → 4
10  → 5
25 is between 20 and 40. Therefore, Alice's rank is 4.

Alice = 50
Leaderboard:
100 → 1
50  → 2
She ties with the second player. Therefore, Alice's rank is 2.

Alice = 120
Leaderboard:
120 → 1
120 is above 100. Therefore, Alice's rank is 1.

Hence, the final rank for Alice's scores would be [6, 4, 2, 1].
'''
from Common.Tags import ARRAY

def climbingLeaderboard(ranked, player):
    # Create a list of unique scores from the ranked list
    unique_scores = sorted(set(ranked), reverse=True)
    ranks = []
    
    # Initialize the index for unique_scores
    index = len(unique_scores) - 1
    
    for score in player:
        # Move the index down while the player's score is greater than or equal to the unique score
        while index >= 0 and score >= unique_scores[index]:
            index -= 1
        # The rank is the index + 2 (since index is 0-based and we want rank starting from 1)
        ranks.append(index + 2)
    
    return ranks

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))  # Output: [6, 4, 2, 1]