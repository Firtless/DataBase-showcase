from flask import Blueprint
from app.vetclinic.controller.client_controller import ClientController

client_bp = Blueprint('client_bp', __name__)
controller = ClientController()

@client_bp.route('/api/clients', methods=['GET'])
def get_clients():
    return controller.get_all()

@client_bp.route('/api/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    return controller.get_by_id(client_id)

@client_bp.route('/api/clients', methods=['POST'])
def create_client():
    return controller.create()

@client_bp.route('/api/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    return controller.update(client_id)

@client_bp.route('/api/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    return controller.delete(client_id)

# Зв'язок 1:M (Отримати всі тварини конкретного клієнта)
@client_bp.route('/api/clients/<int:client_id>/pets', methods=['GET'])
def get_client_pets(client_id):
    return controller.get_pets(client_id)

# Зв'язок M:M (Отримати всі послуги для конкретного прийому)
@client_bp.route('/api/appointments/<int:appointment_id>/services', methods=['GET'])
def get_appointment_services(appointment_id):
    return controller.get_appointment_services(appointment_id)