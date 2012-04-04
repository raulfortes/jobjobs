## -*- coding: utf-8 -*-

import logging
from c2f.site import app, template, request, redirect
from c2f.site.model.user import User as UserModel
from c2f.site.form.user import UserForm

logger = logging.getLogger(__name__)


@app.route("/user/register", method=['GET', 'POST'])
def register():
    form = UserForm(request.POST)
    if request.method == 'POST' and form.validate():
        user = UserModel()
        user.name = form.name.data
        user.email = form.email.data
        user.save()
        redirect('register')
    return template("user/register.html", form=form)
