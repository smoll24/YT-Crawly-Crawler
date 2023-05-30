from googleapiclient.discovery import build

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk

from collections import Counter
import re
import json

youtube = build('youtube', 'v3', developerKey='API_KEY')

#search for the most popular videos containing the word 'crow' in their titles or descriptions
search_response = youtube.search().list(
    q='toki pona',
    part='snippet',
    type='video',
    order='viewCount',
    maxResults=50
).execute()

#Retrieve video information
videos = []
for item in search_response['items']:
    video_title = item['snippet']['title']
    video_description = item['snippet']['description']

    # Check if 'statistics' field is available
    if 'statistics' in item:
        view_count = item['statistics']['viewCount']
        like_count = item['statistics']['likeCount']
    else:
        # Set default values if 'statistics' field is not present
        view_count = 0
        like_count = 0

    videos.append({
        'title': video_title,
        'description': video_description,
        'viewCount': view_count,
        'likeCount': like_count
    })
    
# Process the video titles, descriptions, and comments to extract relevant words
stop_words = set(stopwords.words('english'))
words = []
for video in videos:
    # Tokenize the title, description, and comments into words
    title_words = word_tokenize(video['title'])
    desc_words = word_tokenize(video['description'])

    # Retrieve comments for the video
    video_id = item['id']['videoId']
    comments_response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100
    ).execute()

    # Process each comment
    for comment_item in comments_response['items']:
        comment = comment_item['snippet']['topLevelComment']['snippet']['textDisplay']
        comment_words = word_tokenize(comment)
        # Combine the words from title, description, and comments
        all_words = title_words + desc_words + comment_words
         # Filter out stop words, words shorter than 3 characters, and specific patterns
        filtered_words = [
            word.lower()
            for word in all_words
            if (
                word.lower() not in stop_words
                and len(word) > 2
                and not re.search(r'\.{3}|https|http|href=|/www\.youtube\.com/watch|v=', word.lower())
            )
        ]
        # Append the filtered words to the 'words' list
        words.extend(filtered_words)

# Count the frequency of each word
word_counts = Counter(words)
# Get the most common words and their frequencies
top_words = word_counts.most_common(10)


print(top_words)


# Convert the data to a dictionary
data = {
    'top_phrases': top_words
}

# Write the data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)