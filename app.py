import requests
import pprint

from flask import Flask, render_template, render_template_string


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-greeting/<start_str>", methods=['POST'])
def get_greeting(start_str):
    templ = """
    <div class="block">
        <h1 class="title">{{ title }}</h1>
        <p>{{ greeting }}</p>
    </div>
    """
    r = requests.post(
            "https://api.deepai.org/api/text-generator",
            data = {
                "text": start_str 
                },
            headers={ 'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K' }
            )
    pprint.pprint(r)
    response = r.json()
    return render_template_string(templ, greeting=response["output"], title=start_str)



if __name__ == "__main__":
    app.run(debug=True)
