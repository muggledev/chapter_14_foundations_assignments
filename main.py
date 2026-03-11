
# *************NOTES********************************


# with open('testing_csv_file.csv', 'r') as test_csv:
#     results = []
#     for line in test_csv:
#         words = line.split(',')
#         results.append((words[0], words[1:]))
#     print(results)



# *************ASSIGNMENT*****************************
# Number 1
# with open('countydata.csv', 'r', encoding="utf-8-sig") as county_csv:

#     results = []
#     for line in county_csv:
#         print(line)

# Number 2
# with open('countydata.csv', 'r', encoding="utf-8-sig") as county_csv:

#     results = []
#     for line in county_csv:
#         words = line.split(',')
#         results.append([words[0], words[1], words[10]])
#     for county in results:
#         print(f'{county[0]:20}{county[1]:>10}{county[2]:>12}')


# Number 3

# with open('countydata.csv', 'r', encoding="utf-8-sig") as county_csv:

#     results = []
#     for line in county_csv:
#         words = line.split(',')
#         results.append([words[0], words[1], words[10].strip()])
#     for county in results:
#         growth = int(county[2]) - int(county[1]) 
#         print(f'{county[0]:20}{county[1]:>10}{county[2]:>12}{growth:>12}')

# Number 4

with open('countydata.csv', 'r', encoding="utf-8-sig") as county_csv:
    header = county_csv.readline().split(',')
    results = []
    for line in county_csv:
        words = line.split(',')
        results.append([words[0], words[1], words[10].strip()])
    print(f'{header[0]:20} {header[1]:>11} {header[10].strip():>11} {'Growth':>11} {'Rate%':>12}')
    for county in results:
        growth = int(county[2]) - int(county[1]) 
        rate = (growth/int(county[1])) * 100
        print(f'{county[0]:20}{county[1]:>12}{county[2]:>12}{growth:>12}{rate:>12.2f}%')




# ******************14.2*******************************************
# NOTES************
# import csv

# rows = [
#     ['Jim','Halpert','Sales Rep','10/20/1979'],
#     ['Michael', 'Scott', 'Regional Manager', '08/16/1962'],
#     ['Pam','Beesly', 'Receptionist', '03/07/1974'],
#     ['Dwight','Schrute', 'Assistant to the Regional Manager', '01/20/1966']
# ]

# with open('csv_file_2.csv', 'w') as outfile:
#     wrt = csv.writer(outfile)

#     wrt.writerows(rows)


# import csv

# fields = ['Player', 'Position', 'Age', 'School']
# rows = [
#     ['Donovan Mitchell','SG','25','Louisville'],
#     ['Mike Conley', 'PG', '33', 'Ohio State'],
#     ['Rudy Gobert','C', '29', '--'],
#     ['Joe Ingles','SG', '33', '--']
# ]

# with open('players.csv', 'w') as outfile:
#     wrt = csv.writer(outfile)

#     wrt.writerow(fields)

#     wrt.writerows(rows)



# EXERCISE 1********************

# import csv

# header_fields = ['State', 'Capital', 'Year Founded']

# data = [
#   ['Oregon','Salem',1855],
#   ['Utah','Salt Lake City',1858],
#   ['Oklahoma', 'Oklahoma City', 1910],
#   ['Nebraska', 'Lincoln', 1867],
#   ['Florida', 'Tallahassee', 1824]
# ]

# with open('states.csv', 'w') as outfile:
#     wrt = csv.writer(outfile)

#     wrt.writerow(header_fields)
#     wrt.writerows(data)


# EXERCISE 2************************
# Write a program that takes a list of dictionaries, like the one below and writes the keys as the header row, then writes the data as rows in the database. Your output file should look the same as the output file in Exercise #1.
# NOTES: Pay attention to how the data is formatted and let that guide how you parse it and write it to the file.

import csv

states = [
  { 'State': 'Oregon', 'Capital': 'Salem', 'Year Founded': 1855 },
  { 'State': 'Utah', 'Capital': 'Salt Lake City', 'Year Founded': 1858 },
  { 'State': 'Oklahoma', 'Capital': 'Oklahoma City', 'Year Founded': 1910 },
  { 'State': 'Nebraska', 'Capital': 'Lincoln', 'Year Founded': 1867 },
  { 'State': 'Florida', 'Capital': 'Tallahassee', 'Year Founded': 1824 },
]

with open('states_2.csv', 'w') as outfile:
    wrt = csv.writer(outfile)

    header = states[0].keys()
    states_data = states[1].values()
    wrt.writerow(header)
    wrt.writerows(states)












        