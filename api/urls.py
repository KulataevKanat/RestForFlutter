from django.conf.urls import url
from django.urls import path, include
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.routers import DefaultRouter

from api.authentication import SafeJWTAuthentication
from api.permissions.permission import ROLE_ADMIN
from api.views import UserViews, GroupViews, CategoryViews, AdvertViews, ImageViews

router = DefaultRouter()

# USERS ROUTER
router.register('user', authentication_classes([SafeJWTAuthentication])(
    permission_classes([AllowAny])(UserViews.UserAuthorizationView)), basename='user'),

urlpatterns = [
    # CATEGORIES
    path("category/create_category/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.CreateCategoryView)).as_view()),
    path("category/create_subcategory/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.CreateSubCategoryView)).as_view()),
    path("category/delete_category_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.DeleteCategoryByIdView)).as_view()),
    path("category/update_category_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.UpdateCategoryByIdView)).as_view()),
    path("category/find_all_categories/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.GetCategoryView)).as_view()),
    path("category/find_category_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.FindCategoryByIdView)).as_view()),

    # IMAGE
    path("image/create_image/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ImageViews.CreateImageView)).as_view()),
    path("image/delete_image_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ImageViews.DeleteImageByIdView)).as_view()),
    path("image/update_image_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ImageViews.UpdateImageByIdView)).as_view()),
    path("image/find_all_images/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ImageViews.GetImageView)).as_view()),
    path("image/find_image_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ImageViews.FindImageByIdView)).as_view()),

    # ADVERT
    path("advert/create_advert/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AdvertViews.CreateAdvertView)).as_view()),
    path("advert/delete_advert_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AdvertViews.DeleteAdvertByIdView)).as_view()),
    path("advert/update_advert_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AdvertViews.UpdateAdvertByIdView)).as_view()),
    path("advert/find_all_adverts/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AdvertViews.GetAdvertView)).as_view()),
    path("advert/find_advert_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AdvertViews.FindCategoryByIdView)).as_view()),

    # USERS
    url('', include(router.urls)),
    path("user/registration/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.UserRegistrationView)).as_view()),
    path("user/delete_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.DeleteAllUserView)).as_view()),
    path("user/find_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.GetUserView)).as_view()),
    path("user/find_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.FindUserByIdView)).as_view()),

    # GROUPS
    path("group/create_group/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.CreateGroupView)).as_view()),
    path("group/delete_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.DeleteGroupByIdView)).as_view()),
    path("group/update_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.UpdateGroupByIdView)).as_view()),
    path("group/find_all_groups/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.GetGroupView)).as_view()),
    path("group/find_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.FindGroupByIdView)).as_view()),
]
