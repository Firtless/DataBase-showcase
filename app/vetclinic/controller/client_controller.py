from flask import jsonify, request
from app.vetclinic.service.client_service import ClientService

class ClientController:
    def __init__(self):
        self.service = ClientService()

    def get_all(self):
        return jsonify(self.service.get_all_clients()), 200

    def get_by_id(self, client_id):
        client = self.service.get_client_by_id(client_id)
        if client:
            return jsonify(client), 200
        return jsonify({"error": "Client not found"}), 404

    def create(self):
        data = request.get_json()
        client = self.service.create_client(data)
        return jsonify(client), 201

    def update(self, client_id):
        data = request.get_json()
        client = self.service.update_client(client_id, data)
        if client:
            return jsonify(client), 200
        return jsonify({"error": "Client not found"}), 404

    def delete(self, client_id):
        success = self.service.delete_client(client_id)
        if success:
            return '', 204
        return jsonify({"error": "Client not found"}), 404

    def get_pets(self, client_id):
        pets = self.service.get_pets_for_client(client_id)
        return jsonify(pets), 200

    def get_appointment_services(self, appointment_id):
        services = self.service.get_services_for_appointment(appointment_id)
        return jsonify(services), 200