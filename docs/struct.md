### Диаграмма классов (Class Diagram) приложения

@startuml

class Player {
    - playlist: List<Track>
    - currentTrackIndex: int
    - isPlaying: boolean
    - isPaused: boolean
    + play(): void
    + pause(): void
    + stop(): void
    + nextTrack(): void
    + previousTrack(): void
    + mute(): void
    + unmute(): void
}

class Track {
    - title: string
    - artist: string
    - duration: int
    + getTitle(): string
    + getArtist(): string
    + getDuration(): int
}

Player "1" *-- "*" Track : contains

@enduml
Описание:

- Player: Класс, представляющий плеер. Содержит список треков плейлиста, индекс текущего трека, флаги для отслеживания состояния воспроизведения (воспроизведение, пауза), а также методы для управления воспроизведением (play, pause, stop, nextTrack, previousTrack, mute, unmute).
- Track: Класс, представляющий трек. Содержит информацию о названии, исполнителе и длительности трека, а также методы для получения этой информации (getTitle, getArtist, getDuration).

### Диаграмма объектов (Object Diagram)

@startuml

object player
object track1
object track2

player : Player
track1 : Track
track2 : Track

player "1" *-- "1..*" track : contains

@enduml
Описание:

- player: Объект класса Player, представляющий плеер.
- track1, track2: Объекты класса Track, представляющие треки в плейлисте.
- Связь "player contains track": Плеер содержит один или несколько треков в плейлисте.
