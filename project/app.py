from flask import Flask, request, jsonify
from cassandra.cluster import Cluster
import json
import requests
import requests_cache

cluster = Cluster(contact_points=['172.17.0.2'],port=9042)
session = cluster.connect()
app = Flask(__name__)

requests_cache.install_cache('movie_api_cache', backend='sqlite', expire_after=36000)

omdb_url='http://www.omdbapi.com/?t={title}&apikey={key}'
my_key='cefcfc7e'

@app.route('/')
def hello():
    return '<html><body><h1>MOVIE RESTful API</h1></body></html>'

@app.route('/movies', methods=['GET', 'DELETE'])
def g_d_movie():
    if request.method == 'GET':
        title= request.args.get('title')
        url= omdb_url.format(title = title, key= my_key)
        print(url)
        resp = requests.get(url)
        if resp.ok :
            response = resp.json()
            return jsonify (response)
        else :
            return (resp.json)
    if request.method == 'DELETE':
        query = request.args
        rows = session.execute("""DELETE FROM movies.list WHERE title='{}';""".format(query['title']))
        return jsonify({'ok': True, 'message': 'Movie data deleted successfully!'}), 200

@app.route('/new', methods=['POST'])
def new_movie():
    query=request.args
    rows= session.execute("""Insert into movies.list(title) values('{}');""".format(query['title']))
    return jsonify ({'ok': True, 'message': 'Movie added successfully'}), 200



@app.route('/movies/<title>', methods=['GET'])
def get_title(title):
    rows = session.execute( """Select * From movies.list where title = '{}'""".format(title))
    for p in rows:
        return('<h1>{} is in Netflix!</h1>'.format(title))
    return('<h1>That Movie does not exist!</h1>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443,ssl_context=('cert.pem','key.pem'))

