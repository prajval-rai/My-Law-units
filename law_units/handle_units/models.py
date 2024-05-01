from django.db import models

class Advocate(models.Model):
    advocate_id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    age = models.IntegerField()
    father_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    website = models.URLField(null=True, blank=True)
    tin = models.CharField(max_length=100)
    gst = models.CharField(max_length=30)
    pan = models.CharField(max_length=20)
    hourly_rate = models.IntegerField()

class office_address(models.Model):
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_postal_code = models.CharField(max_length=20)

class home_address(models.Model):
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_postal_code = models.CharField(max_length=20)

class contact_point(models.Model):
    advocate = models.ForeignKey(Advocate,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone_number = models.IntegerField()
    designation = models.CharField(max_length=20)

class case(models.Model):
    advocate = models.ForeignKey(Advocate,on_delete=models.CASCADE)
    case_number = models.IntegerField(primary_key=True)
    court = models.CharField(max_length=50)
    cnr_number = models.BooleanField()
    high_court = models.CharField(max_length=50)
    year = models.DateField()
    appearing_as = models.CharField(max_length=100)
    Petitioner = models.CharField(max_length=100)
    date_of_filling = models.DateField()
    court_hall = models.CharField(max_length=100)
    floor = models.CharField(max_length=50)
    classification = models.CharField(max_length=100)
    tital = models.CharField(max_length=60)
    disc = models.CharField(max_length=100)
    Before_Honble_Judg = models.CharField(max_length=100)
    ref_by = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    Priority = models.CharField(max_length=100)
    under_act = models.CharField(max_length=50)
    under_section = models.CharField(max_length=50)
    fir_police_station = models.CharField(max_length=50)
    fir_number = models.CharField(max_length=50)
    fir_year = models.DateField()
    affidavit_vakalat = models.BooleanField()
    filed = models.BooleanField()
    advocate = models.CharField(max_length=50)

class opponent(models.Model):
    case = models.ForeignKey(case,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()

class opponent_advocate(models.Model):
    case = models.ForeignKey(case,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()

class team_member(models.Model):
    member_id = models.ForeignKey(case,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length= 20)
    designation = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    cost_per_year = models.IntegerField()
