import csv

#parse csv file
save_list = []

class parse_csv:
    
    def read_csv(csv_file):
        with open (csv_file) as f:
            for line in f:
                save_list.append(line.strip().split(','))

        save_list[0] = [save_list[0][0].split('\ufeff')[1]] + save_list[0][1:]

        print('rows:'+ str(len(save_list)) + ',' + 'columns:' + str(len(save_list[0])))
        return save_list





class savedata:

    #save list to csv
    def savetolist(path, target_list):
        with open (path, 'w') as f:
            wr = csv.writer(f)
            wr.writerows(target_list)
