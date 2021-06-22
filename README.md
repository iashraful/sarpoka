# Fast DRF [![Python Packaging](https://github.com/iashraful/sarpoka/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/iashraful/sarpoka/actions/workflows/python-package.yml)
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