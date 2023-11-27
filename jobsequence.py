def job_sequencing(job_count, job_names, deadlines, profits):
    # Combine job details into a list of tuples
    jobs = list(zip(job_names, deadlines, profits))

    # Sort jobs based on profits in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Initialize arrays to track selected jobs and their profits
    selected_jobs = [False] * job_count
    job_sequence = []

    # Iterate through the sorted jobs and select the ones that meet the deadline constraints
    for job in jobs:
        deadline = job[1]
        # Find the latest available slot for the job
        while deadline > 0 and selected_jobs[deadline - 1]:
            deadline -= 1

        # If a slot is available, select the job
        if deadline > 0:
            selected_jobs[deadline - 1] = True
            job_sequence.append(job[0])

    # Join the job names into a space-separated string
    result = ' '.join(job_sequence)
    return result

# Take user input for job details
job_count = int(input())
job_names = input().split()
deadlines = list(map(int, input().split()))
profits = list(map(int, input().split()))

# Call the function and print the result
result = job_sequencing(job_count, job_names, deadlines, profits)
print(result)
