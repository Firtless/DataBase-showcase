from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, Enum, DECIMAL
from sqlalchemy.orm import relationship
from app.utils.db import Base

# Проміжна таблиця Many-to-Many (M:M) з бази даних
medical_records = Table(
    'medical_records',
    Base.metadata,
    Column('appointment_id', Integer, ForeignKey('appointments.id'), primary_key=True),
    Column('service_id', Integer, ForeignKey('services.id'), primary_key=True)
)

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False, unique=True)
    email = Column(String(100), nullable=True)

    # Зв'язок 1:M (Один клієнт має багато тварин)
    pets = relationship('Pet', backref='client_ref', cascade="all, delete-orphan")

    def put_into_dto(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email
        }

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True, autoincrement=True)
    species_name = Column(String(50), nullable=False)

    def put_into_dto(self):
        return {
            'id': self.id,
            'species_name': self.species_name
        }

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=False)
    pet_name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=True)
    gender = Column(Enum('M', 'F'), nullable=False)

    def put_into_dto(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'species_id': self.species_id,
            'pet_name': self.pet_name,
            'birth_date': str(self.birth_date) if self.birth_date else None,
            'gender': self.gender
        }

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_name = Column(String(150), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    def put_into_dto(self):
        return {
            'id': self.id,
            'service_name': self.service_name,
            'price': float(self.price) if self.price else 0.0
        }

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    vet_id = Column(Integer, ForeignKey('vets.id'))
    schedule_id = Column(Integer, ForeignKey('schedules.id'))
    appointment_datetime = Column(String(50))
    status = Column(String(50))

    # Зв'язок M:M через проміжну таблицю medical_records
    services = relationship('Service', secondary=medical_records, backref='appointments')

    def put_into_dto(self):
        return {
            'id': self.id,
            'appointment_datetime': str(self.appointment_datetime),
            'status': self.status
        }