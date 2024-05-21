from rest_framework.views import APIView
from rest_framework.response import Response
from persiantools.jdatetime import JalaliDateTime
from rest_framework import status


class NowView(APIView):
    def get(self, request, format=None):

        current_time = JalaliDateTime.now()
        print(dir(current_time))
        formatted_response = {
            "status_code": status.HTTP_200_OK,
            "now": current_time.strftime("%c"),
            "day": current_time.day,
            "date": current_time.date(),
            "time": current_time.time(),
            "month": current_time.month,
            "year": current_time.year,
            "timestamp": current_time.timestamp(),
            "hour": current_time.hour,
            "minute": current_time.minute,
            "second": current_time.second,
            "week_of_year": current_time.week_of_year(),
            "day_of_week": current_time.weekday(),
            "utc": current_time.utcnow().to_gregorian(),
        }
        return Response(formatted_response, status=status.HTTP_200_OK)
