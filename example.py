from sarpoka import Sarpoka

app = Sarpoka()


@app.route('/')
def home(request, response, **kwargs):
  return 'Welcome Home!!'



@app.route('/about')
def about(request, response, **kwargs):
  return '''
  <h1>Mohammad Ashraful Islam</h1>
  <div>
    Senior Software Engineer at Field Buzz <br/>
    Tel: +8801624153810
  </div>
  '''