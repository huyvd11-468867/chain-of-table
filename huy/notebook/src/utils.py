import pandas as pd
import openai
import tiktoken


def read_tsv(path):
    ans = []
    # interviews_df = pd.read_csv(path, sep='\t')
    # return interviews_df
    with open(path) as file:
        for line in file:
            l=line.split('\t')
            # append list to ans
            ans.append(l)
        
    return ans

def return_qanda_of_tsv(path):
    ques = []
    ans = []
    file_name = []
    # interviews_df = pd.read_csv(path, sep='\t')
    # return interviews_df
    with open(path) as file:
        for line in file:
            l=line.split('\t')
            # append list to ques
            ques.append(l[1])
            ans.append(l[3].replace('\n', ''))
            file_name.append(l[2])
            
    return ques, ans, file_name

def count_prompt_tokens(query):
    encoding = tiktoken.encoding_for_model('gpt-4')
    print(f"Tokens: {len(encoding.encode(query))}")

    return len(encoding.encode(query))
