# import pandas as pd
import csv
import os
import openai
from dotenv import load_dotenv
import numpy as np

# data = pd.read_csv('./data.csv')

# print(data)
# split_data = [[]]
# for row in data:
#     split_data.append(row.split(','))

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")


# gets title from gpt
def generate_title(cluster):
    # print("cluster is: ", cluster)
    prompt = " Please answer with a single phrase: What is a good category name for the following questions?"
    for x in cluster:
        prompt += "\n" + x
    print(prompt)

    
    # response = openai.Completion.create(prompt=prompt, max_tokens = 20)

if __name__ == "__main__":

    split_data = np.array()
    cluster_starts = []

    # get all clusters in 1 array and store the index of the start of each cluster
    with open('data.csv') as f:
        # get the data into 2d array
        reader = csv.reader(f)
        for row in reader:
            split_data.append(row)

        for i in range(len(split_data)):

            # store the index of the start of each cluster
            if "Cluster" in split_data[i][0]:
                cluster_starts.append(i+1+1)

    # split the data into clusters
    clusters = []
    for i in range(len(cluster_starts)-1):
        clusters.append(split_data[cluster_starts[i]:cluster_starts[i+1]])

    # for i in range(len(cluster_starts)):
    #     if i == len(cluster_starts)-1:
    #         clusters.append(split_data[cluster_starts[i]:])
    #     else:
    #         clusters.append(split_data[cluster_starts[i]:cluster_starts[i+1]])

    # get a title from gpt
    # generate_title(["hello", "world", "this", "is", "a", "test"])
    # print(clusters[0])
    # print(split_data[1])
    print(clusters.shape)
    # generate_title(clusters[0][1:])