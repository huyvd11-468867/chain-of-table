import json
import pandas as pd
import os, glob
from utils import *

dir_path = './WikiTableQuestions/data'
tsv_files = glob.glob(os.path.join(dir_path, '*'))

# define question types by pair of q and a
q_type = {
    'min': {'question':[],
            'answer':[],
            'file_name':[]
            },

    'max':{'question':[],
            'answer':[],
            'file_name':[]
            },

    'howmany':{'question':[],
            'answer':[],
            'file_name':[]
            }
    }

# define synonym from question statistical type
snn_min = ['lowest', 'smallest', 'least', 'minimal', 'tiniest', 
           'bottom', 'modicum', 'least possible', 'scant', 'narrowest']
snn_max = ['highest', 'greatest', 'largest', 'utmost', 'peak', 
           'maximum possible', 'upper limit', 'topmost', 'supreme', 'optimum']
snn_howmany = ['how many']

# append tsv: q and a 
for file in [f for f in tsv_files if f.endswith('tsv')]:
    print(f'file: {file}')
    rows = read_tsv(file)

    # get all questions and answer in tsv
    ques_list, ans_list, file_list = return_qanda_of_tsv(file)
    
    for question, answer, file_name in zip(ques_list, ans_list, file_list):
        # get pair of q and a if available
        for word in snn_howmany:
            if word in question.lower():
                q_type['howmany']['question'].append(question)
                q_type['howmany']['answer'].append(answer)
                q_type['howmany']['file_name'].append(file_name)
                break

        for word in snn_min:
            if word in question.lower():
                q_type['min']['question'].append(question)
                q_type['min']['answer'].append(answer)
                q_type['min']['file_name'].append(file_name)
                break
            
        for word in snn_max:
            if word in question.lower():
                q_type['max']['question'].append(question)
                q_type['max']['answer'].append(answer)
                q_type['max']['file_name'].append(file_name)
                break
        
# Specify the file to save the JSON file
file_name = "statistical.json"

# Combine folder path and file name
file_path = os.path.join('./huy/data', file_name)

# Save the dictionary to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(q_type, json_file)
    print(f"The dictionary has been saved to {file_path}")