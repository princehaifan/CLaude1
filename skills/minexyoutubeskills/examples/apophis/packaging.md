# YouTube packaging — "What if Apophis hit Earth?"

**Video:** 5:00, 16:9, a realistic simulated documentary (hypothetical premise)
**Viewer:** science-curious general audience. They have heard "the 2029 asteroid" in the news, half-fear it, and don't trust official reassurance.
**Core promise:** an honest, realistic answer to *how bad an Apophis impact would actually be*: a regional catastrophe, not an extinction. Also why we would know years ahead.
**What the first 30 seconds deliver:** the impact seen from orbit, the real 13 April 2029 date, the Eiffel-Tower scale comparison, and the statement "In real life, it misses."

Status: **concepts and generation prompts only.** No thumbnail has been generated yet (Higgsfield balance is 0 credits; about 4.25 credits per 4K image).

---

## Three title + thumbnail pairs

### A · Consequence: "The moment before"
- **Title:** What If Apophis Hit Earth? A Realistic Simulation
- **Thumbnail scene:** dawn over a European city seen from a hill. Apophis glows just above the horizon with a short white-hot plasma trail, a split second before impact.
- **Overlay text:** `FRIDAY THE 13TH`
- **Hypothesis tested:** an imminent, believable consequence plus a real (and eerie) date makes viewers click to see the outcome.
- **Payoff in the video:** the opening is the impact itself; the body shows exactly what happens next.

### B · Scale: "Familiar anchor"
- **Title:** What an Eiffel Tower–Sized Asteroid Would Actually Do to Earth
- **Thumbnail scene:** the peanut-shaped asteroid stands on end beside the Eiffel Tower on an empty plain, roughly the same height, in hard late-afternoon light.
- **Overlay text:** `≈1,000 MEGATONS`
- **Hypothesis tested:** an exact, understandable size plus one big number creates curiosity about the real effects, beyond doom.
- **Payoff in the video:** the scale comparison at 0:06, then the energy, crater and blast estimates, all labelled as estimates.

### C · Near miss: "One variable changed"
- **Title:** Apophis Will Barely Miss Us in 2029. What If It Didn't?
- **Thumbnail scene:** Earth from high orbit with a ring of satellites. Apophis in the foreground follows a green path that slips just past Earth; a single red dotted line peels off and hits.
- **Overlay text:** `CLOSER THAN SATELLITES`
- **Hypothesis tested:** a surprising true fact (the real near miss) plus a counterfactual pulls in viewers who want facts before drama.
- **Payoff in the video:** 0:12–0:34 shows the real path, then the hypothetical one.

**Recommended starting pair: A.** The thumbnail matches the video's actual opening shot, so the click promise is paid in the first five seconds, and the title keeps the hypothetical framing explicit. This is a creative judgment, not a measured result.

**If you run YouTube's Test & Compare:** test the three pairs as complete title + thumbnail combinations, since each tests a different reason to click. The test measures watch-time share, so let it run to a result and accept "inconclusive" if that's what it says.

---

## Image generation prompts

Settings for all three: `generate_image` · `gpt_image_2_6` · 16:9 · `4k` · `3840x2160` · `quality: high` · PNG · `count: 1`, one call per concept. Each prompt includes the overlay text. If the generated lettering is imperfect, add the overlay in an editor instead using the exact text above.

**A · prompt**
```
Photorealistic cinematic YouTube thumbnail, 16:9. Dawn seen from a grassy hilltop overlooking a European city skyline in the midground, rooftops and church spires in cool blue shadow. Just above the horizon, slightly right of centre, a large dark peanut-shaped asteroid glows white-hot on its leading face, wrapped in a short brilliant plasma trail streaking down from upper left — the instant before impact. The sky near the asteroid burns amber-orange; the rest of the sky stays deep steel blue, creating strong orange-versus-blue separation. One dominant focal point: the glowing asteroid. Clean empty sky in the upper-left third for text. In that area, bold white condensed sans-serif text reading exactly "FRIDAY THE 13TH" with a thin dark outline. Small subtle label "SIMULATION" in the top-right corner. Nothing important in the lower-right corner. Realistic lighting, fine film grain, high detail, no people's faces, no logos.
```

