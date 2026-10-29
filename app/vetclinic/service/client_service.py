from app.vetclinic.dao.client_dao import ClientDAO

class ClientService:
    def __init__(self):
        self.dao = ClientDAO()

    def get_all_clients(self):
        clients = self.dao.get_all()
        return [c.put_into_dto() for c in clients]

    def get_client_by_id(self, client_id):
        client = self.dao.get_by_id(client_id)
        return client.put_into_dto() if client else None

    def create_client(self, client_data):
        client = self.dao.create(client_data)
        return client.put_into_dto()

    def update_client(self, client_id, client_data):
        client = self.dao.update(client_id, client_data)
        return client.put_into_dto() if client else None

    def delete_client(self, client_id):
        return self.dao.delete(client_id)

    def get_pets_for_client(self, client_id):
        pets = self.dao.get_pets_by_client(client_id)
        return [p.put_into_dto() for p in pets]

    def get_services_for_appointment(self, appointment_id):
        services = self.dao.get_appointment_services(appointment_id)
        return [s.put_into_dto() for s in services]