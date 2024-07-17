## Design of Flask Application

**HTML Files:**

* **index.html**: The main page of the website that will contain two text boxes and a submit button. The HTML code should be as follows:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Text Box Website</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-rbsA2VBKQhno3Z4D9l6RwRZ5gKL3dy4OgErp6O4/+IMiDYVJn5yBsJD74kgas+Yc"
      crossorigin="anonymous"
    />
  </head>

  <body>
    <div class="container">
      <h1>Text Box Website</h1>
      <form action="/result" method="post">
        <div class="mb-3">
          <label for="text1" class="form-label">Text Box 1</label>
          <input type="text" class="form-control" id="text1" name="text1" />
        </div>
        <div class="mb-3">
          <label for="text2" class="form-label">Text Box 2</label>
          <input type="text" class="form-control" id="text2" name="text2" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-kenU1KFdBIe4zVF0s0G1M57VBGfcjjbztnA3692T5g5fQztuT8UFhv7Z36Up25E"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

* **result.html**: The page that will display the result of the user's input. The HTML code should be as follows:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Text Box Website</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-rbsA2VBKQhno3Z4D9l6RwRZ5gKL3dy4OgErp6O4/+IMiDYVJn5yBsJD74kgas+Yc"
      crossorigin="anonymous"
    />
  </head>

  <body>
    <div class="container">
      <h1>Text Box Website</h1>
      {% if result %}
      <p>
        The text entered in Box 1 is: {{ result.text1 }}
      </p>
      <p>
        The text entered in Box 2 is: {{ result.text2 }}
      </p>
      {% endif %}
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-kenU1KFdBIe4zVF0s0G1M57VBGfcjjbztnA3692T5g5fQztuT8UFhv7Z36Up25E"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

**Routes:**

* **index**: The route for the main page of the website. This route is typically defined in the `__init__.py` file and decorated with the `@app.route()` decorator. It should render the `index.html` file.
```python
@app.route("/")
def index():
    return render_template("index.html")
```

* **result**: The route for the result page. This route is also typically defined in the `__init__.py` file and decorated with the `@app.route()` decorator. It should render the `result.html` file and pass the result of the user's input to the template.
```
import flask

@app.route("/result", methods=["POST"])
def result():
    text1 = flask.request.form.get("text1")
    text2 = flask.request.form.get("text2")
    return render_template("result.html", result={"text1": text1, "text2": text2})
```