from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

class NewUserView(APIView):

    def post(self, request):
        data = request.data
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')

        # Validate the data (you can add more validation if needed)
        if not (first_name and last_name and email):
            return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        # Write to a txt file
        with open('users.txt', 'a') as file:
            file.write(json.dumps({
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }) + '\n')

        return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)
