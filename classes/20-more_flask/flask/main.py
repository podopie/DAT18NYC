from flask import Flask, render_template, request
from flaskext.markdown import Markdown
import json
import folium
import glob

# imports for classifier re-example
from lyrics_classifier import LyricsClf
lclf = LyricsClf('classifier.p')

# imports for beer similarity
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import manhattan_distances
beers = pd.read_csv('beer.csv').set_index('Beer')
distances = manhattan_distances(beers)

# setup application
app = Flask(__name__)
app.debug = True
Markdown(app)

def blog_posts():
    """this function should search for the blog posts that exist in
    the folder /posts, and create a list of tuples with the cleaned up title
    and the filename.
    ex: ['2015-04-06_my_first_blog_post']
    """
    files = glob.glob("posts/*.md")
    return [f.split('/')[1].split('.')[0] for f in files]

posts = blog_posts()

@app.route('/')
def make_a_map():
    map = folium.Map([40.7127, -74.0059])
    map._build_map()
    return map.HTML

@app.route('/blog')
def blog_index():
    """this route should pull in the posts variable from above."""
    return render_template('blog/index.html', posts=posts)

@app.route('/blog/<page>')
def blog_post(page):
    """this route handles the endpoint for showing a blog post.
    it should pass take the page variable as the filename for a markdown
    file found in the blog folder, open that file, and pass it is to the template.
    """
    loc = 'posts/'
    md = open(loc + page + '.md')
    return render_template('blog/markdown.html', text=md.read())

@app.route('/notebooks/')
def notebooks_index():
    """let's reuse the template here, but make sure all the links now point
    to the notebooks folder."""
    return render_template('blog/index.html', posts=[])

@app.route('/notebooks/<page>')
def notebook_page(page):
    """This endpoint should handle the notebook html."""
    loc = 'notebooks/'
    return open(loc+page, 'rb').read()

@app.route('/api/predict')
def predict():
    """this route handles a prediction from passing a querystring parameter.
    It uses the lyrics classifier from the previous flask class.
    /api/predict/?text=we%20all%20live%20in%20a%20yellow%20submarine
    """
    # pass the song into the lclf object, like before

    # now, convert the results into json!

    # return the json data to the endpoint.
    return data

@app.route('/api/beer/similarity')
def similarity():
    """This route should return back the following json data:
    1. the original beer string
    2. an error if the beer was not found
    3. a dictionary of two beers and their similarity scores.
    """
    # get the "beer" argument from the querystring.

    # check to see if the searched beer is in the index of the beers list.
    # if it is, continue, otherwise, return back an error
    # find the index of that beer (code below)

    # use argsort() to find the first two beers in the distances array.
    # you only need to look at the distances based on the beer searched.
    # will you need the first beer listed?

    # use iloc to find the recommended beers

    # write the json

    # return the json
    return data

@app.route('/content/<content>')
def try_anything(content):
    return content

if __name__ == '__main__':
    app.run()
