"""janten_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path


# from src.view.views import QuestionInformation, AnswerInformation, AggregateResults

try:
    import os
    import sys
    from django.contrib import admin
    from django.urls import path

    sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
except ImportError as e:
    sys.exit(str(e))
else:
    from backend.janten_master.src.view.QuestionInformationView import (
        QuestionInformationView,
    )
    from backend.janten_master.src.view.AnswerInformationView import (
        AnswerInformationView,
    )
    from backend.janten_master.src.view.AggregateResultsView import (
        AggregateResultsView,
    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "webapi/v1/question-information/",
        QuestionInformationView.as_view(),
        name="QuestionInformationView",
    ),
    path(
        "webapi/v1/answer-information/",
        AnswerInformationView.as_view(),
        name="AnswerInformationView",
    ),
    path(
        "webapi/v1/aggregate-results/",
        AggregateResultsView.as_view(),
        name="AggregateResultsView",
    ),
]
