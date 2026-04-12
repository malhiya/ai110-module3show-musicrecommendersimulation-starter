from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

GENRE_SIMILARITY: Dict[Tuple[str, str], float] = {
    ("pop", "indie pop"):    0.6,
    ("pop", "synthwave"):    0.4,
    ("pop", "r&b"):          0.3,
    ("lofi", "ambient"):     0.6,
    ("lofi", "jazz"):        0.4,
    ("rock", "metal"):       0.6,
    ("rock", "punk"):        0.5,
}

MOOD_SIMILARITY: Dict[Tuple[str, str], float] = {
    ("happy", "euphoric"):    0.7,
    ("happy", "uplifting"):   0.6,
    ("chill", "relaxed"):     0.7,
    ("chill", "peaceful"):    0.6,
    ("chill", "focused"):     0.5,
    ("intense", "energetic"): 0.7,
    ("intense", "angry"):     0.5,
}

def genre_match(user_genre: str, song_genre: str) -> float:
    """Return a 0.0–1.0 similarity score between two genres using the soft-match table."""
    if user_genre == song_genre:
        return 1.0
    key = (user_genre, song_genre)
    return GENRE_SIMILARITY.get(key, GENRE_SIMILARITY.get((song_genre, user_genre), 0.0))

def mood_match(user_mood: str, song_mood: str) -> float:
    """Return a 0.0–1.0 similarity score between two moods using the soft-match table."""
    if user_mood == song_mood:
        return 1.0
    key = (user_mood, song_mood)
    return MOOD_SIMILARITY.get(key, MOOD_SIMILARITY.get((song_mood, user_mood), 0.0))

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences; return (0.0–1.0 score, list of weighted reason strings)."""
    g_score = genre_match(user_prefs["genre"], song["genre"])
    m_score = mood_match(user_prefs["mood"], song["mood"])
    e_score = 1 - abs(user_prefs["energy"] - song["energy"])
    a_score = song["acousticness"] if user_prefs["likes_acoustic"] else (1 - song["acousticness"])

    score = g_score * 0.35 + e_score * 0.30 + m_score * 0.20 + a_score * 0.15

    reasons = [
        f"genre match    ({g_score * 35:.0f}/35 pts)",
        f"energy match   ({e_score * 30:.0f}/30 pts)",
        f"mood match     ({m_score * 20:.0f}/20 pts)",
        f"acoustic match ({a_score * 15:.0f}/15 pts)",
    ]
    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, List[str]]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Beginner-friendly version:
    # scored = []
    # for song in songs:
    #     score, explanation = score_song(user_prefs, song)
    #     scored.append((song, score, explanation))
    # scored.sort(key=lambda x: x[1], reverse=True)
    # return scored[:k]

    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]







# Data Flow: Input → Process → Output
#
# flowchart TD
#     A([songs.csv]) --> B["load_songs()\nparse rows → List[Dict]"]
#     U([user_prefs\ngenre · mood · energy · likes_acoustic])
#
#     B --> C
#     U --> C
#
#     C["recommend_songs(user_prefs, songs, k=5)"]
#     C --> D
#
#     subgraph LOOP ["For each song in songs (20 total)"]
#         D["Pick next song\n{ title, genre, mood, energy, acousticness }"]
#         D --> S1["genre_match(user_genre, song_genre)\n× 0.35"]
#         D --> S2["mood_match(user_mood, song_mood)\n× 0.20"]
#         D --> S3["1 - |user_energy - song_energy|\n× 0.30"]
#         D --> S4["acousticness or 1-acousticness\n× 0.15"]
#         S1 & S2 & S3 & S4 --> SUM["total_score = sum of weighted sub-scores\n(0.0 - 1.0)"]
#         SUM --> APP["append (song, score, explanation)\nto scored[ ]"]
#         APP --> MORE{More songs?}
#         MORE -- Yes --> D
#     end
#
#     MORE -- No --> SORT["sort scored[ ] by score descending"]
#     SORT --> SLICE["return scored[:k]"]
#     SLICE --> OUT["main.py prints\ntitle · score · explanation"]
