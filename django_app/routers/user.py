from rest_framework_nested import routers

from django_app.views.user import UserView

router = routers.SimpleRouter(trailing_slash=False)
router.register("user", UserView, basename='user')

urls = router.urls
