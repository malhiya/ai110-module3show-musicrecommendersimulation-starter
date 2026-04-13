"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


PROFILES = [
    {
        "name": "Jazz Café Acoustic",
        "genre": "jazz",
        "mood": "relaxed",
        "energy": 0.37,
        "likes_acoustic": True,
    },
    {
        "name": "Euphoric EDM",
        "genre": "edm",
        "mood": "euphoric",
        "energy": 0.96,
        "likes_acoustic": False,
    },
    {
        "name": "Ambient Meditation",
        "genre": "ambient",
        "mood": "chill",
        "energy": 0.28,
        "likes_acoustic": True,
    },
    {
        "name": "Peaceful Metalhead (Edge Case)",
        "genre": "metal",
        "mood": "peaceful",
        "energy": 0.2,
        "likes_acoustic": True,
    },
    {
        "name": "Sad Raver (Edge Case)",
        "genre": "edm",
        "mood": "sad",
        "energy": 0.9,
        "likes_acoustic": False,
    },
]


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile in PROFILES:
        user_prefs = {k: v for k, v in profile.items() if k != "name"}
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 50)
        print(f"  TOP RECOMMENDATIONS — {profile['name']}")
        print("=" * 50)
        for i, rec in enumerate(recommendations, start=1):
            song, score, reasons = rec
            print(f"\n  #{i}  {song['title']}  —  {song['artist']}")
            print(f"       Genre: {song['genre']}  |  Mood: {song['mood']}")
            print(f"       Score: {score * 100:.0f}/100")
            print("       Why this song?")
            for reason in reasons:
                print(f"         • {reason}")
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
