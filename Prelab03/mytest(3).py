# THIS TEST DOES NOT TEST FOR ERRORS
import collectionTasks
import difflib
import os  # List of module import statements
import sys  # Each one on a line

#testSet
test_proj_ID = ['D88C2930-9DA4-431F-8CDB-99A2AA2C7A05', '35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA', '2E7649C2-574A-496A-850B-F15190031E11', '075A54E6-530B-4533-A2E4-A15226BE588C', '082D6241-40EE-432E-A635-65EA8AA374B6', '77A1A82E-749E-43BF-B3BF-3E70F087F808', '96CC6F98-B44B-4FEB-A06B-390432C1F6EA', '32B9E998-97C3-4D5A-8005-C9685A08196F', '177EBF38-1C20-497B-A2EF-EC1880FEFDF9', '66FA081D-D1AA-4306-8650-9C39429CCDAB', '0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A', 'DE06228A-0544-4543-9055-A39D19DEDFA4', '56B13184-D087-48DB-9CBA-84B40FE17CC5', '17A946D3-A1B0-4335-8808-8594D9FBD62C', 'D230BAC0-249C-410F-84E4-41F9EDBFCB20', 'D7EFB850-9A34-41B0-BD9D-FBCDF4C3C371', '08EDAB1A-743D-4B62-9446-2F1C5824A756', 'FE647EE2-2EBD-4837-83F0-256C377365FE', '83383848-1D69-40D4-A360-817FB22769ED', '3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287', '4C5B295B-58E1-4CFB-80DF-88938B9A6300', 'B9C94766-617A-4168-B2AA-44FFE8323E32', '90BE0D09-1438-414A-A38B-8309A49C02EF', '7C376AFE-6D98-4E50-B29C-71FBF6260B2D', '8E56417E-0D81-4F43-8137-F1F7AA005654', '6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9', '8C71F259-ECA8-4267-A8B3-6CAD6451D4CC', '6CCCA5F3-3008-46FF-A779-2D2F872DAF82']
std_dict = {'Adams, Keith': '02583-95216', 'Alexander, Carlos': '41724-49926', 'Allen, Amanda': '73632-00344', 'Anderson, Debra': '63017-50438', 'Bailey, Catherine': '69282-33425', 'Baker, Craig': '69069-29232', 'Barnes, Sean': '18118-03371', 'Bell, Kathryn': '93445-12424', 'Bennett, Nancy': '19372-45052', 'Brooks, Carol': '68186-76013', 'Brown, Robert': '10592-17540', 'Bryant, Evelyn': '04634-37226', 'Butler, Julia': '63581-09884', 'Campbell, Eugene': '52357-54349', 'Carter, Sarah': '07958-57397', 'Clark, Joe': '42800-15632', 'Coleman, Lori': '84756-04819', 'Collins, Anthony': '75471-28954', 'Cook, Margaret': '79398-24475', 'Cooper, Kelly': '81782-21568', 'Cox, Shirley': '52477-58076', 'Davis, Douglas': '64310-22128', 'Diaz, Tina': '44577-99899', 'Edwards, Rachel': '99701-55213', 'Evans, Johnny': '59274-55268', 'Flores, Andrea': '15821-95120', 'Foster, Benjamin': '83545-99452', 'Garcia, Martha': '04025-42834', 'Gonzales, Arthur': '65101-47245', 'Gonzalez, Kimberly': '17861-29412', 'Gray, Tammy': '26985-90240', 'Green, Roy': '65279-11004', 'Griffin, Charles': '66552-00795', 'Hall, Beverly': '30575-77344', 'Harris, Anne': '13579-76672', 'Henderson, Christopher': '81461-39190', 'Hernandez, Lawrence': '28404-21206', 'Hill, Jose': '49728-91010', 'Howard, Shawn': '98705-63702', 'Hughes, James': '03335-55237', 'Jackson, Doris': '15840-81914', 'James, Randy': '93168-04662', 'Jenkins, Paul': '39210-49975', 'Johnson, Roger': '38749-83244', 'Jones, Stephanie': '52403-12854', 'Kelly, Joyce': '43779-62206', 'King, Carolyn': '95658-86799', 'Lee, Julie': '91285-61524', 'Lewis, William': '35036-62750', 'Long, Joshua': '44845-88216', 'Lopez, Juan': '57004-54761', 'Lowe, Karen': '57925-31071', 'Martin, Richard': '70615-99374', 'Martinez, David': '66537-00315', 'Miller, Aaron': '01524-65380', 'Mitchell, Judith': '64764-90662', 'Moore, John': '00885-84102', 'Morgan, Edward': '76394-56172', 'Morris, Heather': '07922-19414', 'Murphy, Donna': '20347-83572', 'Nelson, Louise': '66285-23831', 'Parker, Raymond': '17415-55660', 'Patterson, Peter': '73162-96886', 'Perez, Kathleen': '69652-84270', 'Perry, Marie': '90411-88509', 'Peterson, Daniel': '33618-79986', 'Phillips, Brenda': '09312-94888', 'Powell, Gregory': '24293-80620', 'Price, Dorothy': '33874-61057', 'Ramirez, Linda': '69147-24600', 'Reed, Bobby': '70401-80000', 'Richardson, George': '60571-51326', 'Rivera, Patricia': '26032-51883', 'Roberts, Teresa': '68589-74799', 'Robinson, Pamela': '48757-77990', 'Rodriguez, Jeffrey': '95100-67620', 'Rogers, Elizabeth': '40230-24482', 'Ross, Frances': '30768-54860', 'Russell, Scott': '05074-62754', 'Sanchez, Deborah': '52134-15115', 'Sanders, Emily': '84209-46116', 'Scott, Michael': '87049-31809', 'Simmons, Cynthia': '80997-59183', 'Smith, Jimmy': '98514-63691', 'Stewart, Earl': '78241-98048', 'Taylor, Brian': '49650-25644', 'Thomas, Mark': '05481-39385', 'Thompson, Michelle': '52930-30854', 'Torres, Betty': '44471-18426', 'Turner, Theresa': '17047-26190', 'Walker, Terry': '55926-36619', 'Ward, Sandra': '53307-18031', 'Washington, Annie': '06139-33248', 'Watson, Martin': '32489-57596', 'White, Diana': '23694-74441', 'Williams, Mary': '04976-05559', 'Wilson, Howard': '28739-05933', 'Wood, Kevin': '82124-28153', 'Wright, Eric': '58048-94342', 'Young, Frank': '44921-58069'}
std_names = ['Adams, Keith', 'Alexander, Carlos', 'Allen, Amanda', 'Anderson, Debra', 'Bailey, Catherine', 'Baker, Craig', 'Barnes, Sean', 'Bell, Kathryn', 'Bennett, Nancy', 'Brooks, Carol', 'Brown, Robert', 'Bryant, Evelyn', 'Butler, Julia', 'Campbell, Eugene', 'Carter, Sarah', 'Clark, Joe', 'Coleman, Lori', 'Collins, Anthony', 'Cook, Margaret', 'Cooper, Kelly', 'Cox, Shirley', 'Davis, Douglas', 'Diaz, Tina', 'Edwards, Rachel', 'Evans, Johnny', 'Flores, Andrea', 'Foster, Benjamin', 'Garcia, Martha', 'Gonzales, Arthur', 'Gonzalez, Kimberly', 'Gray, Tammy', 'Green, Roy', 'Griffin, Charles', 'Hall, Beverly', 'Harris, Anne', 'Henderson, Christopher', 'Hernandez, Lawrence', 'Hill, Jose', 'Howard, Shawn', 'Hughes, James', 'Jackson, Doris', 'James, Randy', 'Jenkins, Paul', 'Johnson, Roger', 'Jones, Stephanie', 'Kelly, Joyce', 'King, Carolyn', 'Lee, Julie', 'Lewis, William', 'Long, Joshua', 'Lopez, Juan', 'Lowe, Karen', 'Martin, Richard', 'Martinez, David', 'Miller, Aaron', 'Mitchell, Judith', 'Moore, John', 'Morgan, Edward', 'Morris, Heather', 'Murphy, Donna', 'Nelson, Louise', 'Parker, Raymond', 'Patterson, Peter', 'Perez, Kathleen', 'Perry, Marie', 'Peterson, Daniel', 'Phillips, Brenda', 'Powell, Gregory', 'Price, Dorothy', 'Ramirez, Linda', 'Reed, Bobby', 'Richardson, George', 'Rivera, Patricia', 'Roberts, Teresa', 'Robinson, Pamela', 'Rodriguez, Jeffrey', 'Rogers, Elizabeth', 'Ross, Frances', 'Russell, Scott', 'Sanchez, Deborah', 'Sanders, Emily', 'Scott, Michael', 'Simmons, Cynthia', 'Smith, Jimmy', 'Stewart, Earl', 'Taylor, Brian', 'Thomas, Mark', 'Thompson, Michelle', 'Torres, Betty', 'Turner, Theresa', 'Walker, Terry', 'Ward, Sandra', 'Washington, Annie', 'Watson, Martin', 'White, Diana', 'Williams, Mary', 'Wilson, Howard', 'Wood, Kevin', 'Wright, Eric', 'Young, Frank']
std_ids = ['02583-95216', '41724-49926', '73632-00344', '63017-50438', '69282-33425', '69069-29232', '18118-03371', '93445-12424', '19372-45052', '68186-76013', '10592-17540', '04634-37226', '63581-09884', '52357-54349', '07958-57397', '42800-15632', '84756-04819', '75471-28954', '79398-24475', '81782-21568', '52477-58076', '64310-22128', '44577-99899', '99701-55213', '59274-55268', '15821-95120', '83545-99452', '04025-42834', '65101-47245', '17861-29412', '26985-90240', '65279-11004', '66552-00795', '30575-77344', '13579-76672', '81461-39190', '28404-21206', '49728-91010', '98705-63702', '03335-55237', '15840-81914', '93168-04662', '39210-49975', '38749-83244', '52403-12854', '43779-62206', '95658-86799', '91285-61524', '35036-62750', '44845-88216', '57004-54761', '57925-31071', '70615-99374', '66537-00315', '01524-65380', '64764-90662', '00885-84102', '76394-56172', '07922-19414', '20347-83572', '66285-23831', '17415-55660', '73162-96886', '69652-84270', '90411-88509', '33618-79986', '09312-94888', '24293-80620', '33874-61057', '69147-24600', '70401-80000', '60571-51326', '26032-51883', '68589-74799', '48757-77990', '95100-67620', '40230-24482', '30768-54860', '05074-62754', '52134-15115', '84209-46116', '87049-31809', '80997-59183', '98514-63691', '78241-98048', '49650-25644', '05481-39385', '52930-30854', '44471-18426', '17047-26190', '55926-36619', '53307-18031', '06139-33248', '32489-57596', '23694-74441', '04976-05559', '28739-05933', '82124-28153', '58048-94342', '44921-58069']


