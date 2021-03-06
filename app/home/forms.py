# app/home/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField,RadioField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Event, Role

class TaskForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    associatedevent = StringField('Event Name', validators=[DataRequired()])
    eventdesc = StringField('Event Description', validators=[DataRequired()])
    taskname = StringField('Name of Task', validators=[DataRequired()])
    taskdescription = StringField('Description', validators=[DataRequired()])
    # taskowner= IntegerField('Associated Event', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SCSCommentForm(FlaskForm):
    """
    Form for admin to add or edit an event
    """
    scscomment = StringField('SCS Comments')
    appapproval = RadioField('Approval', choices=[('True','Accept'),('False','Reject')])
    submit = SubmitField('Submit')

class SendEmailForm(FlaskForm):
    """
    Form for admin to add or edit an event
    """
    scssendemail = StringField('Email Subject')
    emailrecepient = StringField('Email Recepients')
    submit = SubmitField('Submit')

class FMCommentForm(FlaskForm):
    """
    Form for admin to add or edit an event
    """
    fmcomment = StringField('SCS Comments')
    submit = SubmitField('Submit')

class AMCommentForm(FlaskForm):
    """
    Form for admin to add or edit an event
    """
    amcomment = StringField('SCS Comments')
    submit = SubmitField('Submit')

class PMCommentForm(FlaskForm):
    """
    Form for admin to add or edit an event
    """
    pmcomment = StringField('SCS Comments')
    submit = SubmitField('Submit')

class SBCommentForm(FlaskForm):
    """
    Form for admin to add or edit an event
    """
    sbcomment = StringField('SCS Comments')
    submit = SubmitField('Submit')
