from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from EmotionController import EmotionController

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
api = Api(app)


class EmotionScore(Resource):
    emotionController = EmotionController()
    def get(self, text):
        return self.emotionController.scoreForText(text)


class EmotionScoreList(Resource):
    emotionController = EmotionController()

    def get(self, location):
        return self.emotionController.start(location)

class TweetScoreList(Resource):
    emotionController = EmotionController()

    def get(self, hashtag):
        return self.emotionController.getTweetsScores(hashtag)


api.add_resource(EmotionScore, "/emotion/score/<string:text>")
api.add_resource(EmotionScoreList, "/emotion/score/location/<string:location>")
api.add_resource(TweetScoreList, "/tweet/score/<string:hashtag>")


if __name__ == '__main__':
    app.run(debug=True)
#app.run()
