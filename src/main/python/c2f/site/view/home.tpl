{% extends "template/base-template-two-columns.tpl" %}

{% block title %}
	{{ super() }} - Home
{% endblock %}

{% block left_container %}

{% endblock %}

{% block content_container %}
	
		<a href="/login">Login</a></br>
		<a href="/user/register">Register</a>
	
{% endblock %}
