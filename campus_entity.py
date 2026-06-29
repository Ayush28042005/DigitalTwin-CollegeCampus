from abc import ABC, abstractmethod

class CampusEntity(ABC):
    def __init__(self, entity_id, name):
        self.entity_id = entity_id      # Unique ID for every entity
        self.name = name                # Name of the entity

    @abstractmethod
    def get_info(self):
        pass                            # Every subclass MUST implement this

    @abstractmethod
    def to_dict(self):
        pass                            # Every subclass MUST implement this

    def __str__(self):
        return f"[{self.entity_id}] {self.name}"