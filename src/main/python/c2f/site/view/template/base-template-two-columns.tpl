{% extends "template/base-template.tpl" %}

{% block wrapper_content %}
	<div class="left-container" style="width:200px; float:left">
		{% block left_container %}
		{% endblock %}
	</div>
	
	<div class="content-container">
		{% block content_container %}
		{% endblock %}
	</div>
{% endblock %}