from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
api = Api(app)


class EmotionScore(Resource):
    def get(self):
        return {}


class EmotionScoreList(Resource):
    def get(self, location='CANADA'):
        return {}


api.add_resource(EmotionScore, "/emotion/score/<string:location>")
api.add_resource(EmotionScoreList, "/emotion/score/location/<string:location>")

app.run()
