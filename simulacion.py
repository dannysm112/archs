import time
import threading
from datamanager import RealTimeDataManager

def callback_imprimir_datos(data):
    print(f"Datos en tiempo real actualizados: {data}")

if __name__ == "__main__":
    real_time_data_manager = RealTimeDataManager()
    real_time_data_manager.event_manager.subscribe("datos_actualizados", callback_imprimir_datos)

    # Actualizaciones en tiempo real en segundo plano
    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    update_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPrograma terminado.")