from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import requests

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
        # with open('users.txt', 'a') as file:
        #     file.write(json.dumps({
        #         'firstName': first_name,
        #         'lastName': last_name,
        #         'email': email
        #     }) + '\n')

        # Send data to Klaviyo API
        klaviyo_url = "https://a.klaviyo.com/api/profiles/"
        klaviyo_payload = {
            "data": {
                "type": "profile",
                "attributes": {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "properties": {}
                }
            }
        }
        klaviyo_headers = {
            "accept": "application/json",
            "revision": "2023-08-15",
            "content-type": "application/json",
            "Authorization": "Klaviyo-API-Key pk_37284532fd854df3046bf5098d512fd0fc"
        }

        klaviyo_response = requests.post(klaviyo_url, json=klaviyo_payload, headers=klaviyo_headers)

        if klaviyo_response.status_code != 201:  # Assuming 201 is the success status code for Klaviyo
            return Response({"error": "Failed to send data to Klaviyo", "klaviyo_response": klaviyo_response.text}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Data saved and sent to Klaviyo successfully"}, status=status.HTTP_201_CREATED)
