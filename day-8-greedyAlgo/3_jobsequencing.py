# Job sequencing Problem

# Given an 2D array Jobs of size Nx3, where Jobs[i][0] represents JobID , Jobs[i][1] represents Deadline , Jobs[i][2] represents Profit associated with that job. Each Job takes 1 unit of time to complete and only one job can be scheduled at a time.



# The profit associated with a job is earned only if it is completed by its deadline. Find the number of jobs and maximum profit.


# Examples:
# Input : Jobs = [ [1, 4, 20] , [2, 1, 10] , [3, 1, 40] , [4, 1, 30] ]

# Output : 2 60

# Explanation : Job with JobID 3 can be performed at time t=1 giving a profit of 40.

# Job with JobID 1 can be performed at time t=2 giving a profit of 20.

# No more jobs can be scheduled, So total Profit = 40 + 20 => 60.

# Total number of jobs completed are two, JobID 1, JobID 3.

# So answer is 2 60.

# Input : Jobs = [ [1, 2, 100] , [2, 1, 19] , [3, 2, 27] , [4, 1, 25] , [5, 1, 15] ]

# Output : 2 127

# Explanation : Job with JobID 1 can be performed at time time t=1 giving a profit of 100.

# Job with JobID 3 can be performed at time t=2 giving a profit of 27.

# No more jobs can be scheduled, So total Profit = 100 + 27 => 127.

# Total number of jobs completed are two, JobID 1, JobID 3.

# So answer is 2 127.

def job_sequencing(jobs):
    jobs.sort(key= lambda x: x[2], reverse=True)
    
    max_deadline = max(job[1] for job in jobs)
    slots = [False] * (max_deadline + 1)
    
    job_count = 0
    max_profit = 0
    
    for job in jobs:
        job_id, deadline, profit = job
        
        for t in range(deadline, 0, -1):
            if not slots[t]:
                slots[t] = True
                job_count += 1
                max_profit += profit
                break
    return job_count, max_profit