with open("myResult_kai.txt", 'w') as f:
    f.write("\n\nTHIS TEST DOES NOT TEST FOR ERRORS\n\n")
# Part 1
    f.write("------------------Part 1----------------------------------------------------------\n")
    for proj in test_proj_ID:
        f.write("Project ID: {} ==> Counts:\n".format(proj))
        f.write('\t R: ' + str(collectionTasks.getComponentCountByProject(proj, 'R')) + '\n')
        f.write('\t I: ' + str(collectionTasks.getComponentCountByProject(proj, 'I')) + '\n')
        f.write('\t C: ' + str(collectionTasks.getComponentCountByProject(proj, 'C')) + '\n')
        f.write('\t T: ' + str(collectionTasks.getComponentCountByProject(proj, 'T')) + '\n\n')
    f.write('---------------------------Part 1--ENDS--------------------------------------------\n')

# Part2
    f.write("------------------Part 2----------------------------------------------------------\n")
    for name, id in std_dict.items():
        f.write("Name: {} ==> Counts:\n".format(name))
        f.write('\t R: ' + str(collectionTasks.getComponentCountByStudent(name, 'R')) + '\n')
        f.write('\t I: ' + str(collectionTasks.getComponentCountByStudent(name, 'I')) + '\n')
        f.write('\t C: ' + str(collectionTasks.getComponentCountByStudent(name, 'C')) + '\n')
        f.write('\t T: ' + str(collectionTasks.getComponentCountByStudent(name, 'T')) + '\n\n')
    f.write('---------------------------Part 2--ENDS--------------------------------------------\n')

