from rest_framework.views import APIView
from rest_framework.response import Response
from NCPWD.permission import IsAdmin
from NCPWD.apps.user_profile.models import Profile


class StatisticsViews(APIView):
    permission_classes = (IsAdmin,)

    def get(self, request):
        resp = {}
        resp['Total users'] = Profile.objects.all().count()
        resp['Male'] = Profile.objects.filter(sex="MALE").count()
        resp['Female'] = Profile.objects.filter(sex="FEMALE").count()

        return Response(resp)
