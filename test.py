import csv
import os
import openai
from dotenv import load_dotenv

def generate_prompt(cluster):
    # print("cluster is: ", cluster)
    prompt = " Please answer with a single phrase: What is a good category name for the following questions?"
    for x in cluster:
        prompt += "\n" + x
  
    response = openai.Completion.create(
        model="gpt-3.5.turbo",
        prompt=prompt, 
        max_tokens=20
    )
    return response



if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPEN_API_KEY")
    
    clusters = []
    
    with open('data.csv') as f:
        reader = csv.reader(f) 
        # Append each row from data.csv into split_data
        for row in reader:
            if row[0].startswith('Cluster'):
                clusters.append([])
            else:
                clusters[-1].append(row[1])
                
    titles = []
    for cluster in clusters:
        titles.append(generate_prompt(cluster))

    print(titles)
