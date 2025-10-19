# Youtube Crawler

This project is a web-based application developed to analyze the most common words associated with specific phrases in the titles, descriptions, and comments of YouTube videos.
It was mainly created as an experiment to familiarize myself with using Youtube's API, using NTLK, and to practice working in JavaScript.

### What is this project?
This project consists of a web crawler that looks for the most common words associated with a specified phrase on YouTube.

As an example, the phrase "toki pona" is used in this project. 
The YouTube Crawler searches for the top 50 videos containing the word "toki pona" in their titles, descriptions, or comments. 
It then extracts the most frequent words associated with "toki pona" using NLTK. 
The resulting words and their frequencies are then graphed using Chart.js to visualize the prominence of these words in the analyzed YouTube content.

![image](https://github.com/smoll24/YT-Crawly-Crawler/assets/115204665/0aea4f05-740a-416d-b635-e31d627217c7)

### What does this project use?

* I used YouTube's Data API to fetch video titles, descriptions, and comments of YouTube videos that included the phrase "toki pona".
* I used NLTK (Natural Language Toolkit) to tokenize these titles, descriptions, and comments, and filter out any words shorter than 3 characters long.
* I then graphed the 10 most common words (tokens) that were found using Chart.js.

### How do I run this project?
The site is unfortunately not currently hosted anywhere.

To run the project locally, follow these steps:
* Clone the repository to your local machine.
* Open the HTML file (index.html) in a web browser.
* Or use the Repl.it version, that can be found here: [https://replit.com/@smoll24/YT-Crawly-Crawler#index.html](https://replit.com/@smoll24/YT-Crawly-Crawler?v=1)

### Contributions
Contributions to this project are welcome. If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.
