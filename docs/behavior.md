# Поведенческие модели

## Диаграммы состояний

Предоставляю диаграммы состояний в формате PlantUML с соответствующими описаниями для каждого состояния и перехода. Эти диаграммы помогут глубже понять структуру и логику работы вашего музыкального приложения на Python.

### 1. Диаграмма состояний приложения (PlayerApp)
Эта диаграмма отображает жизненный цикл главного приложения, начиная с инициализации и заканчивая состояниями воспроизведения, паузы и остановки треков.


![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/8de1d273-dd8e-47e8-bf67-ede4799f7756)


### Описание состояний:

- **Инициализация**: Начальное состояние приложения, где создаются все GUI-компоненты и инициализируется `Player`.
- **Ожидание загрузки каталога**: Состояние ожидания выбора пользователем каталога с аудиофайлами.
- **Каталог загружен**: Состояние после успешной загрузки и отображения треков в списке воспроизведения.
- **Трек выбран**: Пользователь выбирает трек из списка для воспроизведения.
- **Трек играет**: Состояние воспроизведения выбранного трека.
- **Трек на паузе**: Воспроизведение трека приостановлено.
- **Трек остановлен**: Воспроизведение трека остановлено.

### 2. Диаграмма состояний плеера (Player)
Эта диаграмма иллюстрирует состояния и переходы, связанные с загрузкой и воспроизведением треков в компоненте `Player`.

![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/a934ea07-2375-4302-bceb-34d7da2486f6)


### Описание состояний:

- **Инициализация**: Инициализация объекта `Player` и библиотеки `pygame.mixer`.
- **Треки загружены**: Состояние после загрузки треков в плеер.
- **Трек играет**: Воспроизведение текущего трека.
- **Трек на паузе**: Воспроизведение текущего трека приостановлено.
- **Трек остановлен**: Воспроизведение трека полностью остановлено.

### 3. Диаграмма состояний трека (Track)
Эта диаграмма представляет состояние для отдельного трека в приложении.

![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/a35d11e5-29ac-4180-9201-48dced4113cf)


### Описание состояний:

- **Загружен**: Трек доступен для воспроизведения в плеере после загрузки из указанного каталога.

Эти диаграммы помогут вам четко понимать, как ваше приложение и его компоненты взаимодействуют друг с другом, а также какие состояния и переходы возможны в процессе их работы.


## Диаграмма последовательностей

Для создания диаграммы последовательностей в формате PlantUML, давайте рассмотрим основной поток взаимодействий между пользователем и компонентами приложения. В этой диаграмме мы будем демонстрировать процесс, начиная с загрузки каталога с треками и до воспроизведения трека.

![image](https://github.com/drdSchwarzenMagie/igaveup/assets/159145295/bf54396b-5754-44bc-a579-aaec075be70d)


### Объяснение шагов:

1. **Загрузка каталога**:
    - Пользователь вызывает метод `load_directory()` в `PlayerApp`.
    - `PlayerApp` вызывает диалоговое окно `filedialog.askdirectory()` для выбора каталога.
    - После выбора каталога, `PlayerApp` передает путь к каталогу в метод `load_tracks()` объекта `Player`.
    - `Player` читает файлы в каталоге, проверяет их доступность и загружает треки, обновляя свой `track_list`.
    - `PlayerApp` обновляет GUI с новым списком треков.

2. **Выбор трека и воспроизведение**:
    - Пользователь выбирает трек из списка, вызывая метод `select_track()` в `PlayerApp`.
    - `PlayerApp` вызывает метод `play_track()` в `Player` с индексом выбранного трека.
    - `Player` загружает и начинает воспроизведение трека с использованием `pygame.mixer.music`.
    - `PlayerApp` обновляет GUI, отображая текущий воспроизводимый трек.

3. **Воспроизведение и пауза**:
    - Пользователь нажимает кнопку "Play", вызывая метод `play_track()` в `PlayerApp`, который передает управление `Player`.
    - Пользователь нажимает кнопку "Pause", вызывая метод `pause_track()` в `PlayerApp`, который передает управление `Player` для паузы или возобновления воспроизведения.

4. **Переключение треков**:
    - Пользователь нажимает кнопку "Next", вызывая метод `next_track()` в `PlayerApp`, который передает управление `Player`.
    - `Player` переходит к следующему треку и начинает его воспроизведение, обновляя текущий индекс трека.
    - Пользователь нажимает кнопку "Previous", вызывая метод `prev_track()` в `PlayerApp`, который передает управление `Player`.
    - `Player` переходит к предыдущему треку и начинает его воспроизведение, обновляя текущий индекс трека.

Эта диаграмма последовательностей иллюстрирует взаимодействие между пользователем, `PlayerApp`, `Player`, и `pygame.mixer` для загрузки и управления воспроизведением треков.