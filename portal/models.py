from enum import Enum
from django.db import models


# some enums
class Choice(object):
    @classmethod
    def choices(cls):
        try:
            return tuple([(item.value, item.name)
                        for item in list(cls)])
        except TypeError:
            return None


class Gender(int, Choice, Enum):
    male = 0
    female = 1
    others = 2


class BloodGroup(int, Choice, Enum):
    A = 0
    B = 1
    AB = 2
    O = 3


class MaritalStatus(int, Choice, Enum):
    married = 0
    single = 1


class AcademicProgram(int, Choice, Enum):
    undergraduate = 0
    postgraduate = 1
    doctoral = 2
    dual_degree = 3


class Visibility(int, Choice, Enum):
    public = 0
    only_me = 1
    iiita = 2


# Create your models here.

class Address(models.Model):
    address_line_1 = models.CharField(max_length=100, blank=True)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    scope = models.SmallIntegerField(
        choices=Visibility.choices(),
        default=Visibility.iiita
    )
    user_roll_no = models.CharField(max_length=20)

    def __str__(self):
        return "{} | {}, {}, {}".format(
            self.user_roll_no,
            self.address_line_1,
            self.city,
            self.country
        )


class User(models.Model):
    roll_no = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    date_of_birth = models.DateField(null=False)
    gender = models.SmallIntegerField(choices=Gender.choices(), null=False)
    blood_group = models.SmallIntegerField(choices=BloodGroup.choices(), null=True, blank=True)
    marital_status = models.SmallIntegerField(choices=MaritalStatus.choices(), null=True, blank=True)
    photograph = models.ImageField(upload_to='images', null=True, blank=True)
    nationality = models.CharField(max_length=50, null=False, blank=True)

    email_1 = models.EmailField(null=False, unique=True)
    email_2 = models.EmailField(null=True, blank=True)
    phone_1 = models.CharField(max_length=20, null=True, blank=True)
    phone_2 = models.CharField(max_length=20, null=True, blank=True)

    link_facebook = models.CharField(max_length=100, null=True, blank=True)
    link_twitter = models.CharField(max_length=100, null=True, blank=True)
    link_linkedin = models.CharField(max_length=100, null=True, blank=True)
    link_skype = models.CharField(max_length=100, null=True, blank=True)

    choice_facebook_scope = models.SmallIntegerField(
        choices=Visibility.choices(),
        null=True,
        default=Visibility.iiita
    )
    choice_twitter_scope = models.SmallIntegerField(
        choices=Visibility.choices(),
        null=True,
        default=Visibility.iiita
    )
    choice_linkedin_scope = models.SmallIntegerField(
        choices=Visibility.choices(),
        null=True,
        default=Visibility.iiita
    )
    choice_skype_scope = models.SmallIntegerField(
        choices=Visibility.choices(),
        null=True,
        default=Visibility.iiita
    )

    link_github = models.CharField(max_length=100, null=True, blank=True)
    link_blog = models.CharField(max_length=200, null=True, blank=True)
    link_website = models.CharField(max_length=200, null=True, blank=True)

    permanent_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='permanent_address',
    )
    current_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='current_address',
    )

    def __str__(self):
        return "{} | {}".format(self.roll_no, self.name)


class Qualification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program_code = models.SmallIntegerField(choices=AcademicProgram.choices(), null=True)
    institute_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    convocation_year = models.SmallIntegerField()


class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employer = models.CharField(max_length=150)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    sector = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50)
    founder = models.BooleanField(default=False)
    location = models.OneToOneField(
        Address,
        on_delete=models.CASCADE
    )
