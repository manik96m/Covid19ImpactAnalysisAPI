from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from EmotionController import EmotionController

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
api = Api(app)


class EmotionScore(Resource):
    def get(self):
        return {}


class EmotionScoreList(Resource):
    emotionController = EmotionController()

    def get(self, location):
        return self.emotionController.start(location)


api.add_resource(EmotionScore, "/emotion/score")
api.add_resource(EmotionScoreList, "/emotion/score/location/<string:location>")

if __name__ == '__main__':
    app.run(debug=True)
#app.run()
