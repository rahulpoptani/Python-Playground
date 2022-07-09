'''
Given the names and grades for each student in a class of N students
store them in a nested list and print the name(s) of any student(s) having the second lowest grade in alphabetical order.
Input:
-------
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Output:
-------
Berry
Harry
'''

if __name__ == '__main__':
    listOfScores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        listOfScores.append([name, score])
    scoreSet = set()
    for name, score in listOfScores:
        scoreSet.add(score)
    sortedSet = sorted(scoreSet)
    secondLowestScore = sortedSet[1]
    peopleWithSecondLowestScore = list(filter(lambda x: x[1] == secondLowestScore, listOfScores))
    peopleList = sorted(list(map(lambda x: x[0], peopleWithSecondLowestScore)))
    for x in peopleList:
        print(x)