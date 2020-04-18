# Word Ladder
This repo was created to accompany a word game I built and deployed to www.strohberryfields.com/word_ladder . I am working on several improvements to both the repo and the game, but in the meantime, you can explore the code used to create the game. 

<p align="center">
  <img src="scrabble.jpg" alt="word game" width="400">
</p>

## Using the Repo:
#### Part 1
To see the steps I took to generate the first collection of phrases, check out 'phrase_finder_gen1.py'. This has minor annotations, but I am currently writing a more thorough explanation of why I took certain steps, as well as which steps I will change when I create phrase collection 2.0. This will also feature instructions for how to replicate the process. 
#### Part 2
The steps I took to build & deploy the game app are slightly more elaborate. The necessary files are located in the folder "game_app". These are not yet annotated, but the app is ready to run in it's current state. The following code will launch the app locally. 
* python build_db.py
* python init_db.py
* python app.py


## About this Project

### Inspiration
The core idea of this game was inspired by the game show Chain Reaction. On the show, the phrases are always "common", two-word idioms in American English. Only rarely have I seen an unfamiliar turn of phrase pop up, so they set the bar high. Alas, I have yet to find an extensive database of idioms, let alone two-word idioms. The good news is that this gave me a way to make the project more data-sciencey (in technical terms). The bad news is that my current collection of phrases is bound to disappoint game show connoisseurs, including my mother, who has proclaimed that my "phrases are terrible". 

As for the data science, I built this because I love word games & I enjoy any excuse to do NLP. I have considered scraping online resources, but I wanted to start with the challenge of generating a collection of phrases using NLP tools. The current batch of phrases is a mix of idioms and pairs of words that happen to occur frequently in news stories. I use another repo ( https://github.com/kellystroh/Idiom_Adventure ) to test out approaches to improve the phrase collection. 

I also wanted to practice deploying a flask app that has more interactive functionality than my website. I am not a web developer, so this will not be the ideal example of best practices in web apps. That said, it has led me to explore lots of free resources, so I will eventually write out some tips for fellow beginners.

### Beware Weird Phrases
I used NLP tools to extract two-word phrases from 150,000 news articles. I took the most common 100,000 word pairings and removed words with fewer than three 'connecting' words to avoid potential dead ends. The resulting collection includes many phrases that do not qualify as common idioms, and a handful that may be offensive. An improved collection is in the works!

### Improvements in Progress
* Improved Collection of Phrases (including a fix to faulty lemmatization)
* ~~Better web formatting.~~. I'd like to make a How-To guide ~~, but I'm too embarassed to share shoddy HTML files.~~ I am no longer embarassed of my HTML files, though they'll only feature in the How-To guide to demonstrate the Flask components
* ~~GitHub links.~~ I'm working to make the GitHub repo easier to navigate ~~before sharing.~~
* Change Scoring method. It seemed fair to award fewer points for guessing the word "book" if the preview is "boo" than if the preview is "b". However, the current formula could unfairly disadvantage a player for getting shorter words.
* Enable phrase feedback. Building a tool allowing users to mark phrases that should be removed from the collection. I'd like an easy path to remove phrases that users deem inappropriate or offensive. The pairing process takes out of their intended context, and news stories can cover sensitive topics.
* Game stats. My latest improvement added a new table to collect data on words used, answers given, and number of guesses before answering correctly. I'd like to publish random facts, like which words appear most often and which words are hardest to guess
