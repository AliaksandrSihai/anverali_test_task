from django.core.management import BaseCommand

from users.models import User
from config.settings import User_admin_email, User_admin_first_name,User_admin_last_name,User_admin_is_staff, User_admin_is_superuser, User_admin_password

class Command(BaseCommand):
    """Класс для создания админа"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email=User_admin_email,
            first_name=User_admin_first_name,
            last_name=User_admin_last_name,
            is_staff=User_admin_is_staff,
            is_superuser=User_admin_is_superuser,
        )
        user.set_password(User_admin_password)
        user.save()
