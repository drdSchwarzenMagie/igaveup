# Поведенческие модели

---
## Диаграмма состояний
![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/3545475a-f583-4c5b-b909-e57ce0afb5e6)

1. Idle:
   - Начальное состояние.
   - Переходы:
     - Press Close: переход в состояние Close.
     - Chose Directory: переход в состояние Loading_Playlist.

2. Close:
   - Состояние закрытия плеера.
   - Переходы:
     - [Press Close]: возвращение к состоянию начальной точки [*].

3. Loading_Playlist:
   - Состояние загрузки плейлиста.
   - Переходы:
     - Press Play: переход в состояние Player.

4. Player (составное состояние):
   - Содержит под-состояния и управление воспроизведением.

5. Player включает следующие состояния:
   - Playing:
     - Переходы:
       - Press Pause: переход в состояние Paused.
       - Press Stop: переход в состояние Stopped.
       - Press Next: переход в состояние Next_Track_Playing.
       - Press Prev: переход в состояние Prev_Track_Playing.
   
   - Paused:
     - Переходы:
       - Press Play: возвращение в состояние Playing.
       - Press Stop: переход в состояние Stopped.
       - Press Next: переход в состояние Next_Track_Playing.
       - Press Prev: переход в состояние Prev_Track_Playing.

   - Stopped:
     - Переходы:
       - Press Play: возвращение в состояние Playing.

6. Control_Playing (составное состояние внутри Player):
   - Управляет переходами между треками.
   - Paused и Playing могут переходить в Next_Track_Playing и Prev_Track_Playing при нажатии соответствующих кнопок.

7. Player также включает переход:
   - Press Close: переход в состояние Close.
