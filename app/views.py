"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from werkzeug.utils import secure_filename
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import ProfileForm
from app.models import UserProfile
import datetime


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
    return render_template('about.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTS']


@app.route('/profile',methods = ["GET","POST"])
def profile():
    """Render the website's profile page"""
    form   = ProfileForm()
    user_no = len(UserProfile.query.all())
    
    if request.method == "POST" and form.validate_on_submit():
        
        first_name = form.first_name.data
        last_name  = form.last_name.data
        gender     = form.gender.data
        location   = form.location.data
        email      = form.email.data
        bio        = form.biography.data
        date       = datetime.datetime.now()
        image      = form.image.data
        imageName  = first_name + last_name + str(user_no) + ".png"
        
        # file = form.upload.data
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
        new_user = UserProfile( first_name = first_name,
                                last_name  = last_name,
                                gender     = gender,
                                location   = location,
                                email      = email,
                                biography  = bio,
                                created_on = date,
                                profilePic = imageName)
        db.session.add(new_user)
        db.session.commit()
        
        image.save(os.path.join(app.config['UPLOAD_FOLDER'],imageName))
        
        # image.save("app/static/profilepictures/" + imageName + ".png")
        
        flash("New User Profile Created", "success")
        return redirect(url_for("profiles"))
        
    return render_template("profile.html",form=form)


@app.route('/profile/<userid>')
def userProfile(userid):
    """Display individual user profile given the userid"""
    user = UserProfile.query.filter_by(userid = userid).first()
    return render_template('userprofile.html',user = user, date= user.created_on.strftime("%B %d, %Y"))


@app.route('/profiles')
def profiles():
    """Render the website's list of profiles"""
    users = UserProfile.query.all()
    return render_template("profiles.html", users = users)


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
    and also to cache the rendered page for 10 minutes.
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