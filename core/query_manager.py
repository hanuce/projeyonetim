from sqlalchemy import text

class QueryManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def fetch_all(self, query, params=None):
        session = self.db_manager.get_session()
        try:
            result = session.execute(text(query), params or {})
            return result.fetchall()
        except Exception as e:
            print(f"Sorgu hatası: {e}")
            return []
        finally:
            session.close()

    def fetch_one(self, query, params=None):
        session = self.db_manager.get_session()
        try:
            result = session.execute(text(query), params or {})
            return result.fetchone()
        except Exception as e:
            print(f"Sorgu hatası: {e}")
            return None
        finally:
            session.close()

    def execute_query(self, query, params=None):
        session = self.db_manager.get_session()
        try:
            session.execute(text(query), params or {})
            session.commit()
        except Exception as e:
            print(f"Sorgu hatası: {e}")
        finally:
            session.close()