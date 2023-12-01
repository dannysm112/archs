# Programa de Actualización en Tiempo Real

## Archivos del Programa

### 1. datamanager.py

Este archivo define la clase `RealTimeDataManager`, que gestiona datos en tiempo real de temperatura y humedad. Utiliza un hilo para simular actualizaciones continuas y un objeto `EventManager` para gestionar eventos y notificar a los suscriptores cuando los datos cambian.

#### Funciones Clave:

- `__init__`: Inicializa los datos y el gestor de eventos.
- `start_real_time_updates`: Inicia un bucle que genera datos en tiempo real y notifica a los suscriptores cada 3 segundos.
- `generate_real_time_data`: Simula la generación de datos aleatorios de temperatura y humedad.

### 2. eventos.py

Este archivo define la clase `EventManager`, que gestiona la suscripción, cancelación de suscripción y notificación de eventos a los suscriptores.

#### Funciones Clave:

- `subscribe`: Permite a los suscriptores registrarse para recibir notificaciones de eventos específicos.
- `unsubscribe`: Permite a los suscriptores cancelar su suscripción a eventos.
- `notify`: Notifica a los suscriptores cuando ocurre un evento específico.

### 3. simulacion.py

Este archivo es el punto de entrada del programa. Crea una instancia de `RealTimeDataManager`, se suscribe a eventos de actualización de datos y utiliza un hilo para ejecutar las actualizaciones en tiempo real. Además, maneja la interrupción del teclado (Ctrl+C) para cerrar el programa correctamente.

#### Funciones Clave:

- `callback_imprimir_datos`: Una función de devolución de llamada que imprime los datos actualizados.
- Bloque principal: Crea instancias, configura la suscripción y ejecuta el hilo.

## Discusión con Ejemplos de Resultados del Programa

El programa simula actualizaciones continuas de datos de temperatura y humedad. Aquí hay algunos ejemplos de cómo se ejecutaría:

### Ejemplo de Ejecución:

1. Inicia el programa.
2. Imprime "Datos en tiempo real actualizados" cada 3 segundos con valores de temperatura y humedad que cambian aleatoriamente.

### Salida Esperada:

```plaintext
Datos en tiempo real actualizados: {'temperatura': 24.56, 'humedad': 58.32}
Datos en tiempo real actualizados: {'temperatura': 25.21, 'humedad': 59.78}
Datos en tiempo real actualizados: {'temperatura': 24.89, 'humedad': 61.11}
