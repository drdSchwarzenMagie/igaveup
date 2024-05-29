# Структурные модели
----
Этот документ описывает внутреннюю структуру приложения с использованием диаграмм классов и объектов/компонентов. 
Диаграммы выполнены с помощью PlantUML, позволяя визуализировать архитектурные решения и шаблоны проектирования, применяемые в проекте.
## Диаграммы классов
Диаграмма классов показывает структуру основных классов в модуле music_control.py, их взаимосвязи и методы.

![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/35ae3e1b-3590-4e49-9bdc-183d7841ef6a) ![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/50a9d319-46fc-49df-8c51-31b2dc33352c) ![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/e46db617-2d21-452d-a52c-961f447d3b18) ![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/6630d5e4-edf4-4172-9954-19d8ca64d6bf) ![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/df654b4d-f4f0-4bda-8bfd-64e80c43cc00) ![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/aca9b760-83d4-4b82-bda4-645509bf4509)







### Описание диаграммы
1. **Player**:
   * curr_track: Текущий проигрываемый трек.
   * playlist: Список треков в плейлисте.
   - select_track(track): Метод для выбора трека.
   - play(): Метод для начала воспроизведения.
   - pause(): Метод для постановки на паузу.
   - stop(): Метод для остановки воспроизведения.
   - load_music(directory): Метод для загрузки треков из указанной директории.
   - mute(): Метод для выключения звука.
   - unmute(): Метод для включения звука.
   - next_track(): Метод для переключения на следующий трек.
   - previous_track(): Метод для переключения на предыдущий трек.

2. **Track**:
   * title: Название трека.
   * is_paused: Флаг, указывающий, находится ли музыка на паузе.
   * duration: Продолжительность трека.
   * is_mut: Флаг, указывающий, выключен звук или нет.
   - mute(): Метод для выключения звука.
   - unmute(): Метод для включения звука.
-----
## Диаграмма объектов/компонентов

![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/76f81b22-3059-47e4-975a-abe4e828d916)


