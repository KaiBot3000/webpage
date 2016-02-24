from flask_restful import Resource, Api, abort
import random

replies = {
    "english": ["yes", "no", "I think so", "try a different approach", "ask again"],
    "spanish": ["si", "no", "creo que si", "tal vez", "eso espero", "pregunta de nuevo"],
    "cat": ["purrrfectly possible", "hiss no", "mouse-t certainly", "*silent stare*"],
    "french": ["a chaque jour suffit sa peine", "non", "c'est kif-kif et bourricot",
                "ce ne sont pas vos oignons", "la mort du petit cheval",
                "qui vivra, verra", "sans l'ombre d'un doute",
                "triste comme un repas sans fromage"]
    }


class Magic(Resource):
    def get(self, language="english"):
        """Given a language (english is default), returns random reply"""

        if language in replies.keys():
            reply = random.choice(replies[language])
            return {"reply": reply}
        else:
            abort(400, message="Language not available")


class Language(Resource):
    def get(self):
        """Returns a list of available languages"""

        languages = replies.keys()
        return {"languages": languages}
