from flask import Flask
from flask_restful import Resource, Api
from Services.services import metoda_czytaj_film
from Services.services import metoda_czytaj_link
from Services.services import metoda_czytaj_ocene
from Services.services import metoda_czytaj_tag

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class HelloWorld1(Resource):
    def get(self):
        return metoda_czytaj_film("Data/movies.csv")

api.add_resource(HelloWorld1, '/movies')

class HelloWorld2(Resource):
    def get(self):
        return metoda_czytaj_link("Data/links.csv")

api.add_resource(HelloWorld2, '/links')

class HelloWorld3(Resource):
    def get(self):
        return metoda_czytaj_ocene("Data/ratings.csv")

api.add_resource(HelloWorld3, '/ratings')

class HelloWorld4(Resource):
    def get(self):
        return metoda_czytaj_tag("Data/tags.csv")

api.add_resource(HelloWorld4, '/tags')


#pliczek = Movie()
#print(pliczek.__dict__)
#Movie.__dict__

#axb = metoda_czytaj('Data/movies.csv')
#print(axb)
#print(type(axb))
#for row in axb:
#    listax = row.split(",")
#    print(listax)

if __name__ == '__main__':
    app.run(debug=True)
