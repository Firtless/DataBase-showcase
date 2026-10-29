from app.utils.db import session
from app.vetclinic.domain.models import Client

class ClientDAO:
    def get_all(self):
        return session.query(Client).all()

    def get_by_id(self, client_id):
        return session.query(Client).filter(Client.id == client_id).first()

    def create(self, client_data):
        client = Client(
            first_name=client_data.get('first_name'),
            last_name=client_data.get('last_name'),
            phone=client_data.get('phone'),
            email=client_data.get('email')
        )
        session.add(client)
        session.commit()
        return client

    def update(self, client_id, client_data):
        client = self.get_by_id(client_id)
        if client:
            client.first_name = client_data.get('first_name', client.first_name)
            client.last_name = client_data.get('last_name', client.last_name)
            client.phone = client_data.get('phone', client.phone)
            client.email = client_data.get('email', client.email)
            session.commit()
        return client

    def delete(self, client_id):
        client = self.get_by_id(client_id)
        if client:
            session.delete(client)
            session.commit()
            return True
        return False

    def get_pets_by_client(self, client_id):
        client = self.get_by_id(client_id)
        return client.pets if client else []

    def get_appointment_services(self, appointment_id):
        from app.vetclinic.domain.models import Appointment
        app_obj = session.query(Appointment).filter(Appointment.id == appointment_id).first()
        return app_obj.services if app_obj else []