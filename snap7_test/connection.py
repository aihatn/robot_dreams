import time
import snap7
import CONST
from snap7.util import get_int

def main():
    client = snap7.client.Client()

    try:
        print("Připojuji se k PLC...")
        client.connect(CONST.PLC_IP, CONST.RACK, CONST.SLOT)

        if not client.get_connected():
            print("Nepodařilo se připojit k PLC.")
            return

        print("PLC je připojeno!")
        print("Čtení DB2.DBW0 každou sekundu. Ukončení pomocí CTRL+C.")

        while True:
            data = client.db_read(CONST.DB_NUMBER, CONST.START_OFFSET, CONST.SIZE)
            value = get_int(data, 0)
            print(f"Hodnota INT v DB{CONST.DB_NUMBER}.DBW{CONST.START_OFFSET}: {value}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nUkončuji program po stisku CTRL+C...")

    except Exception as e:
        print(f"Chyba: {e}")

    finally:
        if client.get_connected():
            client.disconnect()
        print("Odpojeno od PLC.")


if __name__ == "__main__":
    main()