# Youtube Crawler

This project is a web-based application developed to analyze the most common words associated with specific phrases in the titles, descriptions, and comments of YouTube videos.

Link: yt-crawly-crawler.smoll24.repl.co/

### Overview
YT Crawler aims to find the most common words associated with particular phrases in the titles, descriptions, and comments of Youtube videos.

As an example, the phrase "toki pona" is used in this project. 
The YouTube Crawler searches for the top 50 videos containing the word "toki pona" in their titles, descriptions, and comments. 
It then extracts the most frequent words associated with "toki pona" using NLTK. 
The resulting words and their frequencies are then graphed using Chart.js to visualize the prominence of these words in the analyzed YouTube content.

### Features

* Data Retrieval: The project interacts with the YouTube Data API to fetch the required data, including video titles, descriptions, and comments.
* Word Extraction: Using NLTK (Natural Language Toolkit), the application applies part-of-speech tagging and filtering techniques to extract relevant words associated with the specified phrase.
* Frequency Analysis: The extracted words are then analyzed, and their frequencies are calculated using the Counter class from the collections module.
* Graph Visualization: The most frequent words and their corresponding frequencies are graphically represented using Chart.js, providing a visual representation of the prominence of these words in the analyzed YouTube content.

### How to Run
To run the project locally, follow these steps:
* Clone the repository to your local machine.
* Open the HTML file (index.html) in a web browser.
* Or use the Repl.it version, that can be found here: [https://replit.com/@smoll24/YT-Crawly-Crawler#index.html](https://replit.com/@smoll24/YT-Crawly-Crawler?v=1)

### Contributions
Contributions to this project are welcome. If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.
