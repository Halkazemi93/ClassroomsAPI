
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views as classes_views
from apiclass import views as api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', classes_views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', classes_views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', classes_views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', classes_views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', classes_views.classroom_delete, name='classroom-delete'),
    path('api/classrooms/', api_views.ClassroomList.as_view(), name="classroom-list"), 
    path('api/classrooms/<int:classroom_id>/detail/', api_views.ClassroomDetail.as_view(), name="classrooms-details"),
    path('api/classrooms/<int:classroom_id>/update/', api_views.ClassroomUpdate.as_view(), name="update-classroom"),
    path('api/classrooms/<int:classroom_id>/cancel/', api_views.ClassroomDelete.as_view(), name="delete-classroom"),
    path('api/classrooms/create/', api_views.ClassroomCreate.as_view(), name="create-classroom"),
    path('login/', TokenObtainPairView.as_view(), name="login"),
]



if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


