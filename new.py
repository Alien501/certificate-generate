import csv

fileToRead = './Final - Out.csv'
fileToWrite = './Final.csv'

with open(fileToRead) as f:
    data = list(csv.reader(f))[1:]

selected = {
    "tech fury": ["HG0120", "HG0106"],
    "hacktivate": ["HG0315", "HG0405"],
    "tekdecks": ["HG0211", "HG0414", "HG0202", "HG0418"],
    "team 404": ["HG0408", "HG0205"],
    "stackoverflowers": ["HG0519"],
    "nexgen": ["HG0613"],
    "pix'els": ["HG0117", "HG0101"],
    "five developers": ["HG0103", "HG0107", "HG0101"],
    "sentinal": ["HGO215"],
    "tech buddy": ["HG0405"],
    "techgigs": ["HG0105"],
    "tech titans": ["HG0612", "HG0314", "HG0103"],
    "dynamite": ["HG0211"],
    "hackernauts": ["HG0311"],
    "inaccessible": ["HG0516"],
    "technoblade": ["HG0111"],
    "hack puyals": ["HG0109"],
    "techmakers-2": ["HG0102"],
    "team z": ["HG0213"],
    "detectify": ["HG0507"],
    "404 not found": ["HG0215"],
    "illuminators": ["HG0207", "HG0405"],
    "travel titans": ["HG0314"],
    "beginners": ["HG0501"],
    "team asparagus": ["HG0506"],
    "codehub": ["HG0513", "HG0514"],
    "team ghasa": ["HG0510"],
    "ace - squad": ["HG0106"],
    "pentagon": ["HG0206"],
    "sentinels": ["HG0101"],
    "build wheels": ["HG0107"],
    "bits n bytes": ["HG0108"],
    "maincharacters": ["HG0110"],
    "neophyte nest": ["HG0207"],
    "codedna": ["HG0220"]
}

selected_list = [
    "tech fury",
    "hacktivate",
    "tekdecks",
    "team 404",
    "stackoverflowers",
    "nexgen",
    "pix'els",
    "five developers",
    "sentinal",
    "tech buddy",
    "techgigs",
    "tech titans",
    "dynamite",
    "hackernauts",
    "inaccessible",
    "technoblade",
    "hack puyals",
    "techmakers-2",
    "team z",
    "detectify",
    "404 not found",
    "illuminators",
    "travel titans",
    "beginners",
    "team asparagus",
    "codehub",
    "team ghasa",
    "ace - squad",
    "pentagon",
    "sentinels",
    "build wheels",
    "bits n bytes",
    "maincharacters",
    "neophyte nest",
    "codedna"
]



with open(fileToWrite, 'w', newline='') as f1:
    csv_writer = csv.writer(f1)
    csv_writer.writerow(['Team Name', 'Team Leader', 'Email', 'PSID', 'Feedback', 'Status'])
    count = 0
    for i in range(0, len(data)):
        if data[i][0].lower() in selected_list and data[i][3] in selected[data[i][0].lower()] :
            count += 1
            data[i].append('Selected')
            csv_writer.writerow(data[i])
        else:
            data[i].append('Rejected')
            csv_writer.writerow(data[i])
    print(count)