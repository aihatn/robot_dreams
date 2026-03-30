import time, snap7, CONST
from dataclasses import dataclass
from snap7.util import get_int, get_bool


@dataclass
class PLCData:
    value1: int
    value2: int
    value3: int
    value4: int
    button1: bool
    button2: bool
    button3: bool
    button4: bool


def connection():
    client = snap7.client.Client()

    print("Připojuji se k PLC...")
    client.connect(CONST.PLC_IP, CONST.RACK, CONST.SLOT)

    if client.get_connected():
        print("PLC je připojeno!")
        return client
    else:
        raise Exception("Nepodařilo se připojit k PLC.")


def read_plc_data(client):

    data = client.db_read(CONST.DB_NUMBER, 0, CONST.SIZE)

    plc_data = PLCData(
        value1=get_int(data, 0),
        value2=get_int(data, 2),
        value3=get_int(data, 4),
        value4=get_int(data, 6),
        button1=get_bool(data, 8, 0),
        button2=get_bool(data, 8, 1),
        button3=get_bool(data, 8, 2),
        button4=get_bool(data, 8, 3),
    )

    return plc_data


def database_read(client):
    print("Čtení struktury z PLC... CTRL+C pro ukončení")

    while True:
        plc = read_plc_data(client)

        print(
            f"INT: {plc.value1}, {plc.value2}, {plc.value3}, {plc.value4} | "
            f"BTN: {plc.button1}, {plc.button2}, {plc.button3}, {plc.button4}"
        )

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