**B · prompt**
```
Photorealistic YouTube thumbnail, 16:9. A vast flat empty plain under a clear pale sky in hard late-afternoon sunlight from the left. On the left third stands the Eiffel Tower, accurate iron lattice, warm-lit. On the right half, a grey-brown stony asteroid shaped like a lumpy peanut stands upright on the ground, almost exactly the same height as the tower, cratered surface with boulders and long raking shadows; both cast long shadows toward the right. Tiny cars on a road at the base show human scale. The two objects are clearly separated with open sky between them. Upper-centre area kept clear for text: bold white condensed sans-serif text reading exactly "≈1,000 MEGATONS" with the number in bright orange. Small subtle label "SIMULATION" in the top-left corner. Nothing important in the lower-right corner. Crisp, high contrast, realistic, no logos.
```

**C · prompt**
```
Photorealistic space YouTube thumbnail, 16:9. Earth fills the right half of the frame from high orbit, sunlit blue oceans and white clouds with a thin glowing atmosphere. A faint ring of tiny satellites circles Earth. In the left foreground, a dark peanut-shaped asteroid lit hard by the sun from the left, sharply detailed. A clean glowing green dashed trajectory line runs from the asteroid past Earth, slipping just inside the satellite ring and missing the planet; a single bright red dotted line branches off the green path and curves into Earth's surface. Black starry space background. Upper-left area kept clear for text: bold white condensed sans-serif text reading exactly "CLOSER THAN SATELLITES". Small subtle label "SIMULATION" under the text. Nothing important in the lower-right corner. Realistic, high contrast, no logos.
```

Checks after generation:
- exact spelling of the overlay
- readable at a small mobile preview
- a single focal point
- Eiffel Tower and asteroid roughly equal height (B)
- red and green lines readable (C)
- nothing in the lower-right timestamp zone

---

## Upload copy

### Description
```
What if asteroid Apophis didn't miss? On Friday, April 13, 2029, this 340-metre space rock will pass closer to Earth than many of our satellites. In real life it misses — NASA has ruled out any impact for at least the next 100 years. In this realistic simulation, we take away the miss and follow what would happen, from atmospheric entry to the blast zone.

You'll learn:
• how much energy a 340-metre asteroid releases (and why it's an estimate)
• how big the crater and blast zone would be
• whether an ocean impact would really cause a giant tsunami
• why Apophis is not a "dinosaur killer"
• how anyone can check an asteroid's path — and what happened with 2024 YR4

All impact scenes are computer-generated simulations of a hypothetical event. Damage figures are model estimates based on published impact-effect equations (Collins, Melosh & Marcus, 2005).

And on April 13, 2029: if you're in Europe, Africa or western Asia, look up.

SOURCES
NASA – Apophis facts: https://science.nasa.gov/solar-system/asteroids/apophis-facts/
The Planetary Society – Will Apophis hit Earth?: https://www.planetary.org/articles/will-apophis-hit-earth
Ocean-impact tsunami simulations: https://www.space.com/36451-asteroids-bad-at-making-waves.html
NASA – Asteroid impact simulations (Robertson et al.): https://ntrs.nasa.gov/api/citations/20170005214/downloads/20170005214.pdf
National Academies – NEO hazard thresholds: https://www.nationalacademies.org/read/25476/chapter/3
2024 YR4 impact odds: https://sciencedaily.com/releases/2025/02/250225122436.htm
DART changes Dimorphos's orbit (JHU APL): https://www.jhuapl.edu/PressRelease/221011-dart-mission-impact-changed-asteroids-motion-in-space

[CHANNEL LINKS — placeholder]
```

### Chapters (names only)
Add timestamps only after checking them against the finished edit. The first chapter must start at 0:00.
1. What if Apophis didn't miss?
2. The rules of the experiment
3. Entering the atmosphere
4. The impact
5. Crater and blast zone
6. What if it hit the ocean?
7. Is it a dinosaur killer?
8. Would anyone tell us?
9. The real answer

### Tags
```
Apophis, asteroid Apophis, 99942 Apophis, Apophis 2029, asteroid impact, asteroid impact simulation, what if asteroid hit earth, what if, near-Earth asteroid, planetary defense, DART mission, 2024 YR4, Friday the 13th asteroid, space science, science documentary
```

### Pinned comment (optional)
This answers the top question in the comment research ("would they even tell us?") and invites discussion.
```
"If it were really going to hit, would they tell us?" — Apophis's orbit isn't secret. Astronomers worldwide (amateurs too) send measurements to the Minor Planet Center, and teams in the US and Italy compute the path separately. You can look it up yourself in NASA JPL's Small-Body Database. Where would YOU watch the 2029 flyby from?
```

### Disclosure note (review during upload)
The video contains realistic AI-generated scenes of an event that never happened (an asteroid impact). When uploading, review YouTube Studio's altered or synthetic content question and answer it for these scenes. Keep the on-screen "SIMULATION" tags and the description line about simulations either way.
