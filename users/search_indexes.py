import datetime
from haystack import indexes
from .models import CustomUser

class CustomUserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    username = indexes.CharField(model_attr='username')
    email = indexes.CharField(model_attr='email')
    role = indexes.CharField(model_attr='role')

    def get_model(self):
        return CustomUser

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class OrderIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user__username')
    status = indexes.CharField(model_attr='status')
    created_at = indexes.DateTimeField(model_attr='created_at')
    updated_at = indexes.DateTimeField(model_attr='updated_at')

    def get_model(self):
        return Order

    def index_queryset(self, using=None):
        return self.get_model().objects.all()