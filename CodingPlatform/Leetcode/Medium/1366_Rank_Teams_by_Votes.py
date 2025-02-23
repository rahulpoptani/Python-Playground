'''
In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition.
The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.
You are given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.
Return a string of all teams sorted by the ranking system.

Example 1:
Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: 
Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.

Example 2:
Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation:
X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, but X has one vote in the second position, while W does not have any votes in the second position. 

Example 3:
Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter, so their votes are used for the ranking.
'''

from typing import List
from collections import defaultdict

def rankTeams(votes: List[str]) -> str:
    if not votes: return ""
    
    rank = defaultdict(lambda: [0] * len(votes[0]))

    for vote in votes:
        for i, team in enumerate(vote):
            rank[team][i] += 1
    
    sorted_teams = sorted(rank.keys(), key=lambda x: (rank[x], -ord(x)), reverse=True)

    return "".join(sorted_teams)


print(rankTeams(votes = ["ABC","ACB","ABC","ACB","ACB"]))
print(rankTeams(votes = ["WXYZ","XYZW"]))
print(rankTeams(votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))