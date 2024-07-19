from django.contrib.auth.base_user import AbstractBaseUser

from django.db import models

# Create your models here.

class User(AbstractBaseUser):
    """
        관리자 프로필 사진
        관리자 닉네임
        관리자 이메일주소
        관리자 비밀번호
    """