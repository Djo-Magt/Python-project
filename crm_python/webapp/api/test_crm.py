from api.crm import User
import pytest
from tinydb import TinyDB, table
from tinydb.storages import MemoryStorage

@pytest.fixture
def user():
    u = User(prenom="jo", nom="mag", address="panam", phone="0123456789")
    u.save()
    return u

@pytest.fixture
def set_up_db():
    User.DB = TinyDB(storage=MemoryStorage)

def test_exist(user):
    assert user.exist() is True


def test_full_name(user):
    assert user.full_name == "jo mag"


def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["prenom"] == "jo"

def test_no_db_instance(set_up_db):
    u = User(prenom="jo", nom="mag", address="panam", phone="0123456789")
    assert u.db_instance is None



def test_delete(set_up_db):
    u = User(prenom="jolad", nom="mag", address="panam", phone="0123456789")
    u.save()

    first = u.delete()
    second = u.delete()

    assert len(first) > 0
    assert len(second) == 0


def test_save(set_up_db):
    u = User(prenom="jolad", nom="mag", address="panam", phone="0123456789")
    b = User(prenom="jolad", nom="mag", address="panam", phone="0123456789")
    first = u.save()
    second = b.save()
    assert isinstance(first, int)
    assert isinstance(second, int)
    assert first > 0
    assert second == -1

def test__check_phone(set_up_db):
    u = User(prenom="jo", nom="mag", address="panam", phone="0123456789")
    b = User(prenom="ludo", nom="mag", address="panam", phone="abcd")

    with pytest.raises(ValueError) as err:
        b._check_phone()
    assert "invalid" in str(err.value)

    u.save(validate_data=True)
    assert u.exist() is True

