from DBService import DBService
from configparser import ConfigParser

from ElectrumService import ElectrumService


def main(db: DBService, electrum: ElectrumService):
    print(db.getAddresses())
    print(electrum.payTo("tb1qw2c3lxufxqe2x9s4rdzh65tpf4d7fssjgh8nv6","0.00001"))
    electrum.stop_eventloop()
    exit(0)


def check_config(config: ConfigParser):
    required_sections = ["mysql", "settings", "electrum"]

    for section in required_sections:
        if section not in config.sections():
            print(
                f"Error: Missing '{section}' section in the configuration file.")
            exit(1)


# Завантаження конфігурацій з файлу
config = ConfigParser()
config.read("config.ini")
check_config(config)


if __name__ == "__main__":
    # Отримання параметрів підключення
    host = config.get("mysql", "host")
    user = config.get("mysql", "user")
    dbpassword = config.get("mysql", "password")
    database = config.get("mysql", "database")

    wallet_pass = config.get("electrum", "password")
    is_test_network = config.getboolean("electrum", "testnetwork")

    db = DBService(host, user, dbpassword, database)
    electrum = ElectrumService(wallet_pass,is_test_network)
    try:
        main(db, electrum)
    except Exception as e:
        print(e)
        exit(1)
    finally:
        db.cursor.close()
        db.connection.close()
