#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from collections import defaultdict
from itertools import combinations
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load data
file_path = r'C:/Users/ODUOBUK/data.json'
with open(file_path, 'r') as file:
    data = json.load(file)

users = data['users']
videos = data['videos']


# 1. Data Parsing:
#    - The `parse_data` function extracts the watch history and video metadata from the JSON file.
# 

# In[2]:


# Data Parsing
def parse_data(users, videos):
    user_watch_history = {user['user_id']: user['watch_history'] for user in users}
    video_metadata = {video['video_id']: video for video in videos}
    return user_watch_history, video_metadata

user_watch_history, video_metadata = parse_data(users, videos)
print("User Watch History:")
print(json.dumps(user_watch_history, indent=2))
print("\nVideo Metadata:")
print(json.dumps(video_metadata, indent=2))


# 2. Similarity Calculation:
#    - The `calculate_similarity` function computes the similarity between two videos based on their category and tags.
#    - The `build_similarity_matrix` function constructs a matrix that stores the similarity between each pair of videos.
# 

# In[3]:


# Similarity Calculation
def calculate_similarity(video1, video2):
    category_similarity = 1 if video1['category'] == video2['category'] else 0
    tag_similarity = len(set(video1['tags']).intersection(set(video2['tags']))) / len(set(video1['tags']).union(set(video2['tags'])))
    return category_similarity + tag_similarity

def build_similarity_matrix(videos):
    similarity_matrix = defaultdict(dict)
    for video_id1, video_id2 in combinations(videos.keys(), 2):
        similarity = calculate_similarity(videos[video_id1], videos[video_id2])
        similarity_matrix[video_id1][video_id2] = similarity
        similarity_matrix[video_id2][video_id1] = similarity
    return similarity_matrix

similarity_matrix = build_similarity_matrix(video_metadata)

print("\nSimilarity Matrix:")
for video1, similarities in similarity_matrix.items():
    for video2, similarity in similarities.items():
        print(f"Similarity between {video1} and {video2}: {similarity}")
        

        


# 3. Recommendation Algorithm:
#    - The `recommend_videos` function identifies candidate videos (videos not yet watched by the user) and ranks them based on their similarity to the videos in the user's watch history.
# 

# In[4]:


# Recommendation Algorithm
def recommend_videos(user_id, n):
    watched_videos = set(user_watch_history[user_id])
    candidate_videos = defaultdict(float)

    for video_id in watched_videos:
        for candidate_id, similarity in similarity_matrix[video_id].items():
            if candidate_id not in watched_videos:
                candidate_videos[candidate_id] += similarity

    recommended_videos = sorted(candidate_videos, key=candidate_videos.get, reverse=True)[:n]
    return recommended_videos


# 4. Top-N Recommendations:
#    - The `get_top_n_recommendations` function returns the top N recommended video IDs for a given user ID.
# 

# In[9]:


# Flask Routes
@app.route('/recommend/<int:user_id>/<int:n>', methods=['GET'])
def get_top_n_recommendations(user_id, n):
       recommendations = recommend_videos(user_id, n)
       print(f"\nTop {n} recommendations for user {user_id}: {recommendations}")        
       return jsonify(recommendations)

if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)

else:
   print("No data to process.")


# In[10]:


# Example usage
user_id = 1
n = 5
print(get_top_n_recommendations(1, 5))


# In[ ]:




