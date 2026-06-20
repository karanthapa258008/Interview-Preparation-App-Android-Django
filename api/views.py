import json
import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


from .models import (
    Question,
    InterviewQuestion,
    ApptitudeQuestion,
    Users
)

otp_store = {}


def getJavaQuestions(request):
    data = list(Question.objects.filter(category="Java").values())
    return JsonResponse(data, safe=False)


def getPythonQuestions(request):
    data = list(Question.objects.filter(category="Python").values())
    return JsonResponse(data, safe=False)


def getJsQuestions(request):
    data = list(Question.objects.filter(category="JS").values())
    return JsonResponse(data, safe=False)

def getcQuestions(request):
    data = list(Question.objects.filter(category="C++").values())
    return JsonResponse(data, safe=False)

def getcssQuestions(request):
    data = list(Question.objects.filter(category="CSS").values())
    return JsonResponse(data, safe=False)

def getsqlQuestions(request):
    data = list(Question.objects.filter(category="SQL").values())
    return JsonResponse(data, safe=False)

def gethtmlQuestions(request):
    data = list(Question.objects.filter(category="HTML").values())
    return JsonResponse(data, safe=False)



def getJavaInterview(request):
    data = list(
        InterviewQuestion.objects.filter(category="Java")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)


def getPythonInterview(request):
    data = list(
        InterviewQuestion.objects.filter(category="Python")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)


def getJsInterview(request):
    data = list(
        InterviewQuestion.objects.filter(category="JS")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)


def getcInterview(request):
    data = list(
        InterviewQuestion.objects.filter(category="c++")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)

def gethtmlInterview(request):
    data = list(
        InterviewQuestion.objects.filter(category="html")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)


def getsqlInterview(request):
    data = list(
        InterviewQuestion.objects.filter(category="sql")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)

def getcssInterview(request):
    data = list(
        InterviewQuestion.objects.filter(category="css")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)


def getJavaApptitude(request):
    data = list(
        ApptitudeQuestion.objects.filter(category="Java")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)


def getPythonApptitude(request):
    data = list(
        ApptitudeQuestion.objects.filter(category="Python")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)


def getJsApptitude(request):
    data = list(
        ApptitudeQuestion.objects.filter(category="JS")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)



def getcpApptitude(request):
    data = list(
        ApptitudeQuestion.objects.filter(category="c++")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)



def getsqlApptitude(request):
    data = list(
        ApptitudeQuestion.objects.filter(category="Sql")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)


def gethtmlApptitude(request):
    data = list(
        ApptitudeQuestion.objects.filter(category="html")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)

def getcssApptitude(request):
    data = list(
        ApptitudeQuestion.objects.filter(category="css")
        .values("question", "answer")
    )
    return JsonResponse(data, safe=False)


@csrf_exempt
def send_otp(request):
    print("SEND OTP HIT")

    if request.method != "POST":
        return JsonResponse({"status": "error", "message": "Only POST allowed"})

    try:
        data = json.loads(request.body.decode("utf-8"))
        print("DATA:", data)

        email = data.get("email")

        if not email:
            return JsonResponse({"status": "error", "message": "Email missing"})

        otp = random.randint(1000, 9999)
        otp_store[email] = otp

        send_mail(
            "OTP",
            f"Your OTP is {otp}",
            "yourgmail@gmail.com",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )

        return JsonResponse({"status": "success", "message": "OTP sent"})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})


# ---------------- VERIFY OTP ----------------
@csrf_exempt
def verify_otp(request):

    if request.method != "POST":
        return JsonResponse({
            "status": "error",
            "message": "Only POST allowed"
        })

    try:

        data = json.loads(request.body.decode("utf-8"))

        email = data.get("email")
        otp = int(data.get("otp"))
        username = data.get("username")
        password = data.get("password")

        print("========== VERIFY OTP ==========")
        print("EMAIL:", email)
        print("OTP:", otp)
        print("USERNAME:", username)
        print("OTP STORE:", otp_store)

        if email in otp_store and otp_store[email] == otp:

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            print("USER CREATED:", username)

            del otp_store[email]

            return JsonResponse({
                "status": "success",
                "message": "User created"
            })

        return JsonResponse({
            "status": "failed",
            "message": "Invalid OTP"
        })

    except Exception as e:

        print("VERIFY OTP ERROR:", str(e))

        return JsonResponse({
            "status": "error",
            "message": str(e)
        })

# ---------------- LOGIN ----------------


@csrf_exempt
def login_user(request):

    print("========== LOGIN HIT ==========")

    try:
        data = json.loads(request.body.decode("utf-8"))

        email = data.get("username")
        password = data.get("password")

        print("EMAIL:", email)
        print("PASSWORD:", password)

        user_obj = User.objects.filter(email=email).first()

        if user_obj:

            user = authenticate(
                username=user_obj.username,
                password=password
            )

            print("USER OBJECT:", user)

            if user is not None:
                return JsonResponse({
                    "status": "success",
                    "message": "Login successful"
                })

        return JsonResponse({
            "status": "failed",
            "message": "Invalid credentials"
        })

    except Exception as e:

        print("LOGIN ERROR:", str(e))

        return JsonResponse({
            "status": "error",
            "message": str(e)
        })