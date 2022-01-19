# Data Hour: Introducing Panel

### What is Panel?

[Panel](https://panel.holoviz.org/) is a high-level app and dashboarding solution for Python. It abstracts much of the complexity of building an interactive tool and makes building relatively easy. But really, it's easier to show rather than try to fully explain. Some examples:
- Simple public dashboard example: [Iris Kmeans Clustering](https://panel.holoviz.org/gallery/simple/iris_kmeans.html#simple-gallery-iris-kmeans)
- Complex public dashboard example: [Gapminder](https://gapminders.pyviz.demo.anaconda.com/gapminders)
- Simple app example: [Power BI Embeddable Frame Link Builder](https://pbi-embed-code-build.herokuapp.com/)

### Demo Scenario
For this demo, we're going to pull data from the Ravelry API. What's Ravelry? It's a social website for people who craft with yarn (i.e. knitters and crocheters). One of the elements of this social site is a large library of patterns. Some are free, and some are for sale. Our goal: explore the pattern price based on different variables, both about the pattern and the designer. Writing a sweater pattern is more work than writing a pattern for a hat, so we want to make sure to only compare like items, which we'll do using a search query in our API calls. 

| Variable | Description | 
| --------- | ----------- |
| id | Pattern id |
| name | Pattern name |
| designer_favorited | How many times the designer has been favorited by site users | 
| designer_pattern_count | How many patterns the designer has published on the site | 
| projects_count | How many times a pattern has been used in a project |
| rating_average | Average rating of the pattern (how much it is liked) |
| rating_count | How many times the pattern has been rated | 
| favorites_count | How many times has someone saved the pattern to their favorites |
| difficulty_average | How difficult is the pattern to complete? |
| difficulty_count | How many difficulty ratings have been logged |
| price | numeric component of price | 
| currency | Type of currency used in listing price | 

#### *Want to try it yourself?*
You'll need a few things if you want to replicate this project exactly for yourself. 
- A [Ravelry](https://www.ravelry.com/) Pro account (it's free!). This is needed to set up the Basic API authentication. 
- A Python environment with the packages listed and their dependencies. I use Anaconda for my environment management, but use what works for you. 
  - Panel
  - Pandas
- A Github account. You'll need to create a repo to start. This repo will get connected to Heroku in the publish stage.
- A [Heroku](https://www.heroku.com/) account (also free!). This is to publish the final built app to a web platform. Heroku is a PaaS provider, and the free tier is sufficient for these purposes

### Links
- A recording of the live demo is available to Unifiers internally [here](link). 
- The published app is available [here](link). 

### What is Data Hour?
Unify's Data Hour series brings examples of new tech to busy consultants. The goal is to introduce new tech that other consultants are working with, and create commmunity around learning new things. Presentations encompass data viz, data engineering, and data science topics, as well as data literacy and ethics. 
