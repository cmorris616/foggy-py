import json

from flask import Flask, render_template

from aws.sqs.sqs_service import SqsService
from globals import SERVICE_AWS_SQS

app = Flask(__name__)

AVAILABLE_SERVICES = {
    SERVICE_AWS_SQS: SqsService()
}


@app.route('/')
def home_page():
    """
    Returns the home page for the management console
    :return: the home page for the management console
    """
    return render_template('index.html')


@app.route('/<service>')
def service_page(service):
    """
    Returns the main page for the specified service
    :param service: the name of the service to return the page
    :return: the main page for the service
    """
    if service not in AVAILABLE_SERVICES.keys():
        return render_template("service_not_found.html")

    return render_template(AVAILABLE_SERVICES[service].main_page)


@app.route('/service/statuses')
def service_statuses():
    result = []
    for key, service in AVAILABLE_SERVICES.items():
        result.append({
            "name": service.name,
            "status": service.status
        })

    return json.dumps(result)
