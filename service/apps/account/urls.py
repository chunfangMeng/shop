from apps.account.controller.auth.member import views as member_views
from apps.account.controller.auth.backend import views as backend_views
from rest_framework.routers import SimpleRouter

urlpatterns = [

]

router = SimpleRouter()

router.register('member', member_views.UserMemberView, basename='user_member_view')
router.register('manager', backend_views.ManagerUserView, basename='manager_user')


urlpatterns += router.urls
