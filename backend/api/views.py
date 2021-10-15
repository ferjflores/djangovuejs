from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

persons = [
    {
        'id': 1,
        'name': 'Pepe Perez',
        'position': 'Project Manager'
    },
    {
        'id': 2,
        'name': 'Pedro Picapiedra',
        'position': 'QA Engineer'
    },
    {
        'id': 3,
        'name': 'Pablo Marmol',
        'position': 'Jr Developer'
    },
    {
        'id': 4,
        'name': 'Bety Marmol',
        'position': 'Sr Developer'
    },
]


class PersonList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(persons)


class PersonDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        for person in persons:
            if person['id'] == id:
                return Response(person)
