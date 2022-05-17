from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, TextAreaField,SubmitField,ValidationError
from wtforms.validators import DataRequired, Required,Email
from flask_login import current_user
from ..models import User

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[Required()])
    post = TextAreaField("Type Away", validators=[Required()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[Required()])
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField("Bio")
#     email = StringField("Email")
#     submit = SubmitField("Update")

class UpdateProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(),Email()])
    bio = TextAreaField('Write a brief bio about you.',validators = [DataRequired()])
    profile_picture = FileField('profile picture', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("The Email has already been taken!")
    
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username has already been taken")