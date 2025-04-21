# ¡Desafío de Programación Avanzado: Menú Interactivo y Poderes Dinámicos en Mario Bros!


Basándonos en el trabajo que ya realizamos con la estructura de personajes y poderes, ¡ahora vamos a llevar este proyecto de Mario Bros al siguiente nivel!

**El Nuevo Reto:**

Tu misión ahora es expandir la interactividad del juego y la gestión de los poderes implementando las siguientes funcionalidades, integrándolas con el código base que ya existe:

1.  **Menú de Opciones Numéricas para el Jugador:**
    * Modifica el bucle principal del juego para presentar un menú de opciones numéricas al jugador.
    * Este menú debe permitir al jugador controlar el movimiento de Mario de la siguiente manera:
        * `1. Adelante` (incrementar `posicionX` de Mario)
        * `2. Atrás` (decrementar `posicionX` de Mario)
        * `3. Subir` (incrementar `posicionY` de Mario)
        * `4. Bajar` (decrementar `posicionY` de Mario)
    * Al seleccionar una opción, la función `mover()` del objeto `Jugador` (Mario) debe ser invocada con los parámetros correctos.

2.  **Generación Aleatoria de Poderes:**
    * En lugar de definir los poderes manualmente (`hongo1`, `hongo2`, `planta1`), crea una lista de al menos 10 objetos `Poder` (pueden ser instancias de `Hongo` con diferentes tipos o de `Planta`).
    * Las propiedades de cada poder (nombre, descripción, `posicionX`, `posicionY`, `estado`, y el `tipo` en caso de ser un `Hongo`) deben ser asignadas de forma aleatoria dentro de rangos lógicos para el entorno del juego. Asegúrate de que inicialmente todos los poderes estén `activo`.

3.  **Verificación de Colisión y Disponibilidad de Poderes:**
    * Dentro del bucle principal del juego (o en una función que se ejecute en cada paso), verifica si la `posicionX` e `posicionY` actuales del objeto `mario` coinciden con la `posicionX` e `posicionY` de algún objeto `Poder` en la lista de poderes generada.
    * Para cada poder en la lista, comprueba si:
        * `mario.posicionX == poder.posicionX`
        * `mario.posicionY == poder.posicionY`
        * Y si el `poder.estado == "activo"`
    * Si las tres condiciones se cumplen:
        * Llama al método `recogerPoder()` del objeto `mario` pasando el objeto `Poder` correspondiente como argumento.
        * Muestra un mensaje informativo indicando qué poder ha recogido Mario.

**Consideraciones Importantes:**

* Asegúrate de integrar el menú y la lógica de movimiento dentro de un bucle que permita al jugador interactuar continuamente con el juego hasta que decida salir (puedes añadir una opción "5. Salir" al menú).
* La generación aleatoria de las coordenadas de los poderes debe considerar un espacio de juego razonable para que Mario tenga la posibilidad de encontrarlos.
* Recuerda la estructura de clases `Personaje`, `Jugador`, `Poder`, `Hongo`, y `Planta` que ya han definido.

**¿Qué desafíos superarás con esta expansión?**

* Implementación de un bucle de juego interactivo basado en la entrada del usuario.
* Generación dinámica de objetos y gestión de listas.
* Implementación de lógica de detección de colisiones entre objetos.
* Integración de las funcionalidades existentes (`mover()`, `recogerPoder()`) en un flujo de juego más complejo.
!