from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from NCPWD.apps.user_profile.models import UserDisability, Disability


class StatisticsViews(APIView):
    def get(self, request):
        resp = {}
        disabilities = Disability.objects.all()
        for i in disabilities:
            resp[i.detail] = UserDisability.objects.filter(disability=i).count()

        return Response(resp)
