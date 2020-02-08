**Problem Statement** 

Given a list of tuples in the form `[(start1, end1), (start2, end2), (start3, end3)....(startn, endn)]` where start and end are positive integers. Each tuple is to represent a time window, for example: `[(1, 3), (73, 80)...]`. Find the time (integer) where max concurrency occurs and get the tuples where max concurrency occurs.

Constraints:

 1. `start` and `end` are integers of time and are between 0 to n
 2. For all cases `start` < `end`
 3. `start` is inclusive but `end` is exclusive
 4. For the time (integer) where maximum concurrency occurs, we can get only one if there are multiple cases

For example the schedule below will have max_concurrency at time 2 and the tuples are (0,3), (2,3), (1, 200) that have it.

    schedule = [
                (0, 3),
                (3, 5),
                (2, 3),
                (6, 8),
                (10, 12),
                (73, 92),
                (1, 200),
                ]