# Part3
    f.write("------------------Part 3----------------------------------------------------------\n")
    for name in std_names[0:12]:
        f.write("{} :\n".format(name))
        temp_list = collectionTasks.getParticipationByStudent(name)
        assert (type(temp_list) == set)
        temp_list = list(temp_list)
        temp_list = sorted(temp_list)
        for item in temp_list:
            f.write('\t' + item + '\n')
        f.write('\n')
    f.write('---------------------------Part 3--ENDS--------------------------------------------\n')

# Part4
    f.write("------------------Part 4----------------------------------------------------------\n")
    for proj in test_proj_ID:
        f.write("{} :\n".format(proj))
        temp_list = collectionTasks.getParticipationByProject(proj)
        assert (type(temp_list) == set)
        temp_list = list(temp_list)
        temp_list = sorted(temp_list)
        for item in temp_list:
            f.write('\t' + item + '\n')
        f.write('\n')
    f.write('---------------------------Part 4--ENDS--------------------------------------------\n')

# Part5
    f.write("------------------Part 5----------------------------------------------------------\n")
    r_dict = collectionTasks.getCostOfProjects()
    assert (type(r_dict) == dict)
    for elem in sorted(r_dict.items()):
        f.write("Project: " + elem[0] + 'cost : ' + str(elem[1]) + '\n')
    f.write('---------------------------Part 5--ENDS--------------------------------------------\n')

