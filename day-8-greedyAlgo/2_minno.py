# Minimum number of platforms required for a railway

# Given the arrival and departure times of all trains reaching a particular railway station, determine the minimum number of platforms required so that no train is kept waiting. Consider all trains arrive and depart on the same day.

# In any particular instance, the same platform cannot be used for both the departure of one train and the arrival of another train, necessitating the use of different platforms in such cases.

# Examples:
# Input : Arrival = [0900, 0940, 0950, 1100, 1500, 1800] , Departure = [0910, 1200, 1120, 1130, 1900, 2000]
# Output : 3

# Explanation : The first , second , fifth number train can use the platform 1.

# The third and sixth train can use the platform 2.

# The fourth train will use platform 3.

# So total we need 3 different platforms for the railway station so that no train is kept waiting.

# Input : Arrival = [0900, 1100, 1235] , Departure = [1000, 1200, 1240]

# Output : 1

# Explanation : All the three trains can use the platform 1.

# So we required only 1 platform.

def find_platform(arr,dep):
    n = len(arr)
    arr.sort()
    dep.sort()
    
    platforms = 1
    max_platforms = 1
    
    i = 1
    j = 0
    
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        max_platforms = max(max_platforms, platforms)
    
    return max_platforms