from globals import SERVICE_AWS_SQS
from service import Service


class SqsService(Service):

    def __init__(self):
        self.name = 'SQS'
        self.status = 'Initializing'
        self.main_page = f'/{SERVICE_AWS_SQS}/status.html'
