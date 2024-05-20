# Структурные модели
----
Этот документ описывает внутреннюю структуру приложения с использованием диаграмм классов и объектов/компонентов. 
Диаграммы выполнены с помощью PlantUML, позволяя визуализировать архитектурные решения и шаблоны проектирования, применяемые в проекте.
## Диаграммы классов
Диаграмма классов показывает структуру основных классов в модуле music_control.py, их взаимосвязи и методы.![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/5ce1cd4a-4493-42b0-a70b-f00d3e8daf88)



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

2. **Track**:
   * title: Название трека.
   * is_paused: Флаг, указывающий, находится ли музыка на паузе.
   * duration: Продолжительность трека.
   * is_mut: Флаг, указывающий, выключен звук или нет.
3. **Playlist**:
   - next_track(): Метод для переключения на следующий трек.
   - previous_track(): Метод для переключения на предыдущий трек.
-----
## Диаграмма объектов/компонентов
![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/46aaa562-a9fa-4634-9bc1-4621240a57bd)

На этой диаграмме объектов представлена структура данных для музыкального плеера. 

1. Объект **Playlist** содержит список треков (track_list), каждый из которых представлен объектом **Track**. В **Track** хранится информация о названии песни (title) и длительности трека в секундах (duration).

2. Объект **Player** имеет связь с объектами **Playlist** и **Track**, что позволяет ему управлять воспроизведением музыкальных треков. Имеются также поля current_track, который указывает на текущий воспроизводимый трек, и is_playing, значение которого true если трек играет.
3. Объект **Controls** содержит набор кнопок, которые могут управлять плеером: "Play" (воспроизведение), "Pause" (пауза), "Stop" (остановка), "Forward" (перемотка вперед), "Backward" (перемотка назад), "Mute" (выключить звук) и "Unmute" (включить звук).

Эта диаграмма позволяет лучше понять структуру объектов и их взаимосвязи в музыкальном плеере.