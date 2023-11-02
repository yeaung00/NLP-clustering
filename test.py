import csv
import os
import openai
from dotenv import load_dotenv
import re

# { 'id': str, 'questions': List }

# { 
#   cluster_id: 37,
#   cluster_title: 'software engineer career'
# }
def generate_prompt(clusters: list):
    # print("cluster is: ", cluster)
    prompt = "Given the following list, what is an appropriate title that correctly categorizes the set of questions for the given id? Make the cluster title specific to the context of the questions." + str(clusters)
        
    schema = {
        'type': "object",
        'properties': { 
            'cluster_id': {
                'type': "string"
            },
            'generated_title': {
                'type': "string",
                'description': "A title for the cluster id"
            }
        }
    }
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful assistant'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        max_tokens=5,
        functions=[{ 
            'name': "get_cluster_titles",
            'parameters': schema
        }]
    )
    return response


if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPEN_API_KEY")
    
    clusters = []
    
    with open('easydata.csv') as f:
        reader = csv.reader(f) 
        # Append each row from data.csv into split_data
        for row in reader:
            if row[0].startswith('Cluster'):

                numeric_part = re.sub(r'\D', '', row[0])

                clusters.append({
                    'id': numeric_part,
                    'questions': []
                })
            else:
                clusters[-1]['questions'].append(row[1])
    
    # print(clusters)
    
    titles = generate_prompt(clusters)
    # for cluster in clusters:
    #     titles.append(generate_prompt(cluster))
    print('titles: ', titles)