# Part6
    f.write("------------------Part 6----------------------------------------------------------\n")
    some_com_ids = {'RTD-159', 'NVC-327', 'MGC-590', 'OLW-497', 'LKZ-532', 'SLT-436', 'TMS-946'}
    f.write('For coms : {}\n'.format(sorted(list(some_com_ids))))
    r = collectionTasks.getProjectByComponent(some_com_ids)
    assert (type(r) == set)
    r = sorted(list(r))
    f.write("\n".join(r) + '\n')
    f.write('---------------------------Part 6--ENDS--------------------------------------------\n')

# Part7
    f.write("------------------Part 7----------------------------------------------------------\n")
    test_index = [(0,2), (7,10), (4,12), (26,3)]
    for index1, index2 in test_index:
        f.write("Common of {} and {}:\n".format(test_proj_ID[index1], test_proj_ID[index2]))
        r = collectionTasks.getCommonByProject(test_proj_ID[index1], test_proj_ID[index2])
        for e in r:
            f.write("\t{}\n".format(e))
    f.write('---------------------------Part 7--ENDS--------------------------------------------\n')

# Part8
    f.write("------------------Part 8----------------------------------------------------------\n")
    some_com_ids = {'RTD-159', 'MGC-590', 'OLW-497', 'SLT-436', 'TMS-946'}
    f.write('For coms : {}\n'.format(some_com_ids))
    r = collectionTasks.getComponentReport(some_com_ids)
    assert (type(r) == dict)
    for elem in sorted(r.items()):
        f.write("\t" + elem[0] + 'was used : ' + str(elem[1]) + ' times\n')
    f.write('---------------------------Part 8--ENDS--------------------------------------------\n')

# Part9
    f.write("------------------Part 9----------------------------------------------------------\n")
    some_std = std_names[23:43]
    f.write('-----std-----\n'+ "\n".join(some_std) + '\n----Circuits----\n')
    r = collectionTasks.getCircuitByStudent(set(some_std))
    r = sorted(list(r))
    for e in r:
        f.write("\t{}\n".format(e))
    f.write('---------------------------Part 9--ENDS--------------------------------------------\n')

# Part10
    f.write("------------------Part 10----------------------------------------------------------\n")
    some_com_ids = {'RTD-159', 'NVC-327', 'MGC-590', 'OLW-497', 'LKZ-532', 'SLT-436', 'TMS-946'}
    f.write('-----COM_ID-----\n'+ "\n".join(sorted(list(some_com_ids))) + '\n----Circuits----\n')
    r = collectionTasks.getCircuitByComponent(set(some_com_ids))
    r = sorted(list(r))
    for e in r:
        f.write("\t{}\n".format(e))
    f.write('---------------------------Part 10--ENDS--------------------------------------------\n')

    a = open('myResult.txt', 'r')
    b = open('myResult_kai.txt', 'r')
    diff = difflib.ndiff(a.readlines(), b.readlines())
    print(''.join(diff))