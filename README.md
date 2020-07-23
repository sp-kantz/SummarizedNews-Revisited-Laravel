# SummarizedNews-Revisited-Laravel

-- Summarized News -- [Laravel]

Remake of my thesis project on Extractive Multi-Document Summarization.

+ Added user accounts. 
+ Users can leave comments on summaries.
+ Admin (user with id=1) can start the process with a button.


-> Database: SummarizedNews.sql - Credentials on .env file
-> Python has to be installed on server.
-> Essential python libs: scrapy, scikit-learn, nltk, networkx, mysql-connector

---------------------------------------------------------------------

System to collect news articles from the web,
automatically extract summaries from multiple articles with overlapping content
and present the summaries to the users.

System Processes:
1. Collects recent news articles with a crawler from various websites (The Independent, The Guardian, BBC, RT, Sky News, CTV News, The New York Times, CBS News).

2. Extracts useful text and data from the articles (article text, title, url, domain), and preprocesses text.

3. Performs agglomerative clustering on the article collection. Each cluster consists of articles describing the same event or topic.

4. Applies two extractive summarization techniques to generate two summaries for each cluster.
The first technique is based on latent semantic analysis (LSA), and the second on a graph representation of the text.

5. Presents the summaries on a webpage.
