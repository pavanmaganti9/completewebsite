from django.contrib.auth.models import User
import django_filters
from .models import FormData

class UserFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = FormData
		fields = ['name', 'email', 'address', ]