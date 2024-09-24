from django.db import models

class Person(models.Model):
    IDS = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    id = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    middle_initial = models.CharField(max_length=10, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    birth_year = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.CharField(max_length=50, blank=True, null=True)
    
    linkedin_url = models.CharField(max_length=255, blank=True, null=True)
    linkedin_username = models.CharField(max_length=255, blank=True, null=True)
    linkedin_id = models.CharField(max_length=255, blank=True, null=True)
    
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_username = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_username = models.CharField(max_length=255, blank=True, null=True)
    
    github_url = models.CharField(max_length=255, blank=True, null=True)
    github_username = models.CharField(max_length=255, blank=True, null=True)
    
    work_email = models.CharField(max_length=255, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    
    job_title = models.CharField(max_length=255, blank=True, null=True)
    job_title_role = models.CharField(max_length=255, blank=True, null=True)
    job_title_sub_role = models.CharField(max_length=255, blank=True, null=True)
    job_title_levels = models.CharField(max_length=255, blank=True, null=True)
    
    job_company_id = models.CharField(max_length=255, blank=True, null=True)
    job_company_name = models.CharField(max_length=255, blank=True, null=True)
    job_company_website = models.CharField(max_length=255, blank=True, null=True)
    job_company_size = models.CharField(max_length=50, blank=True, null=True)
    job_company_founded = models.CharField(max_length=50, blank=True, null=True)
    job_company_industry = models.CharField(max_length=255, blank=True, null=True)
    
    job_company_linkedin_url = models.CharField(max_length=255, blank=True, null=True)
    job_company_linkedin_id = models.CharField(max_length=255, blank=True, null=True)
    job_company_facebook_url = models.CharField(max_length=255, blank=True, null=True)
    job_company_twitter_url = models.CharField(max_length=255, blank=True, null=True)
    
    job_company_location_name = models.CharField(max_length=255, blank=True, null=True)
    job_company_location_locality = models.CharField(max_length=255, blank=True, null=True)
    job_company_location_metro = models.CharField(max_length=255, blank=True, null=True)
    job_company_location_region = models.CharField(max_length=255, blank=True, null=True)
    job_company_location_geo = models.TextField(blank=True, null=True)
    job_company_location_street_address = models.CharField(max_length=255, blank=True, null=True)
    job_company_location_address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    job_company_location_postal_code = models.CharField(max_length=50, blank=True, null=True)
    job_company_location_country = models.CharField(max_length=255, blank=True, null=True)
    job_company_location_continent = models.CharField(max_length=255, blank=True, null=True)
    
    job_last_updated = models.CharField(max_length=50, blank=True, null=True)
    job_start_date = models.CharField(max_length=50, blank=True, null=True)
    job_summary = models.TextField(blank=True, null=True)
    
    location_name = models.CharField(max_length=255, blank=True, null=True)
    location_locality = models.CharField(max_length=255, blank=True, null=True)
    location_metro = models.CharField(max_length=255, blank=True, null=True)
    location_region = models.CharField(max_length=255, blank=True, null=True)
    location_country = models.CharField(max_length=255, blank=True, null=True)
    location_continent = models.CharField(max_length=255, blank=True, null=True)
    location_street_address = models.CharField(max_length=255, blank=True, null=True)
    location_address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    location_postal_code = models.CharField(max_length=50, blank=True, null=True)
    location_geo = models.TextField(blank=True, null=True)
    location_last_updated = models.CharField(max_length=50, blank=True, null=True)
    
    linkedin_connections = models.CharField(max_length=50, blank=True, null=True)
    inferred_salary = models.CharField(max_length=50, blank=True, null=True)
    inferred_years_experience = models.CharField(max_length=50, blank=True, null=True)
    
    summary = models.TextField(blank=True, null=True)
    phone_numbers = models.TextField(blank=True, null=True)
    emails = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    location_names = models.TextField(blank=True, null=True)
    regions = models.TextField(blank=True, null=True)
    countries = models.TextField(blank=True, null=True)
    street_addresses = models.TextField(blank=True, null=True)
    
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    profiles = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    
    version_status = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.first_name
