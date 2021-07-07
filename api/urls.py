from django.urls import path
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny

from api.authentication import SafeJWTAuthentication
from api.permissions.permission import ROLE_ADMIN, UserPermissionsObj
from api.views import UserViews, GroupViews, CategoryViews, AnnouncementViews, ImageViews, PublicityViews

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
    path("category/delete_all_categories/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.DeleteAllCategoriesView)).as_view()),
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

    # ANNOUNCEMENT
    path("announcement/create_announcement/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AnnouncementViews.CreateAnnouncementView)).as_view()),
    path("announcement/delete_announcement_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AnnouncementViews.DeleteAnnouncementByIdView)).as_view()),
    path("announcement/update_announcement_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AnnouncementViews.UpdateAnnouncementByIdView)).as_view()),
    path("announcement/find_all_announcements/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AnnouncementViews.GetAnnouncementView)).as_view()),
    path("announcement/find_announcement_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(AnnouncementViews.FindAnnouncementByIdView)).as_view()),

    # PUBLICITY
    path("publicity/create_publicity/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PublicityViews.CreatePublicityView)).as_view()),
    path("publicity/delete_publicity_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PublicityViews.DeletePublicityByIdView)).as_view()),
    path("publicity/update_publicity_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PublicityViews.UpdatePublicityByIdView)).as_view()),
    path("publicity/find_all_publicity/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PublicityViews.GetPublicityView)).as_view()),
    path("publicity/find_publicity_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PublicityViews.FindPublicityByIdView)).as_view()),

    # USERS
    path("user/access_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.AccessToken)).as_view()),
    path("user/refresh_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.RefreshToken)).as_view()),
    path("user/registration/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.UserRegistrationView)).as_view()),
    path("user/create_super_user/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.CreateSuperUserView)).as_view()),
    path("user/delete_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.DeleteUserByIdView)).as_view()),
    path("user/delete_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.DeleteAllUsersView)).as_view()),
    path("user/update_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([UserPermissionsObj])(UserViews.UpdateUserView)).as_view()),
    path("user/find_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([ROLE_ADMIN | AllowAny])(UserViews.GetUserView)).as_view()),
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
