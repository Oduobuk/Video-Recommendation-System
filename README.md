## Video-Recommendation-System

# To implement the recommendation system, we'll follow these steps:

1. Data Parsing: Load and parse the JSON data into appropriate data structures.
2. Similarity Calculation: Implement a function to calculate the similarity between videos based on their metadata (category and tags).
3. Recommendation Algorithm: Develop an algorithm to generate video recommendations for a user based on their watch history and video similarities.
4. Top-N Recommendations: Implement a function to return the top N recommended video IDs for a given user ID.

# Explanation

1. Data Parsing:
   - The `parse_data` function extracts the watch history and video metadata from the JSON file.

2. Similarity Calculation:
   - The `calculate_similarity` function computes the similarity between two videos based on their category and tags.
   - The `build_similarity_matrix` function constructs a matrix that stores the similarity between each pair of videos.

3. Recommendation Algorithm:
   - The `recommend_videos` function identifies candidate videos (videos not yet watched by the user) and ranks them based on their similarity to the videos in the user's watch history.

4. Top-N Recommendations:
   - The `get_top_n_recommendations` function returns the top N recommended video IDs for a given user ID.

This code is designed to be efficient and scalable, making it suitable for a platform with many users and videos. The similarity matrix allows for quick lookups and similarity calculations, and the use of defaultdict ensures that the algorithm handles missing keys gracefully.
