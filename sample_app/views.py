from rest_framework import views
from rest_framework import response
from rest_framework import status


class SimpleView(views.APIView):
    def get(self, *args, **kwargs):
        return response.Response(
            {'message': 'I am om26er, I have been writing RESTful APIs for 2 years and I am '
                        'a Python developer for 4 years.'},
            status=status.HTTP_200_OK
        )
