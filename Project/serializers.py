from rest_framework import serializers
from Project.models import *
from django.contrib.auth.models import User

# class RoundZSerializers(serializers.ModelSerializer):
#     '''Дисциплина'''
#     class Meta:
#         model = RoundZ
#         fields = ['number']

class NumUpSerializers(serializers.ModelSerializer):
    '''Дисциплина'''
    class Meta:
        model = NumUp
        fields = ['number']


class DisciplineSerializers(serializers.ModelSerializer):
    '''Дисциплина'''
    class Meta:
        model = Discipline
        fields = ['name','id']

class SexSerializers(serializers.ModelSerializer):
    '''Дисциплина'''
    class Meta:
        model = Sex
        fields = ['name','id']

class RankSerializers(serializers.ModelSerializer):
    '''Разряд'''
    class Meta:
        model = Rank
        fields = ['name','id']

class RoundSerializers(serializers.ModelSerializer):
    '''Разряд'''
    class Meta:
        model = Round
        fields = ['name','id']


class DisciplineSerializers(serializers.ModelSerializer):
    '''Регион'''
    class Meta:
        model = Discipline
        fields = ['name','id']

class RegionSerializers(serializers.ModelSerializer):
    '''Регион'''
    class Meta:
        model = Region
        fields = ['name','id']


class UserSerializer(serializers.ModelSerializer):
    '''Пользователь'''
    class Meta:
        model = User
        fields = ['id', 'username']


class CompetitionSerializers(serializers.ModelSerializer):
    '''Соревнование'''
    place = RegionSerializers(read_only=True)
    place_id = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(), write_only=True)
    created = UserSerializer(read_only=True)

    class Meta:
            model = Competition
            fields = ['dateoff','datestart', 'name','info',"place","place_id","id","created"]

    def create(self, validated_data):
        place = validated_data.pop('place_id')
        competition = Competition.objects.create(place=place,  **validated_data)
        return competition

    def update(self, instance, validated_data):
        instance.dateoff = validated_data.get('dateoff', instance.dateoff)
        instance.datestart = validated_data.get('datestart', instance.datestart)
        instance.name = validated_data.get('name', instance.name)
        instance.place_id = validated_data.get('place_id', instance.place_id)
        instance.save()
        return instance



#
# class AddCompetitionSerializers(serializers.ModelSerializer):
#     '''Соревнование'''
#     place = RegionSerializers()
#     class Meta:
#             model = Competition
#             fields = ['dateoff','datestart', 'name','info',"place","id"]
#
#     def create(self, validated_data):
#         name = validated_data.pop('place')
#         place = Region.objects.get(name = name)[0]
#         comp = Competition.objects.create(place = place.name)
# #         return comp
class ZayavkaSerializers(serializers.ModelSerializer):
    '''Заявка(соревнование - id)'''
    competition = CompetitionSerializers(read_only=True)
    discipline = DisciplineSerializers()
    region = RegionSerializers(read_only=True)
    rank = RankSerializers()
    sex = SexSerializers()
    created= UserSerializer()
    class Meta:
        model = Zayavka
        fields = ['id','competition',"FIO","FIOCoach", "yearbirth","rank", "region", "sex", "number","discipline","created"]

class StrokaSerializers(serializers.ModelSerializer):
    '''Заявка(соревнование - id)'''
    competition = CompetitionSerializers(read_only=True)
    discipline = DisciplineSerializers()
    region = RegionSerializers(read_only=True)
    dorozhka = NumUpSerializers()
    rank =RankSerializers()
    class Meta:
        model = Zayavka
        fields = ['id','competition',"FIO", "yearbirth","rank", "region", "number","discipline","resultS1","resultS2","resultS3","dorozhka",]

# class StrokaSerializers1(serializers.ModelSerializer):
#     sportsman = StrokaSerializers(read_only=True)
#     class Meta:
#         model = Stroka
#         fields = ["sportsman", "resultS1",
#                   "resultS2", "resultS3", "dorozhka", ]


# class AddZayavkaSerializers1(serializers.ModelSerializer):
#     results3=StrokaSerializers()
#     class Meta:
#             model = Zayavka
#             fields = ["results3",]

