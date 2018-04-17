import csv
from geotext import GeoText

with open('abcnews-date-text.csv', encoding='utf-8') as csvFile:
    reader = csv.reader(csvFile)
    try:
        newList = []
        for i, rows in enumerate(reader):
            if 0 < i <= 20:
                row = rows[1].capitalize()

                eachWord = row.split(' ')
                out = []
                for part in eachWord:
                    abc = part.capitalize()
                    place = GeoText(abc).cities
                    if abc in place:
                        out.append(abc)
                    else:
                        out.append(part)
                line = " ".join(out)
                newList.append(line)
        csvFile.close()
        print(newList)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format('abcnews-date-text.csv', reader.line_num, e))

with open('example.csv', 'w', newline='') as new:
    writer = csv.writer(new, delimiter=" ")
    for newRow in newList:
        writer.writerow(newRow.split(' '))
    new.close()