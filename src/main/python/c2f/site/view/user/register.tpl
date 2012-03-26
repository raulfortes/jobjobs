
Register

{% if error %}
<div class="row" style="color: red">
	<label>{{ error }}</label>
</div>
{% endif %}

<form action="/user/register" method="POST">

	e-mail: <input type="text" name="email" /></br>
	Nome: <input type="text" name="name" /></br>
	Senha: <input type="password" name="password" /></br>
	      <input type="submit" value="Salvar" />
	      
</from>