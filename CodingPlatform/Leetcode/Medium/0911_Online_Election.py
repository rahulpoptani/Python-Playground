'''
You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].
For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.
Implement the TopVotedCandidate class:
    TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
    int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.

Example 1:
    Input
    ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
    [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
    Output
    [null, 0, 1, 1, 0, 0, 1]

Explanation
    TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
    topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
    topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
    topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
    topVotedCandidate.q(15); // return 0
    topVotedCandidate.q(24); // return 0
    topVotedCandidate.q(8); // return 1
'''

from Common.Tags import DESIGN, HASHMAP
import bisect

class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        self.times = times
        self.person_votes = {}
        self.leaders = []
        max_votes = 0
        leader = None

        for person in persons:
            self.person_votes[person] = self.person_votes.get(person, 0) + 1

            if self.person_votes[person] >= max_votes:
                leader = person
                max_votes = self.person_votes[person]

            self.leaders.append(leader)
    
    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]

# Example usage:
topVotedCandidate = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
print(topVotedCandidate.q(3))   # Output: 0
print(topVotedCandidate.q(12))  # Output: 1
print(topVotedCandidate.q(25))  # Output: 1
print(topVotedCandidate.q(15))  # Output: 0
print(topVotedCandidate.q(24))  # Output: 0
print(topVotedCandidate.q(8))   # Output: 1
