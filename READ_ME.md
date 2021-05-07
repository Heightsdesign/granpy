
Introduction

	Granpy App est une application web qui vous permet de communiquer avec un papy robot.
	Posez-lui une question via son chatbox concernant une localisation ou un monument et
	il vous trouvera une anecdote sur les environs. Il peut parfois radotter (dur dur d'être un papy),
	n'hésitez pas à reformuler votre question si c'est le cas ... :) 


Spécifications Fonctionnelles

	L'application Granpy App est développée en Python avec l'aide du framework Flask pour la partie back-end.
	Pour le front-end nous utilisons HTML, CSS, Bootstrap ainsi que Javascript et Jquery.
	Les différents modules nécessaires (pour Python) ainsi que leurs versions sont présentes dans le fichier requirements.txt.

	Pour les installer : https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1 .

	Bootstrap, Javascript et Jquery sont éxecutés via des CDN et sont présents à la fin du fichier index.html.


Spécifications Techniques

	L'application Granpy App utilise les APIs Google Geocoding API et Maps Javascript API.

	Geocoding API : https://console.cloud.google.com/marketplace/product/google/geocoding-backend.googleapis.com
	Maps Javascript API : https://console.cloud.google.com/marketplace/product/google/maps-backend.googleapis.com

	N'oubliez pas de générer votre propre clé API puis insérez-la dans les fichiers:
		
		- geocode.py : self.api_key = 'YOUR_API_KEY'
		- index.html : <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY">
		
	Des requêtes sont également faites via l'API wikipédia




