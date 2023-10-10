from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from .models import Notes
from .serializers import NotesSerializer

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import permissions

from rest_framework.generics import ListAPIView
from rest_framework import filters


# Generic view for getting notes --> Easy to use filters and order on generic views
class GetNotesApiView(ListAPIView):
    serializer_class=NotesSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['completed', 'priority', 'category']
    ordering_fields = ['created_at', 'priority', 'due_date']
    ordering = ['-created_at']

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user.id)

# Create note View
class NotesCreateApiView(APIView):
    # add authentication and permissions middleware
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    # Create a new note for logged in user
    def post(self, request, *args, **kwargs):

        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "due_date": request.data.get("due_date"),
            "category": request.data.get("category"),
            "user": request.user.id,
        }

        # short cut below --> makes tests failed for now
        # request.data['user'] = request.user.id

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
    

from django.http import FileResponse

from .create_pdf import create_pdf
from .send_email import send
from django.http import HttpResponse

class NotesPdfApiView(APIView):
    # add authentication and permissions middleware
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = self.request.user.id
        buffer = create_pdf(Notes, user)

        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename='Notes.pdf')
    

class PublishPdfApiView(APIView):
    # add authentication and permissions middleware
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        user = self.request.user.id
        buffer = create_pdf(Notes, user) 
 
        email = send('PDF Report', 'Please find the attached PDF report.', [self.request.user.email])
        
        buffer.seek(0)
        email.attach('Notes.pdf', buffer.read(), 'application/pdf')
        email.send()

        buffer.close()

        return HttpResponse('PDF sent by email successfully')




