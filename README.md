# chipotlepolka

chipotlepolka is a python library aiming to help data scientist to clean and analyze their data  


## Project Structure 🚀

```sh
chipotlepolka/
├── README.md
├── __init__.py
├── __pycache__
│   └── chipotlepolka.cpython-38.pyc
├── chipotlepolka.py
├── project_structure.txt
├── setup.py
├── test.ipynb
└── test_result
    ├── test.csv
    ├── test.faa
    ├── test.json
    └── test.xls

2 directories, 11 files
```

## Class Structure 🚀

```sh
chipotlepolka.py

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

```

## How to use chipotlepolka 🚀

```sh
$ git clone https://github.com/jr198868/chipotlepolka.git 

$ cd chipotlepolka/

$ python3 setup.py install

$ or simply copy chipotlepolka.py to your current working directory
```

## Check if the package successfully installed 🚀
pip list

