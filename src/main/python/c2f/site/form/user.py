from wtforms import Form, BooleanField, TextField, validators


class UserForm(Form):
    name = TextField('Nome', [validators.Length(min=4, max=25)])
    password = TextField('Senha', [validators.Length(min=4, max=25)])

    email = TextField('Email', [
        validators.Length(min=6, message='Little short for an email address?'),
        validators.Email(message='That\'s not a valid email address.')
    ])
    #accept_rules = BooleanField('I accept the site rules', [validators.Required()])
