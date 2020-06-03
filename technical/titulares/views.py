from rest_framework import viewsets, permissions, request, status, views
from rest_framework.response import Response

from .models import Fisica, Juridica
from .serializers import FisicaSerializer, JuridicaSerializer


class TitularView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        q1 = Fisica.objects.all()
        q2 = Juridica.objects.all()

        # evaluate querysets and get a serializeble output in a list
        serializer1 = FisicaSerializer(q1, many=True, context={'request': request}).data
        serializer2 = JuridicaSerializer(q2, many=True, context={'request': request}).data
        # concatenate two lists of dicts and sort it by 'cuit' key
        titulares_list = sorted(serializer1 + serializer2, key=lambda x: x.get('id'))
        return Response(data=titulares_list, status=status.HTTP_200_OK)


class FisicaViewSet(viewsets.ModelViewSet):
    queryset = Fisica.objects.all().order_by('id')
    serializer_class = FisicaSerializer
    permission_classes = [permissions.IsAuthenticated]


class JuridicaViewSet(viewsets.ModelViewSet):
    queryset = Juridica.objects.all().order_by('id')
    serializer_class = JuridicaSerializer
    permission_classes = [permissions.IsAuthenticated]
