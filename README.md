# Word Ladder

This repo was created to accompany a word game I built and deployed to www.strohberryfields.com/word_ladder . I am working on several improvements to both the repo and the game, but in the meantime, you can explore the code used to create the game. 

## Using the Repo:
To see the steps I took to generate the first collection of phrases, check out 'phrase_finder_gen1.py'. This has minor annotations, but I am currently writing a more thorough explanation of why I took certain steps, as well as which steps I will change when I create phrase collection 2.0.  



## About this Project

### Collecting Phrases

My current collection of phrases contains some pretty I used NLP tools to extract two-word phrases from 150,000 news articles. I took the most common 100,000 word pairings and removed words with fewer than three 'connecting' words to avoid potential dead ends. The resulting collection includes many phrases that do not qualify as common idioms, and a handful that may be offensive. An improved collection is in the works!

