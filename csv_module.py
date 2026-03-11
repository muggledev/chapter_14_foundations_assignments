

import csv

with open('Spells.csv', 'r') as potter_csv:
    header = potter_csv.readline().split(',')
    results = []

    for i, line in enumerate(potter_csv, start=1):
        if i>= 18:
            words = line.split(',')
            results.append(words[1:4])
        if i>= 49:
            break
    
    with open('Output.csv', 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        if len(header) > 3:
            writer.writerow(header[1:4])
        
        writer.writerows(results)
if len(header) > 3:
    print(f'{header[1]:<25}{header[2]:<34}{header[3]:<16}')
for row in results:
    print(f'{row[0]:<25}{row[1]:<34}{row[2]:<16}')




