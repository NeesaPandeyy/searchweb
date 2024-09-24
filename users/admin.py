from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    # Display all fields in the list view (if appropriate)
    list_display = (
        'id', 'full_name', 'first_name', 'middle_initial', 'middle_name', 'last_name', 
        'gender', 'birth_year', 'birth_date', 'linkedin_url', 'linkedin_username', 
        'linkedin_id', 'facebook_url', 'facebook_username', 'facebook_id', 
        'twitter_url', 'twitter_username', 'github_url', 'github_username', 
        'work_email', 'mobile_phone', 'industry', 'job_title', 'job_title_role', 
        'job_title_sub_role', 'job_title_levels', 'job_company_id', 'job_company_name', 
        'job_company_website', 'job_company_size', 'job_company_founded', 
        'job_company_industry', 'job_company_linkedin_url', 'job_company_linkedin_id', 
        'job_company_facebook_url', 'job_company_twitter_url', 'job_company_location_name', 
        'job_company_location_locality', 'job_company_location_metro', 
        'job_company_location_region', 'job_company_location_geo', 
        'job_company_location_street_address', 'job_company_location_address_line_2', 
        'job_company_location_postal_code', 'job_company_location_country', 
        'job_company_location_continent', 'job_last_updated', 'job_start_date', 
        'job_summary', 'location_name', 'location_locality', 'location_metro', 
        'location_region', 'location_country', 'location_continent', 'location_street_address', 
        'location_address_line_2', 'location_postal_code', 'location_geo', 
        'location_last_updated', 'linkedin_connections', 'inferred_salary', 
        'inferred_years_experience', 'summary', 'phone_numbers', 'emails', 'interests', 
        'skills', 'location_names', 'regions', 'countries', 'street_addresses', 
        'experience', 'education', 'profiles', 'certifications', 'languages', 
        'version_status'
    )

    # Allow searching across multiple fields
    search_fields = ('full_name', 'last_name', 'full_name', 'work_email', 'mobile_phone')

    # Filters to make it easier to find specific records
    list_filter = ('gender', 'birth_year', 'job_company_name')

admin.site.register(Person, PersonAdmin)

