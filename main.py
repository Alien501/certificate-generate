import csv, json

# ['1', 'Winged Wizards', 'HG0302', 'Culture, Education and Tourism', 'HG0302-WingedWizards-PPT - SIVAMAHALAKSHMI S 230101053.pptx', '', '', '3', '1', '2', '1', '2', '1', '10', 'Shakithyan', 'Rejected', 'The Content is AI generated. The Given Solution for the Problem seems to impartical.Flowchart is not defined properly with any visual representation .The Overal Presenation should be improved.'

'''
0 - teamNo
1 - teamName
2 - PSID
13 - Total
14 - Evaluator Name
15 - Status
16 - Feedback
'''

with open('./Evaluvation List.csv') as f:
    csv_reader = list(csv.reader(f, delimiter=','))[2:]
    ans = []
    for row in range(0, (len(csv_reader)), 3):
        try:
            teamNo = csv_reader[row][0]
            teamName = csv_reader[row][1]
            teamPsid = csv_reader[row][2]
            try:
                teamTotal = (float(csv_reader[row][13]) + float(csv_reader[row + 1][13]) + float(csv_reader[row + 2][13]))/3
            except:
                teamTotal = 0
            teamStatus = [csv_reader[row][15], csv_reader[row + 1][15], csv_reader[row + 2][15]]
            feedbacks = [csv_reader[row][16], csv_reader[row + 1][16], csv_reader[row + 2][16]]
            my_dict = {
                'teamNo': teamNo,
                'teamName': teamName,
                'teamPsid': teamPsid,
                'teamStatus': teamStatus,
                'teamTotal': int(teamTotal),
                'teamFeedback': '\n'.join(feedbacks) 
            }
            ans.append(my_dict)
        except Exception as e:
            print('Error - ' + e)
    # As json
    # with open('./res.json', 'w') as res:
    #     json.dump(ans, res)
    # As csv
    with open('./res1.csv', 'w', newline='') as res:
        csv_writer = csv.writer(res)
        for i in ans:
            csv_writer.writerow((i['teamNo'], i['teamName'], i['teamPsid'], i['teamStatus'], i['teamTotal'], i['teamFeedback']))