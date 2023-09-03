import datetime
from Domain.Entities.room import Room
from Domain.Repositories.room_repository import RoomRepository


class RoomService:
    def __init__(self):
        self.rooms = []
        self.room_repository = RoomRepository()

    def get_all_rooms(self):
        rooms = self.room_repository.find_all()
        return [Room(room.id, room.name, room.room_type) for room in rooms if hasattr(room, 'room_type')]
    
    def create_room(self, name, room_type):
        new_room = self.room_repository.create_room(name, room_type)
        return Room(new_room.id, new_room.name, new_room.room_type)
    
    def get_room_by_id(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            return Room(room.id, room.name)
        return None
    
    def update_room(self, room_id, new_name):
        room = self.room_repository.find_by_id(room_id)
        if room:
            room.name = new_name
            return Room(room.id, room.name)
        return None

    def get_occupied_rooms(self):
        occupied_rooms = [room for room in self.room_repository.find_all() if room.is_occupied]
        return [Room(room.id, room.name) for room in occupied_rooms]
    
    def reserve_room(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            if room.is_occupied:
                return None  # A sala já está ocupada
            room.is_occupied = True
            return self.get_room_details(room_id)  # Retorna detalhes da sala após a reserva
        return None
    
    def get_room_details(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            return {
                'id': room.id,
                'name': room.name,
                'is_occupied': room.is_occupied
            }
        return None
    
    def delete_room(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            self.room_repository.delete_room(room)
            return True  # Sala excluída com sucesso
        return False
    
    def get_available_rooms(self):
        available_rooms = [room for room in self.room_repository.find_all() if not room.is_occupied]
        return [Room(room.id, room.name) for room in available_rooms]
    
    def update_room_name(self, room_id, new_name):
        room = self.room_repository.find_by_id(room_id)
        if room:
            room.name = new_name
            return Room(room.id, room.name)
        return None
    
    def get_rooms_by_type(self, room_type):
        rooms = self.room_repository.find_by_type(room_type)
        return [Room(room.id, room.name, room.room_type) for room in rooms]
    
    def reserve_room_by_period(self, room_id, start_time, end_time):
        room = self.find_by_id(room_id)

        if room is None:
            return {'error': 'Room not found'}

        try:
            start_datetime = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            end_datetime = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return {'error': 'Invalid date format'}

        if start_datetime >= end_datetime:
            return {'error': 'Invalid time period'}

        for reservation in room.reservations:
            if start_datetime < reservation['end_time'] and end_datetime > reservation['start_time']:
                return {'error': 'Room already occupied during this period'}

        room.reservations.append({
            'start_time': start_datetime,
            'end_time': end_datetime
        })

        return {'message': 'Room reserved successfully'}
    
    def find_by_id(self, room_id):
        for room in self.rooms:
            print(f"Room ID: {room.id}")
            if room.id == room_id:
                return room
        return None