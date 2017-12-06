from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient("192.168.33.13")
db = client.webapp

@app.route("/")
def hello():
   body = "<h1>{title}</h1>\n<img src='{gif}'><img>\n<article>{article}</article>\n"
   page = ''
   for ob in db.webapp.find():
      page += body.format(
      article=ob['article'],
      title=ob['title'],
      gif=ob['gif']
      )
   return page

if __name__ == "__main__":
   app.run(host='0.0.0.0')

