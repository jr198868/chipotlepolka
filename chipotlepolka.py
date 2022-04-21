import csv
import json
import pandas as pd


class parse_data:

    #parse csv file
    def read_csv(csv_file):
        save_list = []
        with open (csv_file) as f:
            for line in f:
                save_list.append(line.strip().split(','))

        if save_list[0][0].startswith('\ufeff'):
            save_list[0] = [save_list[0][0].split('\ufeff')[1]] + save_list[0][1:]

        #print('rows:'+ str(len(save_list)) + ',' + 'columns:' + str(len(save_list[0])))
        return save_list

    def read_json(json_file):
        # Opening JSON file
        f = open(json_file)
 
        # returns JSON object as a dictionary
        data = json.load(f)     
        return data        

    
    def read_fasta(input_fasta):
        fas = {}
        with open(input_fasta) as fasta:
            id = ""
            data = []
            chrm = ""
            for each in fasta:
                if each.startswith(">"):
                    if chrm == "":
                        chrm = each[1:].strip()
                        continue
                    seq = "".join(data)
                    data = []
                    fas[chrm] = seq

                    chrm = each[1:].strip()
                else:
                    data.append(each.strip())
        
            fas[chrm] = "".join(data)
        return fas 

    def lambda_sort(arr, sortkey):
        arr = sorted(arr, key=lambda x:sortkey)
        return arr



class datatransfer:

    def xls_to_csv(excel_file, path):
        # read an excel file and convert 
        # into a dataframe object
        df = pd.read_excel(excel_file, engine = 'openpyxl')
        df.to_csv(path)
        # show the dataframe

    def csv_to_excel(csv_file, path):
        read_file = pd.read_csv (csv_file)
        read_file.to_excel (path, index = None, header=True)



class savedata:

    #save list to csv
    def savetolist(path, target_list):
        with open (path, 'w') as f:
            wr = csv.writer(f)
            wr.writerows(target_list)

    def savetojson(path, target_dict):
        with open(path, "w") as outfile:
            json.dump(target_dict, outfile)