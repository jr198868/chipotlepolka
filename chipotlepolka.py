import csv
import json
import pandas as pd

'''
Help on module chipotlepolka:

NAME
    chipotlepolka

CLASSES
    builtins.object
        cleandata
        datatransfer
        parse_data
        savedata
    
    class cleandata(builtins.object)
     |  Methods defined here:
     |  
     |  keep_decimal(num, k)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class datatransfer(builtins.object)
     |  Methods defined here:
     |  
     |  csv_to_excel(csv_file, excelfile_path)
     |  
     |  csv_to_json(csv_file, jsonfile_path)
     |  
     |  xls_to_csv(excel_file, csvfile_path)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class parse_data(builtins.object)
     |  Methods defined here:
     |  
     |  read_csv(csv_file)
     |  
     |  read_fasta(input_fasta)
     |  
     |  read_json(json_file)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class savedata(builtins.object)
     |  Methods defined here:
     |  
     |  savetojson(path, target_dict)
     |  
     |  savetolist(path, target_list)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
'''


##########################################################################
#                                                                        #
#                         Transferring data                              #
#                                                                        #
##########################################################################


class transferdata:

    def xls_to_csv(excel_file, csvfile_path):
        # read an excel file and convert 
        # into a dataframe object
        df = pd.read_excel(excel_file, engine = 'openpyxl')
        df.to_csv(csvfile_path)
        # show the dataframe

    def csv_to_excel(csv_file, excelfile_path):
        read_file = pd.read_csv (csv_file)
        read_file.to_excel (excelfile_path, index = None, header=True)


    def csv_to_json(csv_file, jsonfile_path):

        df = pd.read_csv (csv_file)
        df.to_json (jsonfile_path)


##########################################################################
#                                                                        #
#                           Parsing data                                 #
#                                                                        #
##########################################################################


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


##########################################################################
#                                                                        #
#                           Saving data                                  #
#                                                                        #
##########################################################################


class savedata:

    #save list to csv
    def savetolist(path, target_list):
        with open (path, 'w') as f:
            wr = csv.writer(f)
            wr.writerows(target_list)

    #save dictionary to json
    def savetojson(path, target_dict):
        with open(path, "w") as outfile:
            json.dump(target_dict, outfile)


##########################################################################
#                                                                        #
#                           Cleaning data                                #
#                                                                        #
##########################################################################

class cleandata:

    def keep_decimal(num, k):
        result = None
        if k == 1:
            result = '{:.1f}'.format(float(num))
        if k == 2:
            result = '{:.2f}'.format(float(num))
        if k == 3:
            result = '{:.3f}'.format(float(num))

        return result