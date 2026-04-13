# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  

### App Name: Melody Match



---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

Melody Match is designed to suggest songs that match a listener's mood, preferred genre, energy level, and acoustic taste — giving you a short, personalized playlist from a curated catalog. It assumes users can describe their current vibe in simple terms (e.g., "chill and acoustic" or "intense and high-energy") rather than needing a listening history or account. This project is built for classroom exploration, meaning it's a working simulation of how real streaming platforms think about recommendations — not a production app. It's meant to help students and curious learners see the tradeoffs behind even a small, rule-based system.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Melody Match looks at four things for every song in the catalog: its genre, mood, energy level, and whether it's acoustic or not. It compares those song traits against what the user told it they want — their favorite genre, current mood, how high-energy they're feeling, and whether they like acoustic music. Each of those four comparisons gets a score, and genre match counts the most (35%), followed by energy (30%), mood (20%), and acousticness (15%), so the final ranking reflects what matters most to most listeners. One key upgrade from the starter version is that genre and mood comparisons aren't just exact matches — for example, "pop" and "indie pop" are treated as similar rather than completely different, which gives the results a more natural feel.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog contains 25 songs spanning 15 genres — including pop, lofi, rock, jazz, hip-hop, EDM, classical, folk, blues, reggae, soul, and more — and moods ranging from happy and chill to melancholic, angry, and euphoric. Five sad/melancholic EDM songs were added to the original dataset to better support users with high-energy but emotionally heavy preferences. However, most genres outside of EDM have only one or two songs, so listeners who favor folk, blues, country, classical, or jazz will quickly exhaust good matches. Emotional nuances like "romantic," "nostalgic," and "soulful" are also present in the data but have no close mood neighbors in the scoring system, meaning those feelings aren't well supported.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works best for users with clear, common taste profiles — someone who wants chill lofi, high-energy pop, or intense rock will almost always get a top-5 list that actually makes sense. The weighted scoring captures the intuition that genre is the strongest signal: when a user's genre matches exactly, those songs consistently rise to the top regardless of small energy or mood differences. Soft-matching also helps in adjacent cases — a pop fan gets reasonable indie pop results rather than a blank, which mirrors how most people actually listen. Overall, the more mainstream and well-represented a user's taste is in the catalog, the more the recommendations feel natural and intentional.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The recommender puts a lot of  weight on energy level, so a song can get pushed down in the results simply because it's louder or quieter than expected — even if the mood and genre are a perfect match. 

Many genres like folk, blues, country, and classical have only one song in the catalog, so listeners of those styles quickly run out of good matches and get handed random songs that don't fit their taste. 

The system also treats acousticness as a yes-or-no switch, which means non-acoustic listeners will almost never see entire genre families like jazz, folk, or classical — even when those songs match in every other way. 

Finally, feelings like "romantic," "nostalgic," and "soulful" have no similar moods in the system, so a user who wants that vibe ends up ranked by technicalities like tempo and acousticness instead of anything emotionally relevant.


---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested a range of user profiles — from straightforward ones like a chill lofi listener to more unusual ones like a sad EDM fan who wanted high-energy but emotionally heavy music. I looked at whether the top 5 results actually matched the mood and genre I asked for, or if the system was just picking songs with similar energy levels by coincidence. The most surprising finding was that "obvious" profiles like pop or lofi worked well, but edge cases like a sad raver exposed how the system still breaks down when genre and mood point in opposite directions — revealing that the recommender is only as good as its most common user.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

The most impactful next step would be expanding the catalog — especially for underrepresented genres like folk, blues, and classical — so that niche listeners actually get meaningful choices instead of near-random fallbacks. Adding features like tempo preference and danceability to the user profile would also help the system distinguish between, say, a user who wants chill background music versus one who wants something to move to. To improve diversity, a re-ranking step could be added to ensure the top 5 results don't all come from the same genre or artist, which is a common issue when one category dominates the scores. Finally, supporting blended tastes — like "mostly chill but occasionally energetic" — would make the system feel much more like how people actually listen to music.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this project gave me a clearer picture of how high-production apps like Spotify approach recommendations — through techniques like content-based filtering (matching song traits to user preferences) and collaborative filtering (learning from what similar users enjoy). What surprised me most was how closely genre and energy function as scoring signals: they tend to dominate the results together, while mood and acousticness play more of a tiebreaker role. I also realized that there's no single perfect formula — every change you make to the weights or features creates a new tradeoff, helping some users while hurting others. That made me appreciate how much engineering and experimentation goes into the recommendation systems we interact with every day without thinking twice.

**Reflection from Phase 5:**

My biggest learning moment was testing the sad EDM profile — I expected the system to struggle but I didn't realize how badly genre would override mood until I actually saw the results, and that's when it clicked that the formula doesn't think, it just scores. AI tools helped me move a lot faster on writing and structuring the code, but I still had to double-check the song scores manually because the AI would sometimes explain logic that sounded right but didn't match what the numbers were actually doing. The most surprising thing was how even a basic weighted formula can feel like a real recommendation when the inputs are clean — a chill lofi profile would return results that genuinely felt curated, even though the system had no idea what music actually sounds like. If I extended this project I'd want to try collaborative filtering so the system could learn from patterns across multiple users instead of just matching one person's traits to song features.
