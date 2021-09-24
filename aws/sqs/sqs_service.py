from globals import SERVICE_AWS_SQS
from service import Service


class SqsService(Service):
    queue_list = []

    def __init__(self):
        self.name = 'SQS'
        self.status = 'Initializing'
        self.main_page = f'/{SERVICE_AWS_SQS}/status.html'
        self.status = "Running"

    def process_request(self, request):
        if 'Action' not in request.args:
            return 'Missing "Action" parameter', 400

        if request.args['Action'].lower() == 'createqueue':
            self.create_queue(request)
            return 'Queue Created', 200

        return 'Something', 200

    def create_queue(self, request):
        queue_name = request.args['QueueName']
        
        self.queue_list.append(request.args['QueueName'])
