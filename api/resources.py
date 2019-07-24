from api.models import *
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization


class SmsResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Sms.objects.all()
        resource_name = 'sms'
        authorization = Authorization()
        allowed_methods = ['get', 'post']


class RecommendationResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Recommendation.objects.all()
        resource_name = 'recommendation'
        authorization = Authorization()
        allowed_methods = ['get', 'post']


class UserRecommendationResource(ModelResource):
    class Meta:
        limit = 0
        queryset = UserRecommendation.objects.all()
        resource_name = 'user_recommendation'
        authorization = Authorization()
        allowed_methods = ['get', 'post']


class UserInterestResource(ModelResource):
    class Meta:
        limit = 0
        queryset = UserInterest.objects.all()
        resource_name = 'user_interest'
        authorization = Authorization()
        allowed_methods = ['get', 'post']
