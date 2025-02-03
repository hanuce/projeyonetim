import time
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError, OperationalError

class DBManager:
    def __init__(self, retry_attempts: int = 5, retry_delay: int = 2):
        """
        Veritabanı yöneticisi. Veritabanı bağlantısı ve havuzlama işlemlerini yönetir.
        Veritabanı yollarını sabit olarak dict içinde tutar.
        :param retry_attempts: Bağlantı deneme sayısı (varsayılan: 5)
        :param retry_delay: Her deneme arasında bekleme süresi (saniye, varsayılan: 2)
        """
        # Veritabanı yolları ve isimleri
        self.database_config = {
            "statics": "sqlite:///databases/statics.db",
            "users": "sqlite:///databases/users.db",
            "sessions": "sqlite:///databases/sessions.db",
            "projects": "sqlite:///databases/projects.db",
        }
        self.engines = {}  # Engine havuzu
        self.retry_attempts = retry_attempts
        self.retry_delay = retry_delay

    def connect(self, db_name: str):
        """
        Belirtilen bir veritabanına bağlantı sağlar ve bir engine oluşturur.
        Kilitli bir durumda belirli sayıda tekrar deneme yapar.
        :param db_name: Bağlanılacak veritabanı adı (örnek: 'users')
        :return: SQLAlchemy Engine
        """
        if db_name not in self.database_config:
            raise ValueError(f"{db_name} için tanımlı bir veritabanı yolu bulunamadı.")

        if db_name not in self.engines:
            for attempt in range(self.retry_attempts):
                try:
                    # Engine oluşturuluyor ve havuza ekleniyor
                    engine = create_engine(self.database_config[db_name])
                    self.engines[db_name] = engine
                    print(f"{db_name} veritabanına bağlantı başarıyla oluşturuldu.")
                    return engine
                except OperationalError as e:
                    print(f"{db_name} veritabanına bağlanırken bir hata oluştu: {e}")
                    if attempt < self.retry_attempts - 1:
                        print(f"Yeniden deneme {attempt + 1}/{self.retry_attempts}, {self.retry_delay} saniye bekleniyor...")
                        time.sleep(self.retry_delay)
                    else:
                        raise RuntimeError(f"{db_name} veritabanına bağlanılamadı. Tüm denemeler başarısız oldu.")
        return self.engines[db_name]

    def get_connection(self, db_name: str):
        """
        Belirtilen veritabanına bağlantı döner.
        Kilitli bir durumda belirli sayıda tekrar deneme yapar.
        :param db_name: Bağlanılacak veritabanı adı (örnek: 'users')
        :return: SQLAlchemy Connection
        """
        engine = self.connect(db_name)
        for attempt in range(self.retry_attempts):
            try:
                connection = engine.connect()
                print(f"{db_name} veritabanı için bağlantı açıldı.")
                return connection
            except OperationalError as e:
                print(f"{db_name} veritabanına bağlanırken bir hata oluştu: {e}")
                if attempt < self.retry_attempts - 1:
                    print(f"Yeniden deneme {attempt + 1}/{self.retry_attempts}, {self.retry_delay} saniye bekleniyor...")
                    time.sleep(self.retry_delay)
                else:
                    raise RuntimeError(f"{db_name} veritabanına bağlanılamadı. Tüm denemeler başarısız oldu.")

    def close_connection(self, db_name: str):
        """
        Belirtilen veritabanı bağlantısını kapatır.
        :param db_name: Bağlantısı kapatılacak veritabanı adı
        """
        if db_name in self.engines:
            engine = self.engines[db_name]
            engine.dispose()
            del self.engines[db_name]
            print(f"{db_name} veritabanı bağlantısı kapatıldı.")
        else:
            print(f"{db_name} için açık bir bağlantı bulunamadı.")

    def close_all_connections(self):
        """
        Tüm açık veritabanı bağlantılarını kapatır.
        """
        for db_name in list(self.engines.keys()):
            self.close_connection(db_name)
        print("Tüm veritabanı bağlantıları kapatıldı.")
