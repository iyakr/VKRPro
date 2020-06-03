from django.urls import path,include

from Project.views import *
#
urlpatterns = [
    path('requests/', ZayavkaView.as_view()),                   #Заявки
    path('userrequests/', UserRequest.as_view()),               #Заявки пользователя
    path('requests/<int:pk>/', ZayavkaDetail.as_view()),        #Вывод заявки по id
        path('competitions/', CompetitionView.as_view()),           #Соренования
    path('competition/<int:pk>/', CompetitionDetail.as_view()),# Соревнование
    path('members/<int:pk>/', CompMemberView.as_view()),        #Заявки на участие в конкретном соревновании(pk- id соревнования)
    path('sportsmans/<int:pk>/', ZayavkiPoDisc.as_view()),      #Заявки по дисциплинам
    path('disciplines/',DisciplineView.as_view()),
    path('disciplines/<int:pk>/',DiscDetail.as_view()),
    path('rank/',RankView.as_view()),
    path('sex/',SexView.as_view()),
    path('region/',RegionView.as_view()),
    path('malerequests/',ZayavkaMView.as_view()),
    path('womenrequests/',ZayavkaWView.as_view()),
    path('membersM/<int:pk>/', CompMemberViewM.as_view()),
    path('membersW/<int:pk>/', CompMemberViewW.as_view()),
    # path('zabeg/', ZabegView.as_view()),
    path('protadd/<int:pk>/<int:pk2>/<int:pk3>/', Protadd.as_view()),
    # path('stroki/', StrokaView.as_view()),


    path('dorozhka/', DorozhkaVew.as_view()),


    # path('protocols/', ProtocolView.as_view()),

            ]
