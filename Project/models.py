from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now
from django.contrib.auth.models import User,Group
import datetime

class Sex(models.Model):
    name = models.CharField(max_length=10,verbose_name="пол")
    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"

class NumUp(models.Model):
    number = models.CharField(max_length=1,verbose_name="дорожка")
    class Meta:
        verbose_name = "дорожка"
        verbose_name_plural = "дорожка"


class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование региона')
    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

class Rank(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование разряда')
    class Meta:
        verbose_name = "Разряд"
        verbose_name_plural = "Разряды"


class Round(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование раунда')

    class Meta:
        verbose_name = "Раунд"
        verbose_name_plural = "Раунды"


class Discipline(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование дисциплины')

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class Competition(models.Model):
    datestart = models.DateField(default=now(), verbose_name='Дата начала')
    info = models.CharField(max_length=300, verbose_name='Информация о соревновании',blank=True)
    dateoff = models.DateField(default=now() verbose_name='Дата конца')
    name = models.CharField(max_length=50, verbose_name='наименование соревнований')
    place = models.ForeignKey(Region, verbose_name="место проведения", on_delete=models.CASCADE, blank=True, related_name="RegionAsPlace")
    disciplines = models.ManyToManyField(Discipline, related_name='competitions', blank=True, null=True)
    created = models.ForeignKey(User, verbose_name="автор", on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"


class Zayavka(models.Model):
    FIO = models.CharField(max_length=50, verbose_name='ФИО спортсмена')
    yearbirth = models.CharField( null=True,blank=True, max_length=4)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, verbose_name="пол", null=True,related_name="sexAsSex")
    discipline = models.ForeignKey(Discipline,related_name="disciplineAsDiscipline", on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, verbose_name="разряд", on_delete=models.CASCADE)
    FIOCoach = models.CharField(max_length=50, verbose_name='ФИО тренера',blank=True)
    region = models.ForeignKey(Region, verbose_name="регион", on_delete=models.CASCADE, blank=True,related_name="RegionAsRegion")
    competition = models.ForeignKey(Competition, verbose_name="соревнование", on_delete=models.CASCADE,related_name="competitionAsCompetition")
    number = models.IntegerField(verbose_name="номер")
    resultS1 = models.CharField(max_length=20, verbose_name='результат забег', blank=True)
    resultS2 = models.CharField(max_length=20, verbose_name='результат полуф', blank=True)
    resultS3 = models.CharField(max_length=20, verbose_name='результат финал', blank=True)
    dorozhka = models.ForeignKey(NumUp,  verbose_name="дорожка", on_delete=models.CASCADE, blank=True, null=True)
    created = models.ForeignKey(User,verbose_name="автор",on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


# class Stroka(models.Model):
#     sportsman = models.OneToOneField(
#         Zayavka,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     resultS1 = models.CharField(max_length=20, verbose_name='результат забег', blank=True)
#     resultS2 = models.CharField(max_length=20, verbose_name='результат полуф', blank=True)
#     resultS3 = models.CharField(max_length=20, verbose_name='результат финал', blank=True)
#     dorozhka = models.ForeignKey(NumUp, verbose_name="дорожка", on_delete=models.CASCADE, blank=True, null=True)

# class Zabeg(models.Model):
#
#     zabeg = models.ManyToManyField(Zayavka, verbose_name="Забег")
#     number = models.IntegerField(verbose_name="номер забега")
#
#     class Meta:
#         verbose_name = "Забег"
#         verbose_name_plural = "Забег"
#
#
# class RoundZ(models.Model):
#     number = models.IntegerField(verbose_name="номер ")
#     class Meta:
#         verbose_name = "кросс"
#         verbose_name_plural = "кросс"
#
#
# class Protocol(models.Model):
#
#     disciplineP = models.ForeignKey(Discipline, verbose_name="дисциплина", on_delete=models.CASCADE)
#     agegroup = models.CharField( null=True,blank=True, max_length=4)
#     roundP = models.ForeignKey(Round, verbose_name="раунд", on_delete=models.CASCADE)
#     sexP = models.ForeignKey(Sex,on_delete=models.CASCADE)
#     # stroki = models.ManyToManyField(StrokaProt,on_delete=models.CASCADE)
#     zabeg = models.ManyToManyField(Zabeg, verbose_name="забег")
#     class Meta:
#         verbose_name = "Протокол"
#         verbose_name_plural = "Протоколы"

