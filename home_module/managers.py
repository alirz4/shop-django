from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, password, full_name):
        if not phone_number:
            raise ValueError('user must has phone number')

        if not email:
            raise ValueError('user must has email')

        if not full_name:
            raise ValueError('user must has full name')

        user = self.model(phone_number=phone_number, email=email, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, password, full_name):
        user = self.create_user(phone_number, email, password, full_name)
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
