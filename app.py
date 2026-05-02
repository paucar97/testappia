from flask import Flask, render_template_string
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title="My API", description="My API", doc=False)

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


REDOC_TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <title>My API - Docs</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
    <style>body { margin: 0; padding: 0; }</style>
  </head>
  <body>
    <redoc spec-url="/swagger.json" expand-responses="200"></redoc>
    <script src="https://cdn.jsdelivr.net/npm/redoc/bundles/redoc.standalone.js"></script>
  </body>
</html>
"""


@app.route("/docs")
def redoc():
    return render_template_string(REDOC_TEMPLATE)


if __name__ == "__main__":
    app.run(debug=True)
