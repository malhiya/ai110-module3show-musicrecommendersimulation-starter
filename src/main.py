"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Taste profile — weights: genre(0.35), energy(0.30), mood(0.20), acoustic(0.15)
    user_prefs = {
        "genre": "pop",          # genre_match  × 0.35
        "mood": "happy",         # mood_match   × 0.20
        "energy": 0.8,           # energy_score × 0.30  (0.0–1.0)
        "likes_acoustic": False, # acoustic_score × 0.15 (False = prefers low acousticness)
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  TOP RECOMMENDATIONS")
    print("=" * 50)
    for i, rec in enumerate(recommendations, start=1):
        song, score, reasons = rec
        # bar = "#" * round(score * 20)
        print(f"\n  #{i}  {song['title']}  —  {song['artist']}")
        print(f"       Genre: {song['genre']}  |  Mood: {song['mood']}")
        print(f"       Score: {score * 100:.0f}/100 ") #[{bar:<20}]
        print("       Why this song?")
        for reason in reasons:
            print(f"         • {reason}")
    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
