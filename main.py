import json
import os

from flask import Flask, send_file, request

from aws.sqs.sqs_service import SqsService
from globals import SERVICE_AWS_SQS

STATIC_DIR = 'static'

app = Flask(__name__)

AVAILABLE_SERVICES = {
    SERVICE_AWS_SQS: SqsService()
}


def get_static_page(file_name):
    """
    Returns the specified static file
    :param file_name: the name of the static file to be returned
    :return: the specified static file
    """
    return send_file(os.path.join(app.root_path, STATIC_DIR, file_name))


@app.route('/')
def home_page():
    """
    Returns the home page for the management console
    :return: the home page for the management console
    """
    return get_static_page('index.html')


@app.route('/<service>')
def service_request(service):
    """
    Returns the main page for the specified service
    :param service: the name of the service to return the page
    :return: the main page for the service
    """
    if service not in AVAILABLE_SERVICES.keys():
        return get_static_page("service_not_found.html")

    if len(request.args) == 0:
        return get_static_page(AVAILABLE_SERVICES[service].main_page)

    return AVAILABLE_SERVICES[service].process_request(request)


@app.route('/<service>/<page>')
def service_page(service, page):
    """
    Returns the specified page for the specified service
    :param service: the name of the service to which the page pertains
    :param page: the specific page for the service
    :return: the specified page for the specified service
    """
    if service not in AVAILABLE_SERVICES.keys():
        return get_static_page("service_not_found.html")

    return get_static_page(f"{service}/{page}")


@app.route('/service/statuses')
def service_statuses():
    result = []
    for key, service in AVAILABLE_SERVICES.items():
        result.append({
            "name": service.name,
            "status": service.status,
            "main_page": service.main_page
        })

    return json.dumps(result)
