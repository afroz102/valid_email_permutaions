import json
# from django.core import serializers
import concurrent.futures   # for threading
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render
from .email_perm_cons import generate_pattern, validate_user_email


@csrf_exempt
def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data)
        first_name = data.get('f_name')
        middle_name = data.get('m_name')
        last_name = data.get('l_name')
        domain_name = data.get('d_name')

        email_list = generate_pattern(
            first_name,
            middle_name,
            last_name,
            domain_name
        )

        # Used for threading
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(validate_user_email, email)
                       for email in email_list]
            final_data = []
            for f in concurrent.futures.as_completed(results):
                # print(f.result())
                final_data.append(f.result())
            # print(type(results))
        # data = serializers.serialize("json", results)
        return JsonResponse({"results": final_data})
