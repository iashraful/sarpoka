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
        'name': 'Mohammad Ashraful Islam',
    }


@app.route('/about')
def about(request, response, **kwargs):
    return '''
  <h1>Mohammad Ashraful Islam</h1>
  <div>
    Senior Software Engineer at Field Buzz <br/>
    Tel: +8801624153810
  </div>
  '''


app.run(debug=True)
