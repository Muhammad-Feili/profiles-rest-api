from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
	""" Test API View """

	def get(self, response, format=None):
		""" Returns a list of APIView features """
		an_apiview=[
			'Uses HTTP methods as function (get, post, patch, put, delete)',
			'Is similar to a traditional Django view',
			'Gives you the most control over you application logic',
			'Is mapped manually to URLs'
			]
		this="I am mohammad feili and are you okay!?"
		return Response({"message": 'hello', 'an_apiview': an_apiview, 'this':this})
