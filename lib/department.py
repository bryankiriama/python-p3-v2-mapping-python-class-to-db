from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

@classmethod
def create_table(cls):
    sql = """
    CREATE TABLE IF NOT EXISTS departsments(
    id INTEGER PRIMARY,
    name TEXT,
     location TEXT
     )
    """
    CURSOR.executes(sql)
    CONN.commit()


@classmethod
def delete_table(cls):
    sql ="""
    DROP TABLE IF 
    """