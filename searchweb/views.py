from django.shortcuts import render
from users.models import Person
import io 
import pandas as pd
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator

def build_query(params):
    query = Q()

    if params.get('full_name'):
        full_name = params['full_name'].split()  # Split by spaces to separate first and last names
        if len(full_name) > 1:
            query |= Q(first_name__icontains=full_name[0]) & Q(last_name__icontains=full_name[1])
        else:
            query |= Q(first_name__icontains=full_name[0]) | Q(last_name__icontains=full_name[0])

    if params.get('job_title'):
        query |= Q(job_title__icontains=params['job_title'])
    if params.get('job_title_sub_role'):
        query |= Q(job_title_sub_role__icontains=params['job_title_sub_role'])
    if params.get('job_company_location_name'):
        query |= Q(job_company_location_name__icontains=params['job_company_location_name'])
    if params.get('industry'):
        query |= Q(industry__icontains=params['industry'])
    if params.get('location_name'):
        query |= Q(location_name__icontains=params['location_name'])
    if params.get('location_country'):
        query |= Q(location_country__icontains=params['location_country'])
    if params.get('skills'):
        query |= Q(skills__icontains=params['skills'])
    if params.get('countries'):
        query |= Q(countries__icontains=params['countries'])
    if params.get('education'):
        query |= Q(education__icontains=params['education'])

    return query

def home(request):
    # Capture search query parameters from GET request
    query_params = {
        'full_name': request.GET.get('full_name', ''),
        'job_title': request.GET.get('job_title', ''),
        'job_title_sub_role': request.GET.get('job_title_sub_role', ''),
        'job_company_location_name': request.GET.get('job_company_location_name', ''),
        'industry': request.GET.get('industry', ''),
        'location_name': request.GET.get('location_name', ''),
        'location_country': request.GET.get('location_country', ''),
        'skills': request.GET.get('skills', ''),
        'countries': request.GET.get('countries', ''),
        'education': request.GET.get('education', '')
    }

    # Build the query using the helper function
    query = build_query(query_params)

    # Fetch the search results
    search_results = Person.objects.filter(query).order_by('IDS')

    # Implement pagination
    paginator = Paginator(search_results, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {
        'results': page_obj,
        'total_results': search_results.count()
    })

def download(request):
    # Capture search query parameters from GET request
    query_params = {
        'full_name': request.GET.get('full_name', ''),
        'job_title': request.GET.get('job_title', ''),
        'job_title_sub_role': request.GET.get('job_title_sub_role', ''),
        'job_company_location_name': request.GET.get('job_company_location_name', ''),
        'industry': request.GET.get('industry', ''),
        'location_name': request.GET.get('location_name', ''),
        'location_country': request.GET.get('location_country', ''),
        'skills': request.GET.get('skills', ''),
        'countries': request.GET.get('countries', ''),
        'education': request.GET.get('education', '')
    }

    # Build the query using the helper function
    query = build_query(query_params)

    # Fetch the search results
    search_results = Person.objects.filter(query)

    # Use values() to extract field data efficiently
    data_list = search_results.values(
        'IDS', 'id', 'full_name', 'first_name', 'middle_initial', 'middle_name', 'last_name', 
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

    # Convert to DataFrame and export to CSV
    df = pd.DataFrame(data_list)

    # Create a CSV buffer
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Prepare the response
    response = HttpResponse(csv_buffer.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    return response
