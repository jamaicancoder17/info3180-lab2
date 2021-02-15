"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from flask import render_template, request, redirect, url_for, flash
import datetime
from app import app

def format_date_joined(date):
    date_joined = datetime.date(2016, 2, 7)
    return date_joined.strftime("%B, %Y")

###
# Routing for your application.
###


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Kyle Burke")


@app.route('/profile/')
def profile():
    hold = {}
    hold['name'] = "Marlon Williams"
    hold['tag'] = "@marlonWill14"
    hold['addr'] = "Spanish Town, Jamaica"
    hold['joined'] = format_date_joined(2017,1,5)
    hold['num_posts'] = 50
    hold['num_following'] = 1000
    hold['num_followers'] = 750
    hold['bio'] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus lacinia, sapien commodo malesuada consectetur, neque sem cursus dolor, et eleifend nunc mauris at dui. Quisque euismod sollicitudin vestibulum. Integer congue felis at urna gravida, eu euismod tellus consectetur. In hac habitasse platea dictumst. Suspendisse eu eleifend metus."
    return render_template('profile.html', params = hold)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
