class Room:
    def __init__(self, id, name, room_type=None, is_occupied=False, capacity=None, description=None, room_category=None):
        self.id = id
        self.name = name
        self.room_type = room_type
        self.is_occupied = is_occupied
        self.capacity = capacity
        self.description = description
        self.room_category = room_category  # Adicione o campo room_category
        self.reservations = []

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'is_occupied': self.is_occupied,
            'room_category': self.room_category  # Inclua o campo room_category na saída JSON
        }

    def to_detailed_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'is_occupied': self.is_occupied,
            'capacity': self.capacity,
            'description': self.description,
            'room_category': self.room_category,  # Inclua o campo room_category na saída detalhada JSON
            'reservations': self.reservations
        }
