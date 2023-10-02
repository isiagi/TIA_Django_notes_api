from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notes
from .serializers import NotesSerializer

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import permissions

class NotesListApiView(APIView):
    # add authentication and permissions middleware
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # Get all notes of logined user
    def get(self, request, *args, **kwargs):
        notes = Notes.objects.filter(user=request.user.id)
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create a new note for logged in user
    def post(self, request, *args, **kwargs):

        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "due_date": request.data.get("due_date"),
            "user": request.user.id,
        }
        serializer = NotesSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class NotesDetailApiView(APIView):
    # add authentication and permissions middleware
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # Helper function to get user object
    def get_object(self, note_id, user_id):
        try:
            return Notes.objects.get(id=note_id, user=user_id)
        except Notes.DoesNotExist:
            return None
        
            
    # Get by Id
    def get(self, request, note_id, *args, **kwargs):

        notes_instance = self.get_object(note_id, request.user.id)

        if not notes_instance:
            return Response({'message': "Object with note id doesnot exist"},
                                status=status.HTTP_400_BAD_REQUEST)
        
        serializer = NotesSerializer(notes_instance)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # update
    def patch(self, request, note_id, *args, **kwargs):

        notes_instance = self.get_object(note_id, request.user.id)

        if not notes_instance:
            return Response({'message': "Object with note id doesnot exist"},
                                status=status.HTTP_400_BAD_REQUEST,)
            
        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "due_date": request.data.get("due_date"),
            "user": request.user.id,
            }

        serializer = NotesSerializer(instance=notes_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    # delete
    def delete(self, request, note_id, *args, **kwargs):

        notes_instance = self.get_object(note_id, request.user.id)

        if not notes_instance:
            return Response({'message': "Object with note id doesnot exist"},
                                status=status.HTTP_400_BAD_REQUEST,)
            
        notes_instance.delete()

        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)



    




