from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message
from .serializers import MessageListSerializer
from .serializers import MessageInputSerializer
from django.shortcuts import render


def index(request):
    messages = Message.objects.order_by('id')[:30]
    return render(request, 'main/index.html', {'messages': messages})

class MessageView(APIView):
    serializer_class = MessageListSerializer

    def get_queryset(self):
        messages = Message.objects.all()
        return messages

    def get(self, request):

        messages = self.get_queryset()
        serializer = MessageListSerializer(messages, many=True)

        return Response(serializer.data)

    def post(self, request, vemac_id):
        message_data = request.data

        new_message = Message.objects.create(date=message_data["date"], vemac_id=vemac_id,
                                             time=message_data["time"], lat=message_data["lat"],
                                             lon=message_data["lon"], speed=message_data["speed"],
                                             course=message_data["course"], sats=message_data["sats"],
                                             danger=message_data["danger"], overlake=message_data["overlake"])

        new_message.save()

        serializer = MessageListSerializer(new_message)

        return Response(serializer.data)

    # def get(self, request):
    #     numbers = Message.objects.all()
    #     serializer = MessageListSerializer(numbers, many=True)
    #     return Response(serializer.data)


class MessageInput(APIView):
    '''Изменение числа'''

    def post(self, request):
        coordinate_api = MessageInputSerializer(data=request.data)
        if coordinate_api.is_valid():
            print('we')
            coordinate_api.save()
            return Response(200)
        else:
            return Response({'error': "Ошибка"})
