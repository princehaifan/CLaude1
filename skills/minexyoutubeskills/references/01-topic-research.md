# Stage 1 — Topic research

> Part of **minexyoutubeskills**. Find What if science topics with proven, repeated demand and pick the best ones for the requested format. Load this file when the user has no topic yet, or asks which topics perform.

## Goal

Return a small, ranked shortlist (default **3 topics**, or **10** when the user asks for ten). Each topic needs evidence that it worked **for more than one creator, more than once**, plus a sign that it still has current interest. Never present a topic because it "sounds viral".

## Be honest about the numbers first

- Single science "What if" videos almost never reach 1 billion views. Billion-view scale usually exists only at **series or channel level**, such as a whole "What If" series. If the user asks for "1 billion views per topic", say so plainly. Then redefine the evidence as "the same topic performing again and again across creators".
- Third-party trackers (Rosetta, OutlierKit, vidIQ mirrors) give stale or conflicting snapshots. Label them approximate and prefer live data from a scraper.
- Lifetime views alone do not prove current demand. Compare each video with its own channel (views ÷ subscribers). A **small channel with huge views is the strongest demand signal**. Example from this skill's first run: a 3.4K-subscriber channel with a 5.6M-view Apophis video uploaded the month before the research.

## Sources to check (in this order)

1. **Higgsfield / Everygen Content Factory catalog**, the "most viewed and liked" in-house evidence.
   - `list_content_factory_references` (viewmax/Everygen connector) returns every reference style with `views`, `likes` and duration. Rank by views, then by **likes per 100 views** (engagement).
   - The topic of each style is hidden in its kit. Call `get_content_factory_template` (`style:<id>`) and then `get_video_kit` (`kitId`). The result is large, so grep it for `"default":"What if…` title slots. For example, `gas-giant` = "What if you fell into Jupiter?" and `lowpoly-skyline` = "What if all humans disappeared?".
   - Higgsfield's own `/content-factory` instructions (`get_preset_instructions`) list the What If styles with `preset_id`s. They show what can be made, not views.
   - The catalog shows reach of those reference videos, not why they worked. Never claim a style caused views.
2. **YouTube, live**, through Apify (cheap, cents per run). See `tool-notes.md` for exact inputs.
   - Search 2–3 phrasings of the topic, sorted by popularity. Keep views, likes, publish date, duration and channel subscribers.
   - Keep long videos and Shorts separate.
3. **Web search** for cross-creator repeats (Kurzgesagt, Vsauce, Veritasium, What If, xkcd What If, etc.) and for current hooks: this month's science news, upcoming real dates (flybys, launches, eclipses), anniversaries.
4. **Short-form trend roundups** are weak evidence (marketing blogs with unclear methods). Use them only as a supporting signal and say so.

## Scoring a candidate

| Signal | Strong evidence |
|---|---|
| Repeated across creators | 3+ independent creators with multi-million views on the same premise |
| Outlier performance | views ÷ subscribers far above the channel's norm |
| Engagement | high likes per 100 views (Content Factory and YouTube) |
| Current hook | a real date, fresh news, or a recent outlier upload |
| Fit for the format | a clear visual first consequence; can be answered in the target length |

Drop a topic if the science cannot honestly answer it, if the visuals would need real victims or real tragedy, or if the only evidence is one video.

## Deliverable format

For each pick:
- **Title-style premise** ("What if … ?")
- **Proof**: 2–4 bullet facts with numbers and linked sources (creator, title, views, date)
- **Why it works at this length**: the built-in structure (countdown, journey inward, timeline)
- **Current hook**, if any

Then add a short **"What I couldn't measure"** list: data that wasn't accessible, stale trackers, and anything that needs a paid scraper run. If a paid run would help, offer it with its cost; don't silently skip it.

End with a recommendation and an offer to move to Stage 2 (script).
