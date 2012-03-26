
Register

<form action="/user/register" method="POST">
	
<div>{{ form.email.label }}: {{ form.email(class="css_class") }}</div>
    {% if form.email.errors %}
        <ul class="errors">{% for error in form.email.errors %}<li>{{ error }}</li>{% endfor %}</ul>
    {% endif %}
    
    <div>{{ form.name.label }}: {{ form.name() }}</div>
    {% if form.name.errors %}
        <ul class="errors">{% for error in form.name.errors %}<li>{{ error }}</li>{% endfor %}</ul>
    {% endif %}	


    <div>{{ form.password.label }}: {{ form.password() }}</div>
    {% if form.password.errors %}
        <ul class="errors">{% for error in form.password.errors %}<li>{{ error }}</li>{% endfor %}</ul>
    {% endif %}	
	
	<input type="submit" value="Salvar" />
	      
</from>