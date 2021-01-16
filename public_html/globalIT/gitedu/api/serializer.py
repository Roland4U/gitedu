from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import *

class FacultetSerializer(ModelSerializer):
    '''Facultet'''

    trainings = SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:

        model = facultet
        fields = ('__all__' )


class TrainingSerializer(ModelSerializer):
    '''Training'''

    class Meta:

        model = training
        fields = ('__all__') 


class ServiceSerializer(ModelSerializer):
    '''Service'''

    # trainings = SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:

        model = service
        fields = ('__all__') 