# class CompetitionSerializers(serializers.ModelSerializer):
#     '''Соревнование'''
#     place = RegionSerializers(read_only=True)
#     place_id = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(), write_only=True)
#     class Meta:
#             model = Competition
#             fields = ['dateoff','datestart', 'name','info',"place","place_id","id"]
#
#     def create(self, validated_data):
#         place = validated_data.pop('place_id')
#         competition = Competition.objects.create(place=place,  **validated_data)
# #         return competition
#
class AddZayavkaSerializers(serializers.ModelSerializer):
    region = RegionSerializers(read_only=True)
    region_id = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(), write_only=True)
    competition = CompetitionSerializers(read_only=True)
    competition_id = serializers.PrimaryKeyRelatedField(queryset=Competition.objects.all(), write_only=True)
    rank = RankSerializers(read_only=True)
    rank_id = serializers.PrimaryKeyRelatedField(queryset=Rank.objects.all(), write_only=True)
    sex = SexSerializers(read_only=True)
    sex_id = serializers.PrimaryKeyRelatedField(queryset=Sex.objects.all(), write_only=True)
    discipline = DisciplineSerializers(read_only=True)
    discipline_id = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects.all(), write_only=True)
    # created= UserSerializer()
    # created_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    # discipline_id = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects.all(), write_only=True)
    class Meta:
            model = Zayavka
            fields = ["competition",'competition_id',"region",'region_id',"rank","sex","FIO", "yearbirth",  "rank_id","sex_id", "number","discipline","FIOCoach","discipline_id",]
            # extra_kwargs = {'discipline': {'required': False}}

    def create(self, validated_data):
        discipline = validated_data.pop('discipline_id')
        region = validated_data.pop('region_id')
        competition = validated_data.pop('competition_id')
        sex = validated_data.pop('sex_id')
        rank = validated_data.pop('rank_id')
        # created = validated_data.pop('created_id')
        zayavka = Zayavka.objects.create(region=region, competition=competition, sex=sex, rank=rank,discipline=discipline, **validated_data)
        return zayavka

#
class CompMemberSerializers(serializers.ModelSerializer):
    '''Участники соревнований'''
    discipline = DisciplineSerializers()
    competition = CompetitionSerializers(read_only=True)
    region = RegionSerializers()
    class Meta:
        model = Zayavka
        fields = ["FIO", "yearbirth", "region", "sex", "number","discipline","competition","id"]


class DiscMemberSerializers(serializers.ModelSerializer):
    '''Участники соревнований'''
    sex = serializers.SlugRelatedField(
        many=True,
        slug_field='sex',
        queryset=Zayavka.objects.all(),
    )
    class Meta:
        model = Zayavka
        fields = ["resultS1","resultS2","resultS3","dorozhka","FIO", "yearbirth", "Region", "sex", "number","discipline"]

#
class ZayavkaFiltr(serializers.ModelSerializer):
    '''Заявка(соревнование - id)'''

    class Meta:
        model = Zayavka
        fields = ["FIO", "yearbirth", "region", "sex", "number",]


# class ZabegSerializers(serializers.ModelSerializer):
#     zabeg = ZayavkaSerializers(many=True)
#     class Meta:
#             model = Zabeg
#             fields = ['number',"zabeg","id" ]

# class ProtocolSerializers(serializers.ModelSerializer):
#     '''Протокол'''
#     disciplineP = DisciplineSerializers()
#     zabeg = ZabegSerializers(many=True)
#     roundP=RoundSerializers()
#     sexP = SexSerializers()
#
#     class Meta:
#         model = Protocol
#         fields = ["disciplineP", "agegroup", "roundP", "sexP","zabeg",]







# class AddZayavkaSerializers(serializers.ModelSerializer):
#     rank = RankSerializers(read_only=True)
#     competition = CompetitionSerializers(read_only=True)
#     discipline = DisciplineSerializers(many=True)
#     Region = RegionSerializers(read_only=True)
#     sex = serializers.SlugRelatedField(
#         many=True,
#         slug_field='sex',
#         queryset=Zayavka.objects.all(),
#     )
#     class Meta:
#         model = Zayavka
#         fields = ['id','competition',"FIO", "yearbirth",  "sex", "number","discipline","rank","Region"]