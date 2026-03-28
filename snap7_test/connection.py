import time, snap7, CONST
from snap7.util import get_int


def connection():
    client = snap7.client.Client()

    print("Připojuji se k PLC...")
    client.connect(CONST.PLC_IP, CONST.RACK, CONST.SLOT)

    if client.get_connected():
        print("PLC je připojeno!")
        return client
    else:
        raise Exception("Nepodařilo se připojit k PLC.")


def database_read(client):
    print(f"Čtení DB{CONST.DB_NUMBER}.DBW{CONST.START_OFFSET} každou sekundu. Ukončení pomocí CTRL+C.")

    while True:
        data = client.db_read(CONST.DB_NUMBER, CONST.START_OFFSET, CONST.SIZE)
        value = get_int(data, 0)
        print(f"Hodnota INT v DB{CONST.DB_NUMBER}.DBW{CONST.START_OFFSET}: {value}")
        time.sleep(1)


def main():
    client = None

    try:
        client = connection()
        database_read(client)

    except KeyboardInterrupt:
        print("\nUkončuji program po stisku CTRL+C...")

    except Exception as e:
        print(f"Chyba: {e}")

    finally:
        if client and client.get_connected():
            client.disconnect()
        print("Odpojeno od PLC.")


if __name__ == "__main__":
    main()