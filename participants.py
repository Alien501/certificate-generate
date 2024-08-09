import csv


#['7/25/2024 0:32:29', '220401026@rajalakshmi.edu.in', 'NURTURENET', 'ASHWARIYA M', '220401026@rajalakshmi.edu.in', '8190952138', 'Female', 'Biotechnology', 'DESIGNING AND DEVELOPMENT', 'AGILA SHREE A', '220701015@rajalakshmi.edu.in', '8056332992', 'Female', 'Computer Science and Engineering', 'WEB DEVELOPMENT', 'PRENESHIYA V', '220801153@rajalakshmi.edu.in', '9342737026', 'Female', 'Electronics and Communication Engineering', 'IDEA GUIDANCE', 'SURUTHI M D', '220801215@rajalakshmi.edu.in', '9025696183', 'Female', 'Electronics and Communication Engineering', 'CODER', 'ARUN PRAVIN ', '220401026@rajalakshmi.edu.in', '6381450103', 'Male', 'Biotechnology', 'AI SPECIALIST', 'HG0213', 'Telehealth Platform for Maternal and Child Health in Rural Areas\n', 'https://drive.google.com/open?id=1RrtgJPLfELc_UkuaFev6r0n1_AL5tAQw', 'https://drive.google.com/open?id=1Dr-Bx29ICdG0hi1xQKztfjYAYhrmSLMa', 'NO', 'I agree', '', '', '', 'Health and Well-being']


'''
2 - teamName
3 - leadername
4 - leaderemail
9 - memberOneName
10 - memberOneEmail
15 - memberTwoName
16 - memberTwoEmail
21 - memberThreeName
22 - memberThreeEmail
27 - psid
'''
res = ['7/25/2024 0:32:29', '220401026@rajalakshmi.edu.in', 'NURTURENET', 'ASHWARIYA M', '220401026@rajalakshmi.edu.in', '8190952138', 'Female', 'Biotechnology', 'DESIGNING AND DEVELOPMENT', 'AGILA SHREE A', '220701015@rajalakshmi.edu.in', '8056332992', 'Female', 'Computer Science and Engineering', 'WEB DEVELOPMENT', 'PRENESHIYA V', '220801153@rajalakshmi.edu.in', '9342737026', 'Female', 'Electronics and Communication Engineering', 'IDEA GUIDANCE', 'SURUTHI M D', '220801215@rajalakshmi.edu.in', '9025696183', 'Female', 'Electronics and Communication Engineering', 'CODER', 'ARUN PRAVIN ', '220401026@rajalakshmi.edu.in', '6381450103', 'Male', 'Biotechnology', 'AI SPECIALIST', 'HG0213', 'Telehealth Platform for Maternal and Child Health in Rural Areas\n', 'https://drive.google.com/open?id=1RrtgJPLfELc_UkuaFev6r0n1_AL5tAQw', 'https://drive.google.com/open?id=1Dr-Bx29ICdG0hi1xQKztfjYAYhrmSLMa', 'NO', 'I agree', '', '', '', 'Health and Well-being']


'''
8/3/2024 17:47:43,231401004@rajalakshmi.edu.in,Yes,No,TEAM GHASA,HG0510,Blockchain for Secure Voting System,AKASH MK,231401004,CSBS,Male,Hosteler,GUNASEELAN S,231401031,CSBS,Male,Hosteler,HARIHARAN K,231401032,CSBS,Male,Hosteler,SIVA SABARI GANESAN A,230701321,CSE,Male,Hosteler,ANANYA SRIRAM,231401007,CSBS,Female,Day scholar
'''

'''
name
dept
rollno
'''
with open('./h.csv', 'r', encoding='utf-8') as f:
    csv_data = list(csv.reader(f, delimiter=','))[1:]
    with open('./out.csv', 'w', newline='', encoding='UTF-8') as w:
        csv_writer = csv.writer(w, delimiter=',')
        csv_writer.writerow(['Team Name', 'Name', 'Dept', 'Roll No'])
        for row in csv_data:
            teamName = row[4]
            memberOneName = row[7]
            memeberOneRollNo = row[8]
            meberOneDept = row[9]
            memberTwoName = row[12]
            memeberTwoRollNo = row[13]
            meberTwoDept = row[14]
            memberThreeName = row[17]
            memeberThreeRollNo = row[18]
            meberThreeDept = row[19]
            memberFourName = row[22]
            memeberFourRollNo = row[23]
            meberFourDept = row[24]
            memberFiveName = row[27]
            memeberFiveRollNo = row[28]
            meberFiveDept = row[29]
            csv_writer.writerow([teamName, memberOneName, meberOneDept, memeberOneRollNo])
            csv_writer.writerow([teamName, memberTwoName, meberTwoDept, memeberTwoRollNo])
            csv_writer.writerow([teamName, memberThreeName, meberThreeDept, memeberThreeRollNo])
            csv_writer.writerow([teamName, memberFourName, meberFourDept, memeberFourRollNo])
            csv_writer.writerow([teamName, memberFiveName, meberFiveDept, memeberFiveRollNo])
            # teamName = row[2]
            # problemId = row[33]
            # teamMemberOne = row[3]
            # teamMemberOneEmail = row[4].split('@')[0]
            # teamMemberOneDept = row[7]
            # teamMemberTwo = row[9]
            # teamMemberTwoEmail = row[10].split('@')[0]
            # teamMemberTwoDept = row[12]
            # teamMemberThree = row[15]
            # teamMemberThreeEmail = row[16].split('@')[0]
            # teamMemberThreeDept = row[18]
            # teamMemberFour = row[21]
            # teamMemberFourEmail = row[22].split('@')[0]
            # teamMemberFourDept = row[24]
            # teamMemberFive = row[27]
            # teamMemberFiveEmail = row[28].split('@')[0]
            # teamMemberFiveDept = row[30]
            # # csv_writer.writerow([teamName, teamMemberOne, teamMemberOneEmail, problemId])
            # # csv_writer.writerow([teamName, teamMemberTwo, teamMemberTwoEmail, problemId])
            # # csv_writer.writerow([teamName, teamMemberThree, teamMemberThreeEmail, problemId])
            # # csv_writer.writerow([teamName, teamMemberFour, teamMemberFourEmail, problemId])
            # # csv_writer.writerow([teamName, teamMemberFive, teamMemberFiveEmail, problemId])
            # # print('Team name: ' + teamName + ' PSID: ' + problemId)
            # # print('Member One: ' + teamMemberOne + ' Team Email - ' + teamMemberOneEmail)
            # # print('Member Two: ' + teamMemberTwo + ' Team Email - ' + teamMemberTwoEmail)
            # # print('Member Three: ' + teamMemberThree + ' Team Email - ' + teamMemberThreeEmail)
            # # print('Member Four: ' + teamMemberFour + ' Team Email - ' + teamMemberFourEmail)
            # # print('Member Five: ' + teamMemberFive + ' Team Email - ' + teamMemberFiveEmail)
            # # print(' - ' * 10)