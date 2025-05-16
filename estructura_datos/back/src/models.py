from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {"id": 1, "first_name": "John", "last_name": "Jackson", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "last_name": "Jackson", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "last_name": "Jackson", "age": 5, "lucky_numbers": [1]}
        ]
        self._next_id = 4

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i, m in enumerate(self._members):
            if m["id"] == id:
                del self._members[i]
                return True
        return False

    def get_member(self, id):
        for m in self._members:
            if m["id"] == id:
                return m
        return None

    def get_all_members(self):
        return self._members
