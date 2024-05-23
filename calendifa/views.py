from rest_framework.views import APIView
from rest_framework.response import Response
from persiantools.jdatetime import JalaliDateTime
from persiantools import digits
from rest_framework import status


class Jalali:
    def __init__(self) -> None:
        self.current_time = JalaliDateTime.now()
        self.pairs = {}


class JalaliNowContent(Jalali):
    def __init__(self) -> None:
        super().__init__()
        self.make_pairs()

    def make_pairs(self):
        self.pairs["now"] = self.current_time.strftime("%c")
        self.pairs["day"] = self.current_time.day
        self.pairs["date"] = self.current_time.date()
        self.pairs["time"] = self.current_time.time()
        self.pairs["month"] = self.current_time.month
        self.pairs["year"] = self.current_time.year
        self.pairs["timestamp"] = self.current_time.timestamp()
        self.pairs["hour"] = self.current_time.hour
        self.pairs["minute"] = self.current_time.minute
        self.pairs["second"] = self.current_time.second
        self.pairs["week_of_year"] = self.current_time.week_of_year()
        self.pairs["day_of_week"] = self.current_time.weekday()
        self.pairs["utc"] = self.current_time.utcnow().to_gregorian()

    def get_pairs(self):
        return self.pairs


def digit_to_persian(en_obj: dict):
    fa_obj = {}
    for key, value in en_obj.items():
        fa_obj[key] = digits.en_to_fa(value)

    return fa_obj


class StatusView(APIView):
    def get(self, request, format=None):
        formatted_response = {
            "status_code": status.HTTP_200_OK,
            "message": "Hi from calendifa",
        }
        return Response(formatted_response, status=status.HTTP_200_OK)


class NowView(APIView):
    def get(self, request, format=None):
        jalali_responsse = JalaliNowContent()
        formatted_response = jalali_responsse.get_pairs()
        formatted_response["status_code"] = status.HTTP_200_OK
        return Response(formatted_response, status=status.HTTP_200_OK)


class NowPersianDigitView(APIView):
    def get(self, request, format=None):
        jalali_responsse = JalaliNowContent()
        formatted_response = jalali_responsse.get_pairs()
        formatted_response = digit_to_persian(formatted_response)
        formatted_response["status_code"] = status.HTTP_200_OK
        return Response(formatted_response, status=status.HTTP_200_OK)
