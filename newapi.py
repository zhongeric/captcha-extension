from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
app = Flask(__name__)
api = Api(app)
# create new model objec

parser = reqparse.RequestParser()
parser.add_argument('g-captcha-response')
parser.add_argument('email-id')
user_cap = {}

class solve(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        g_cap_response = args['g-captcha-response']
        email_id = args['email-id']

        output = {'g_cap_response': g_cap_response, 'email-id': email_id}
        print(output)
        user_cap[email_id] = g_cap_response

        return output

api.add_resource(solve, '/solve')

class getJson(Resource):
    def get(self):
        # use parser and find the user's quer

        return user_cap

api.add_resource(getJson, '/json')

# example of another endpoint
# api.add_resource(PredictRatings, '/ratings')

if __name__ == '__main__':
    app.run(port=3500)
