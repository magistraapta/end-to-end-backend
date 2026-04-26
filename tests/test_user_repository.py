from app.repository.user_repository import UserRepository


class FakeCursor:
    def __init__(self, documents):
        self.documents = documents
        self.to_list_length = None

    async def to_list(self, length):
        self.to_list_length = length
        return self.documents


class FakeCollection:
    def __init__(self):
        self.inserted_document = None
        self.find_one_queries = []
        self.update_calls = []
        self.delete_queries = []
        self.cursor = FakeCursor([{"id": 1, "name": "Alice"}])

    async def insert_one(self, document):
        self.inserted_document = document

    async def find_one(self, query):
        self.find_one_queries.append(query)
        return {"id": 1, "name": "Alice", **query}

    async def update_one(self, query, update):
        self.update_calls.append((query, update))

    async def delete_one(self, query):
        self.delete_queries.append(query)

    def find(self):
        return self.cursor


class FakeDatabase:
    def __init__(self):
        self.users = FakeCollection()

    def __getitem__(self, collection_name):
        if collection_name != "users":
            raise KeyError(collection_name)
        return self.users


def test_create_user_inserts_user_document(run_async, user_schema):
    db = FakeDatabase()
    repository = UserRepository(db)

    run_async(repository.create_user(user_schema))

    assert db.users.inserted_document == user_schema.model_dump()


def test_get_user_finds_by_mongodb_id(run_async):
    db = FakeDatabase()
    repository = UserRepository(db)

    result = run_async(repository.get_user(1))

    assert db.users.find_one_queries == [{"_id": 1}]
    assert result["_id"] == 1


def test_update_user_sets_user_document_by_mongodb_id(run_async, user_schema):
    db = FakeDatabase()
    repository = UserRepository(db)

    run_async(repository.update_user(1, user_schema))

    assert db.users.update_calls == [
        ({"_id": 1}, {"$set": user_schema.model_dump()}),
    ]


def test_delete_user_deletes_by_mongodb_id(run_async):
    db = FakeDatabase()
    repository = UserRepository(db)

    run_async(repository.delete_user(1))

    assert db.users.delete_queries == [{"_id": 1}]


def test_get_all_users_returns_first_100_documents(run_async):
    db = FakeDatabase()
    repository = UserRepository(db)

    result = run_async(repository.get_all_users())

    assert result == [{"id": 1, "name": "Alice"}]
    assert db.users.cursor.to_list_length == 100


def test_get_user_by_email_finds_by_email(run_async):
    db = FakeDatabase()
    repository = UserRepository(db)

    result = run_async(repository.get_user_by_email("alice@example.com"))

    assert db.users.find_one_queries == [{"email": "alice@example.com"}]
    assert result["email"] == "alice@example.com"


def test_get_user_by_id_finds_by_mongodb_id(run_async):
    db = FakeDatabase()
    repository = UserRepository(db)

    result = run_async(repository.get_user_by_id(1))

    assert db.users.find_one_queries == [{"_id": 1}]
    assert result["_id"] == 1


def test_get_user_by_name_finds_by_name(run_async):
    db = FakeDatabase()
    repository = UserRepository(db)

    result = run_async(repository.get_user_by_name("Alice"))

    assert db.users.find_one_queries == [{"name": "Alice"}]
    assert result["name"] == "Alice"
