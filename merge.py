import csv

# Load evaluation data
with open('./res1.csv') as fread:
    csv_data = list(csv.reader(fread))

# Load participants list and prepare for writing
with open('./out.csv', 'r+', newline='') as f:
    this_data = list(csv.reader(f))
    this_writer = csv.writer(f)
    
    # Iterate over the evaluation data
    for i in csv_data:
        team_name = i[1]
        team_psid = i[2]
        team_feedback = i[5]
        
        # Iterate over participants list to find the matching record
        for j in range(len(this_data)):
            # Assuming team_name is at index 0 and team_psid is at index 3 in participants list
            if this_data[j][0] == team_name and this_data[j][3] == team_psid:
                # Append the feedback to the matched record
                this_data[j].append(team_feedback)
                # break
    
    # Move the file pointer to the beginning of the file and truncate it
    f.seek(0)
    f.truncate()
    
    # Write the updated data back to the file
    this_writer.writerows(this_data)
