with open('/home/wook/Documents/apgdfilter/252846911385_S01_Guys121919_CGH_1100_Jul11_2_1_1.txt', encoding='utf-8') as fefile:
    import csv
    readfeline = csv.reader(fefile, delimiter = '\t')
    line = 0
    for row in readfeline:
        #create the output (will overwrite if this exists already) and write the first row to it
        if line < 1:
            print(row)
            with open('/home/wook/Documents/apgdfilter/filtered.txt', mode='w', encoding='utf-8') as filteredfile:
                filteredfilewriter = csv.writer(filteredfile, delimiter='\t')
                filteredfilewriter.writerow(row)
        #append the rest of the header lines to the output
        if line > 0 and line < 10:
            print(row)
            with open('/home/wook/Documents/apgdfilter/filtered.txt', mode='a', encoding='utf-8') as filteredfile:
                filteredfilewriter = csv.writer(filteredfile, delimiter='\t')
                filteredfilewriter.writerow(row)                
        #append the desired chromosome rows to the output
        if line > 10 and line < 200:
            import re
            #if row[7] == [chr]:
            match1 = re.search('chr2', row[7])
            match2 = re.search('chr10', row[7])
            if match1 or match2:
                print(row[7])
                with open('/home/wook/Documents/apgdfilter/filtered.txt', mode='a', encoding='utf-8') as filteredfile:
                    filteredfilewriter = csv.writer(filteredfile, delimiter='\t')
                    filteredfilewriter.writerow(row)                
        #iterate through the loop
        line += 1
