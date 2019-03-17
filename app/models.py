from . import db


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    userid     = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name  = db.Column(db.String(80))
    email      = db.Column(db.String(255))
    gender     = db.Column(db.String(16))
    location   = db.Column(db.String(255))
    biography  = db.Column(db.Text)
    profilePic = db.Column(db.String(255))
    created_on = db.Column(db.Date)
    
    
    def __init__(self,first_name,last_name,email,gender,location,biography,profilePic,created_on):
        self.first_name = first_name
        self.last_name  = last_name
        self.email      = email
        self.gender     = gender
        self.location   = location
        self.biography  = biography
        self.profilePic = profilePic
        self.created_on = created_on

    def __repr__(self):
        return '<User %r>' % (self.username)