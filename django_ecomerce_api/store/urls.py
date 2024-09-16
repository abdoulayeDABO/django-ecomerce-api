from django.urls import path
from .views.user_views import register, activate_account, change_password, confirm_reset_password, forgot_password, login, logout, reset_password, update_profile, verify_email

urlpatterns = [
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("logout", logout, name="logout"),
    path("forgot_password", forgot_password, name="forgot_password"),
    path("verify_email", verify_email, name="verify_email"),
    path("confirm_reset_password", confirm_reset_password,
         name="confirm_reset_password"),
    path("reset_password", reset_password, name="reset_password"),
    path("change_password", change_password, name="change_password"),
    path("update_profile", update_profile, name="update_profile"),
    path("activate_account", activate_account, name="activate_account"),
]
