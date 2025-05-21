# N meetings in one room

# Given one meeting room and N meetings represented by two arrays, start and end, where start[i] represents the start time of the ith meeting and end[i] represents the end time of the ith meeting, determine the maximum number of meetings that can be accommodated in the meeting room if only one meeting can be held at a time.


# Examples:
# Input : Start = [1, 3, 0, 5, 8, 5] , End = [2, 4, 6, 7, 9, 9]

# Output : 4

# Explanation : The meetings that can be accommodated in meeting room are (1,2) , (3,4) , (5,7) , (8,9).

# Input : Start = [10, 12, 20] , End = [20, 25, 30]

# Output : 1

# Explanation : Given the start and end time, only one meeting can be held in meeting room.

def maxMeetings(start, end):
    n = len(start)
    meetings = [(start[i], end[i]) for i in range(n)]
    
    meetings.sort(key=lambda x: x[1])
    
    count = 1
    last_end = meetings[0][1]
    
    for i in range(1,n):
        if meetings[i][0] > last_end:
            count += 1
            last_end = meetings[i][1]
    
    return count