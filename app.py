from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title="My API", description="API with Swagger UI", doc="/docs")

ns = api.namespace("api", description="Endpoints")

hello_model = api.model("HelloResponse", {
    "response": fields.String(example="hello world"),
    "key": fields.String(example="item"),
})


@ns.route("/hello")
class Hello(Resource):
    @ns.doc("get_hello")
    @ns.marshal_with(hello_model)
    def get(self):
        """Returns a hello world message"""
        return {"response": "hello world", "key": "item"}


if __name__ == "__main__":
    app.run(debug=True)
