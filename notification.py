#import Flask from flask
#import Resource, Api from flask_restful
#
#create app using Flask
#create api using Api
#
#create resource class inheriting from Resource
#define methods returning desired data and status code
#
#route resource using api.add_resource(resource_class, 'route')
#url parameter syntax: /x/y/<type:variable> #/blab/bleb/<string:blub>
#
#run app using app.run(port=value)

import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

estado = True

class Lembrete(Resource):
    def get(self):
        global estado
        estado = not estado
        return {"caboclo_esqueceu_de_comer_goiabada": estado }, 200

class Default(Resource):
    def get(self):
        return {"default": "test" }, 200

api.add_resource(Lembrete, '/lembretes')
api.add_resource(Default, '/')

#if __name__ == '__main__':
port_from_env = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port_from_env)