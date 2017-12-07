from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient("192.168.33.13")
db = client.webapp

@app.route("/")
def hello():
   body = "<h1>{title}</h1>\n<img height='300' src='{gif}'><img>\n<article>{article}</article>\n"
   page = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">'
   for ob in db.webapp.find():
      page += body.format(
      article=ob['article'],
      title=ob['title'],
      gif=ob['gif']
      )
   return page

if __name__ == "__main__":
   app.run(host='0.0.0.0')

