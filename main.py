import sqlite3
from flask import Flask, render_templates

app = Flask(__name__)
@app.route('/')
def main():
  return render_templates('index.html')

if __name__ == '__main__':
  app.run(port=2000, host='localhost')
