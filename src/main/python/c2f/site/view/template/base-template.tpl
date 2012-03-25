<!DOCTYPE html>
<html>
	<head>
		    <meta http-equiv="Pragma" content="no-cache" />
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
			<title>{% block title %}jobjobs.com.br{% endblock%}</title>
	</head>
	<body>
		<div class="wrapper-main">
			{% include "template/header.tpl" %}
			<div class="wrapper-content">
				{% block wrapper_content %}
				{% endblock %}
			</div>
			{% include "template/footer.tpl" %}
		</div>
		
	</body>
</html>