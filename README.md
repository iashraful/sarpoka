# Sarpoka [![Python Packaging](https://github.com/iashraful/sarpoka/actions/workflows/python-packaging.yml/badge.svg?branch=master)](https://github.com/iashraful/sarpoka/actions/workflows/python-packaging.yml)
> Sarpoka is a rapidly development Python micro framework designed for serverless applications

## Installation
```sh
pip install sarpoka
```

## An example of usage
```python
from sarpoka import Sarpoka

app = Sarpoka()


@app.route('/')
def home(request, response, **kwargs):
    return 'Welcome Home!!'


@app.route('/api/me', methods=['GET', 'POST'])
def get_me(request, response, **kwargs):
    response.content_type = 'application/json'
    response.status_code = 200
    return {
        'name': 'Mohammad Ashraful Islam'
    }


@app.route('/about')
def about(request, response, **kwargs):
    return '''
  <h1>Mohammad Ashraful Islam</h1>
  <div>
    Senior Software Engineer at Field Buzz<br/>
  </div>
  '''
if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)

```

## Run the application
There are several ways. Let's walk one step at a time.
* Just run the example.py file(It's in my case here. In your case filename might different)
* You can use gunicorn to run the app at production level like following,
```shell
$ pip install gunicorn

$ gunicorn example:app # Filename:Object name. According to the example it's example and the app
```

## Features
* Basic Routing
* HTTP Method defining during route
* Query string support
* View function support only
* Serving html as string (File not supported yet.)

## Upcoming Features
* Database and ORM support
* Class based view support
* HTML/Markdown file rendering
* Template engine support
* ... will be added many more.
