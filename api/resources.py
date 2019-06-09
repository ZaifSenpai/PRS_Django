from api.models import Sms
from api.models import Recommendation
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

class SmsResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Sms.objects.all()
        resource_name = 'sms'
        authorization = Authorization()

class RecommendationResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Recommendation.objects.all()
        resource_name = 'recommendation'
        authorization = Authorization()
