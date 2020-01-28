# Word Ladder

This repo was created to accompany a word game I built and deployed to www.strohberryfields.com/word_ladder . I am working on several improvements to both the repo and the game, but in the meantime, you can explore the code used to create the game. 

## Using the Repo:
To see the steps I took to generate the first collection of phrases, check out 'phrase_finder_gen1.py'. This has minor annotations, but I am currently writing a more thorough explanation of why I took certain steps, as well as which steps I will change when I create phrase collection 2.0.  



## About this Project

### Collecting Phrases

My current collection of phrases contains some pretty I used NLP tools to extract two-word phrases from 150,000 news articles. I took the most common 100,000 word pairings and removed words with fewer than three 'connecting' words to avoid potential dead ends. The resulting collection includes many phrases that do not qualify as common idioms, and a handful that may be offensive. An improved collection is in the works!

### Improvements in Progress
* Improved Collection of Phrases (including a fix to faulty lemmatization)
* ~~Better web formatting.~~ I'd like to make a How-To guide~~, but I'm too embarassed to share shoddy HTML files.~~ I am no longer embarassed of my HTML files, though they'll only feature in the How-To guide to demonstrate the Flask components
* GitHub links. I'm working to make it easier to navigate before sharing.
* Change Scoring method. It seemed fair to award fewer points for guessing the word "book" if the preview is "boo" than if the preview is "b". However, the current formula could unfairly disadvantage a player for getting shorter words.
* Enable phrase feedback. Building a tool allowing users to mark phrases that should be removed from the collection. I'd like an easy path to remove phrases that users deem inappropriate or offensive. The pairing process takes out of their intended context, and news stories can cover sensitive topics.
* Game stats. My latest improvement added a new table to collect data on words used, answers given, and number of guesses before answering correctly. I'd like to publish random facts, like which words appear most often and which words are hardest to guess
