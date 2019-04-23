import sqlite3
import os.path


class Client:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'data.db')
        self.data = sqlite3.connect(db_path)
        self.d = self.data.cursor()
    
    async def get_value(self, id):
        self.d.execute("SELECT * FROM players WHERE id=?",id)
        return self.d.fetchall()
    
    async def create_value(self, id):
        with self.data:
            self.d.execute(f"INSERT INTO players VALUES (?, ?)", [id, 0])
    
    async def update(self, bal, id):
        with self.data:
            self.d.execute("UPDATE players SET bal=? WHERE id=?", [bal, id])