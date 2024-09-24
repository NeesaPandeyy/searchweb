from django.shortcuts import render
from users.models import Person  
import io 
import pandas as pd
from django.http import HttpResponse

from django.shortcuts import render


def home(request):
    
    full_name_query = request.GET.get('full_name', '')
    job_title_query = request.GET.get('job_title', '')
    job_title_sub_role_query = request.GET.get('job_title_sub_role', '')
    job_company_location_name_query = request.GET.get('job_company_location_name', '')
    industry_query = request.GET.get('industry', '')
    location_name_query = request.GET.get('location_name', '')
    location_country_query = request.GET.get('location_country', '')
    skills_query = request.GET.get('skills', '')
    countries_query = request.GET.get('countries', '')
    education_query = request.GET.get('education', '')

    query = Person.objects.all()

    if full_name_query:
        query = query.filter(first_name__icontains=full_name_query)
    if job_title_query:
        query = query.filter(job_title__icontains=job_title_query)
    if job_title_sub_role_query:
        query = query.filter(job_title_sub_role__icontains=job_title_sub_role_query)
    if job_company_location_name_query:
        query = query.filter(job_company_location_name__icontains=job_company_location_name_query)
    if industry_query:
        query = query.filter(industry__icontains=industry_query)
    if location_name_query:
        query = query.filter(location_name__icontains=location_name_query)
    if location_country_query:
        query = query.filter(location_country__icontains=location_country_query)
    if skills_query:
        query = query.filter(skills__icontains=skills_query)
    if countries_query:
        query = query.filter(countries__icontains=countries_query)
    if education_query:
        query = query.filter(education__icontains=education_query)

    search_results = query

    return render(request, 'index.html', {'results': search_results})


def download(request):
    query = Person.objects.all()
    
    full_name_query = request.GET.get('full_name')
    job_title_query = request.GET.get('job_title')
    job_title_sub_role_query = request.GET.get('job_title_sub_role')
    job_company_location_name_query = request.GET.get('job_company_location_name')
    industry_query = request.GET.get('industry')
    location_name_query = request.GET.get('location_name')
    location_country_query = request.GET.get('location_country')
    skills_query = request.GET.get('skills')
    countries_query = request.GET.get('countries')
    education_query = request.GET.get('education')
    
    if full_name_query:
        query = query.filter(first_name__icontains=full_name_query)
    if job_title_query:
        query = query.filter(job_title__icontains=job_title_query)
    if job_title_sub_role_query:
        query = query.filter(job_title_sub_role__icontains=job_title_sub_role_query)
    if job_company_location_name_query:
        query = query.filter(job_company_location_name__icontains=job_company_location_name_query)
    if industry_query:
        query = query.filter(industry__icontains=industry_query)
    if location_name_query:
        query = query.filter(location_name__icontains=location_name_query)
    if location_country_query:
        query = query.filter(location_country__icontains=location_country_query)
    if skills_query:
        query = query.filter(skills__icontains=skills_query)
    if countries_query:
        query = query.filter(countries__icontains=countries_query)
    if education_query:
        query = query.filter(education__icontains=education_query)
    
    filtered_data = query
    
    data_list = [{
        "IDS": data.IDS,
        "id": data.id,
        "full_name": data.full_name,
        "first_name": data.first_name,
        "middle_initial": data.middle_initial,
        "middle_name": data.middle_name,
        "last_name": data.last_name,
        "gender": data.gender,
        "birth_year": data.birth_year,
        "birth_date": data.birth_date,
        "linkedin_url": data.linkedin_url,
        "linkedin_username": data.linkedin_username,
        "linkedin_id": data.linkedin_id,
        "facebook_url": data.facebook_url,
        "facebook_username": data.facebook_username,
        "facebook_id": data.facebook_id,
        "twitter_url": data.twitter_url,
        "twitter_username": data.twitter_username,
        "github_url": data.github_url,
        "github_username": data.github_username,
        "work_email": data.work_email,
        "mobile_phone": data.mobile_phone,
        "industry": data.industry,
        "job_title": data.job_title,
        "job_title_role": data.job_title_role,
        "job_title_sub_role": data.job_title_sub_role,
        "job_title_levels": data.job_title_levels,
        "job_company_id": data.job_company_id,
        "job_company_name": data.job_company_name,
        "job_company_website": data.job_company_website,
        "job_company_size": data.job_company_size,
        "job_company_founded": data.job_company_founded,
        "job_company_industry": data.job_company_industry,
        "job_company_linkedin_url": data.job_company_linkedin_url,
        "job_company_linkedin_id": data.job_company_linkedin_id,
        "job_company_facebook_url": data.job_company_facebook_url,
        "job_company_twitter_url": data.job_company_twitter_url,
        "job_company_location_name": data.job_company_location_name,
        "job_company_location_locality": data.job_company_location_locality,
        "job_company_location_metro": data.job_company_location_metro,
        "job_company_location_region": data.job_company_location_region,
        "job_company_location_geo": data.job_company_location_geo,
        "job_company_location_street_address": data.job_company_location_street_address,
        "job_company_location_address_line_2": data.job_company_location_address_line_2,
        "job_company_location_postal_code": data.job_company_location_postal_code,
        "job_company_location_country": data.job_company_location_country,
        "job_company_location_continent": data.job_company_location_continent,
        "job_last_updated": data.job_last_updated,
        "job_start_date": data.job_start_date,
        "job_summary": data.job_summary,
        "location_name": data.location_name,
        "location_locality": data.location_locality,
        "location_metro": data.location_metro,
        "location_region": data.location_region,
        "location_country": data.location_country,
        "location_continent": data.location_continent,
        "location_street_address": data.location_street_address,
        "location_address_line_2": data.location_address_line_2,
        "location_postal_code": data.location_postal_code,
        "location_geo": data.location_geo,
        "location_last_updated": data.location_last_updated,
        "linkedin_connections": data.linkedin_connections,
        "inferred_salary": data.inferred_salary,
        "inferred_years_experience": data.inferred_years_experience,
        "summary": data.summary,
        "phone_numbers": data.phone_numbers,
        "emails": data.emails,
        "interests": data.interests,
        "skills": data.skills,
        "location_names": data.location_names,
        "regions": data.regions,
        "countries": data.countries,
        "street_addresses": data.street_addresses,
        "experience": data.experience,
        "education": data.education,
        "profiles": data.profiles,
        "certifications": data.certifications,
        "languages": data.languages,
        "version_status": data.version_status
    } for data in filtered_data]
    
    df = pd.DataFrame(data_list)
    
    csv_buffer = io.StringIO()
    
    df.to_csv(csv_buffer, index=False)
    
    csv_buffer.seek(0)
    
    response = HttpResponse(csv_buffer, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    
    return response

