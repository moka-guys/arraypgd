'''
this script filters out the unwanted chromosome and control data from an FE file

fefilter.py
    arguments
        filename (excluding the .txt)
        first chromosome of interest (e.g. 12)
        second chromosome of interest (e.g. 8)
        third chromosome of interest (e.g. 20)
        fourth chromosome of interest (e.g. X)
'''

with open('/home/wook/Documents/apgdfilter/' + sys.argv[1] + '.txt', encoding='utf-8') as fefile:
    import csv
    readfeline = csv.reader(fefile, delimiter = '\t')
    line = 0
    for row in readfeline:
        #create the output (will overwrite if this exists already) and write the first row to it
        if line < 1:
            print(row)
            with open('/home/wook/Documents/apgdfilter/' + sys.argv[1] + '_filtered.txt', mode='w', encoding='utf-8') as filteredfile:
                filteredfilewriter = csv.writer(filteredfile, delimiter='\t')
                filteredfilewriter.writerow(row)
        #append the rest of the header lines to the output
        if line > 0 and line < 10:
            print(row)
            with open('/home/wook/Documents/apgdfilter/' + sys.argv[1] + '_filtered.txt', mode='a', encoding='utf-8') as filteredfile:
                filteredfilewriter = csv.writer(filteredfile, delimiter='\t')
                filteredfilewriter.writerow(row)                
        #append the desired chromosome rows to the output
        if line > 10 and line < 200:
            import re
            #if row[7] == [chr]:
            match1 = re.search('chr' + sys.argv[2], row[7])
            match2 = re.search('chr' + sys.argv[3], row[7])
            match3 = re.search('chr' + sys.argv[4], row[7])
            match4 = re.search('chr' + sys.argv[5], row[7])
            if match1 or match2 or match3 or match4:
                print(row[7])
                with open('/home/wook/Documents/apgdfilter/' + sys.argv[1] + '_filtered.txt', mode='a', encoding='utf-8') as filteredfile:
                    filteredfilewriter = csv.writer(filteredfile, delimiter='\t')
                    filteredfilewriter.writerow(row)                
        #iterate through the loop
        line += 1
