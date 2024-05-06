from django.shortcuts import render

# Create your views here.


def lobby_screen_view(request):
    return render(request, "chatbox/lobby.html")



def room_screen_view(request):
    return render(request, 'chatbox/room.html')