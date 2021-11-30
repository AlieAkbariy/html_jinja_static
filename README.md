# html_jinja_static
This code can change html link and image to jinja static form and i think it's useful for Django developer

for example: 
this code
```bash
<link rel="shortcut icon" type="image/x-icon" href="assets/images/favicon.png">
```

convert to
```bash
<link rel="shortcut icon" type="image/x-icon" href="{% static'images/favicon.png' %}">
```
