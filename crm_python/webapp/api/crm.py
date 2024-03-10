import re
import string
from pathlib import Path
from typing import List

from tinydb import TinyDB, where


class User:
    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

    def __init__(self, prenom: str, nom: str, address: str = "", phone: str = ""):
        self.prenom = prenom
        self.nom = nom
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"{self.full_name}\n{self.address}\n{self.phone} "

    def __repr__(self):
        return f"User({self.prenom} {self.nom})"

    def delete(self) -> List[int]:
        if self.exist():
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])
        return []

    def exist(self):
        return bool(self.db_instance)

    def save(self, validate_data: bool = False) -> int:
        if validate_data:
            self._checks()

        if self.exist():
            return -1
        else:
            return User.DB.insert(self.__dict__)

    @property
    def full_name(self):
        return f"{self.prenom} {self.nom}"

    @property
    def db_instance(self):
        return User.DB.get((where('prenom') == self.prenom) & (where('nom') == self.nom))

    def _checks(self):
        self._check_name()
        self._check_phone()

    def _check_phone(self):
        phone_digit = re.sub(r"[+()\s]*", "", self.phone)
        if len(phone_digit) < 10 or not phone_digit.isdigit:
            raise ValueError(f"num {self.phone} invalid")

    def _check_name(self):
        if not (self.prenom and self.nom):
            raise ValueError

        special_characters = string.digits + string.punctuation

        for character in self.prenom + self.nom:
            if character in special_characters:
                raise ValueError


def get_all_users():
    return [User(**user) for user in User.DB.all()]


if __name__ == "__main__":
    print(get_all_users())
    # print(martin.db_instance)

    # from faker import Faker
    # fake = Faker(locale="fr_FR")
    # for _ in range(2):
    #     user = User(prenom = fake.first_name(),
    #                 nom = fake.last_name(),
    #                 address = re.sub("[\n]"," ",fake.address()),
    #                 phone = fake.phone_number())
    #     print(user.save()

    print("-" * 10)
