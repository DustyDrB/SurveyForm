from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

   
    def index(self):
        if 'count' not in session:
            session['count'] = 0
        if 'name' not in session:
            session['name'] = ''
        if 'language' not in session:
            session['language'] = ''
        if 'location' not in session:
            session['location'] = ''
        if 'comment' not in session:
            session['comment'] = ''
        return self.load_view('survey.html')

    def survey(self):
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        session['count'] += 1

        return redirect('/result')
    def result(self):
        return self.load_view('result.html')