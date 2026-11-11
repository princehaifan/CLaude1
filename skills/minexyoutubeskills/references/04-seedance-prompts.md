# Stage 4a — Seedance 2.5 scene prompts

> Part of **minexyoutubeskills**. Write cinematic Seedance 2.5 prompts and run Seedance generation at 1080p when explicitly requested. Load this file only when SKILL.md routes you to this stage. Where this file names companion skills (faceless script, Seedance prompts, faceless production, YouTube packaging), they are the other stage files in this folder.

Use the supplied directing system in [embedded original prompting core](#prompting-core) when writing a generation prompt. Preserve its scene construction, camera direction, lighting, continuity, timing and prompt blocks. The intake and tool rules below govern execution; the directing reference is not a substitute for the connected model's actual controls.

## Start with what the user already supplied

Read the current request and the approved conversation context. Keep the topic, format, language, duration, style, references and previous decisions. A correction to one shot does not reopen the whole questionnaire.

For a new video with a missing format, ask in English:

**Where will you post this video?**

- **YouTube long-form** — horizontal, 16:9.
- **Shorts / Reels / TikTok** — vertical, 9:16.
- **Instagram feed** — choose square or portrait next.

Use the host's actual interactive question tool when it supports clickable choices. Discover its name and schema from available tools; do not invent a button API or assume a Claude-specific tool exists. If an interactive tool is unavailable or disallowed in the current mode, ask the same question once as a compact numbered list. Do not claim plain text is clickable. Wait for the answer when it determines the output; silence is not a selection.

For Instagram feed only, offer **Square (1:1)** or **Portrait (4:5)**. The current Seedance route supports 1:1 but not native 4:5. For portrait feed, compose a supported 3:4 source with crop-safe framing and finish to 4:5 through an available editor. State this before generation; never label a 3:4 file as 4:5.

If the topic is missing, then ask:

**Do you already have a topic?**

- **I have a topic** — let the user enter it.
- **Suggest 10 topics** — research current examples and propose ten options.

Skip either question when the answer is already supplied. For a technique question, a prompt review, or a specific shot with enough information, answer directly. Do not ask for narrator gender. Use supplied voice directions only if the scene needs dialogue or narration.

## When the user asks for ten topics

Inspect the current Higgsfield Content Factory catalog through the connected read-only tools or authorized interface, and research relevant current and evergreen interest on the web. Use a focused sample across more than one source; do not claim to have analyzed the entire internet. Catalog styles show what can be made, not which topic is guaranteed to perform.

The current connector exposes the catalog in `get_preset_instructions` for `/content-factory`. This read does not request generation. If the user explicitly wants to browse the style gallery, follow its documented `get_presets` route and turn restrictions instead. Preserve any exact slash command they selected.

Return exactly ten distinct topic candidates, each with a clear question, a visible opening, a plausible payoff, and a short evidence note. Separate observed interest from your creative inference. If data is inaccessible, name the gap and offer clearly labeled ideas rather than invented metrics. Keep source evidence in the research response or private working notes; do not add other creators' identities, signature characters, copied scripts or downloaded assets to this skill.

Invite the user to choose a topic using the available choice interface, respecting its option limits; otherwise accept a number or a custom topic. Do not generate videos just because topics were requested.

## Write the requested level of prompt

- **One shot:** one standalone English prompt in a copyable code block, plus the actual generation settings outside it.
- **Several requested shots:** self-contained prompts with stable identity, light and prop anchors. Respect the requested count.
- **A complete video from one request:** give one consolidated MCP production brief containing the premise, full approved narration or script reference, visual direction, first shot, timing strategy, sound, captions, edit requirements and final delivery format. The production agent can break it into supported clips internally; do not make the reader paste thirty separate requests unless they asked for scene-by-scene control.

A five-minute brief is an instruction to coordinate and edit multiple generations. It is not a claim that one Seedance model call produces five minutes. Distinguish a new consolidated brief from the exact prompt of an already completed generation.

Use the original prompting core for the actual scene descriptions. Keep references scoped to what is present in each shot. Use only supplied or otherwise authorized assets and voices; study general visual technique without copying another creator's distinctive content or implying endorsement.

## Generation settings and capability boundaries

For video generation under this skill, use **Higgsfield → Seedance 2.5 → 1080p**. Default to **16:9 for YouTube long-form** and **9:16 for Shorts, Reels or TikTok**. Aspect ratio is not resolution: send `resolution: "1080p"` separately from `aspect_ratio`.

Read [embedded seedance tool routing](#seedance-tool-routing) before a real generation. It documents the observed route and what to recheck. Preserve the user's explicit model choice: do not silently fall back to a different video model or a lower resolution. If the requested route is unavailable, finish the prompt and explain the exact limitation.

Treat numerical FOV, speed, haze, Kelvin, cut timing and continuity locks in the directing core as creative instructions, not calibrated model controls or guaranteed results. A character image does not guarantee a stable voice; a generation prompt does not guarantee pixel-identical editing. Do not pad footage, repeat batches, or upload new assets automatically because the reference contains a generic example. Apply actual tool limits and the user's authorized scope first. Do not promise an unsupported resolution by writing it into the prose.

## Execute only when requested

Writing or reviewing a prompt does not authorize spending credits, uploading assets, or publishing. An explicit request to generate should proceed through the available Higgsfield tools and their current credit checks; do not stop at delivering a prompt when generation was requested and is possible.

Use returned job IDs to wait for completion, inspect the result, and make only justified scoped corrections. A transport timeout may mean a job was submitted: determine that job's status before retrying. Keep a usable result distinct from a queued task or an untested prompt.

**Content Factory is a separate route.** Its current What If workflow draws scenes in code and renders them; it is not a Seedance video model call. Do not execute it under a Seedance-only request or relabel its results as Seedance. If the user explicitly selects Content Factory, follow its actual recipe and preserve the distinction in the handoff.


---

<a id="prompting-core"></a>

## Embedded original prompting core

# Seedance 2.5 Prompt Writer

Turn scripts, scenes, and ideas into Seedance 2.5 prompts. Block, light, and pace each shot like a film.

**Output: always a single standalone prompt in a code block.**

---

## CORE PRINCIPLE: WRITE THE VISIBLE

The model reacts to what can be **seen and measured**, not to mood words.

Translate every abstraction into something observable.
- ❌ "tense scene" → ✅ "man freezes, slowly clenches his fist, light only from the side, half his face in shadow"
- ❌ "cool cinematic shot of a car, epic, fast" → ✅ "low tracking shot alongside the car as it powers through a wet curve, headlights glowing, spray off the tyres, hard buffeting camera shake"
- ❌ "make the movement more natural" → ✅ "the body undulates like a worm in the air with every wingbeat; right after surfacing it shakes its head like a dog shaking off water, the twist traveling down the neck as a spiral wave"

Write in plain, clear, instruction-style language. Fewer precise words beat many vague ones.

**Lean on what 2.5 does well** — write these confidently instead of avoiding them: true lens behavior (a real fisheye warps the near hand before the face), mirror and floor reflections, lit crowds where extras act, one light source keeping its rhythm across every cut, the camera as a physical object (a phone set on a rock wobbles then locks; a drone catches lens droplets and wake shake), and 30-second single takes that carry a full emotional arc.

Before generating, mentally "watch" the prompt as a viewer: is everything unambiguous, is the first frame non-empty, is it clear where the subject is and where it looks, where is the light coming from.

---

## WORKFLOW

1. **Read as a director.** Find the dramatic shape: where the scene turns, lands, breathes.
2. **Define continuity anchors.** Who is in frame, how they look, what they carry across cuts.
3. **Write the prompt** using the block structure below.
4. **Tag assets.** Tagging rules below.

If the idea is ambiguous, close the gaps in conversation first — blocking, angle, light, timing, character behavior, what is in the first frame, how it ends. The model fills any gap on its own, usually not the way intended.

---

## ASSET TAGGING

Reference image (`@tag`) sets **appearance and identity**. Text sets **what happens** and locks critical details. Both are required.

**Tag naming:**
- If the user specifies tags as `@tag_name`, use those.
- If no tags are specified, name them by load order of the supplied assets: `@image1 @image2 ...` for images, `@video1 @video2 ...` for videos, `@audio1 @audio2 ...` for audio.
- Otherwise follow the user's explicit instruction.

**Reference + text rule:** keep the character description minimal — long appearance text conflicts with the image and degrades it.

```
@TAG: age + role/build + current state + unique visible features + action-critical details + voice (only if it has a line). 100% matches the reference.
```

State critical details (small text, logos, color) in words even if they appear on the reference — the model can drop them.

**Voice lock (2.5):** Seedance 2.5 locks the voice together with the appearance in the character sheet. Reuse the same sheet reference across generations and the voice stays consistent — describe the voice once in the tag line, not in every prompt.

Never place an `@tag` in a shot where that object is not present; the model will try to force it into frame.

---

## CONTEXT ISOLATION

Each generation is a blank slate — **no memory of previous shots.** A prompt is a sealed single-shot document.

Do not carry in: scene numbers, script headings, summaries of prior scenes, unused tags/characters, "as above / continues" phrasing, or people and props from a previous line that are not needed in this shot.

---

## STYLE — DISTRIBUTED, NOT A PREFIX

There is **no separate style-prefix block at the top of the prompt.** Style is not one thing in one place — it is a set of aspects, and each aspect lives in the block that already governs it, where it is most effective and unambiguous. State the target look, never what to avoid; adapt every line to this specific scene.

Cover these aspects, each in its home block:

| Aspect | Lives in | What to write |
|--------|----------|---------------|
| Lighting | **LIGHTING** | source, direction, exposure, key/fill, haze for THIS scene |
| Color / grade | **COLOR GRADE** (own block if grade is strong, e.g. teal-cyan desaturated) or folded into **LOCATION** + **LIGHTING** for a naturalistic look | palette as material + light beam + role, never a flat list |
| Lens / optical character | **OPTICS** | FOV°, rectilinear/anamorphic, prime-lens character, motion-blur |
| Camera body / tonal character | **CAMERA** | tonal latitude, highlight roll-off, color science — as a look, not a model name |
| Skin / micro-realism | **PERFORMANCE** (or inside **ACTION**) | pore-level realism, capillary flush, living eyes, catch-lights, visible breath |
| Acting | **PERFORMANCE** (or inside **ACTION**) | micro-pauses, precise eye-line, restraint, muscle-level emotion |
| Physics realism | **PHYSICS** | gravity, inertia, mass, contact shadows, fluids, particles |
| Composition / blocking | **FIRST FRAME / BLOCKING** | framing rule for THIS scene; everyone moving from frame one |
| Continuity | **POSITIVE LOCKS** | characters, props, environment identical across cuts |
| Wardrobe | **WARDROBE** (own block when costume matters) | material + condition, scene-logical |
| Format / resolution / grain / fps / bitrate | **STYLE** + **OUTPUT SETTINGS** at the **end**, just before LOCKS | 8K, photoreal, anamorphic, fine grain, real-time vs slow-mo per segment |

**Placement principle:** descriptive style (light, color, optics, physics, acting) sits *inside the content block it describes*, in the body of the prompt. Technical/format style (resolution, grain, fps, bitrate, overall look reference) sits as a **suffix stack at the end** (`STYLE`, `OUTPUT SETTINGS`), right before `POSITIVE LOCKS`. Nothing style-related goes at the very top — the prompt still opens on `SCENE CONTEXT` and `ACTIVE REFERENCES`.

Use only the aspects the shot needs. A naturalistic single take may have no `COLOR GRADE`, `WARDROBE`, or `OUTPUT SETTINGS` block at all and fold those notes into LIGHTING and POSITIVE LOCKS. A graded, multi-segment piece earns the full suffix stack.

If the user supplies their own prefix or block text, use it verbatim.

---

## PROMPT STRUCTURE

Write blocks in this order. Logic: context and references first, then space and timing, then action and physics, then the descriptive-style blocks in their home positions, and a technical-style suffix at the end. Use only the blocks the shot needs; drop the rest.

```
SCENE CONTEXT
[1–2 sentences: what happens, where, when. Geo-positions of characters.]

ACTIVE REFERENCES
[@tag + minimal anchor of critical details + "100% matches the reference"]

LOCATION MAP
[Foreground / midground / background, where the camera is, where light comes from, movement paths. Naturalistic color can live here.]

FIRST FRAME / BLOCKING
[Who is where in the first frame: positions, orientation, gaze. Composition rule for this scene.]

FORMAT MODE
[Choose the level of control the shot needs:
 - Single continuous shot — "one continuous shot, the camera does not cut on its own."
 - Sequence of cuts, no timecodes — "CUT 1 … CUT 2 … CUT 3", described in order.
 - Timed multishot — explicit HARD CUTs at stated seconds.]

OPTICS
[Shot size + FOV per segment + lens/optical character. For multishot add "no drift mid-segment".]

CAMERA
[Operator behavior: height, distance, movement, focus. Camera-body tonal character as a look.]

ACTION
[Events at the precision the shot needs. Camera motion and subject motion stated separately.]

PERFORMANCE        (when acting matters)
[Acting + skin/micro-realism: muscle-level emotion, eye-line, catch-lights, breath, pore-level detail.]

PHYSICS
[Mass, inertia, contact, fluids, particles.]

LIGHTING
[Source, direction, exposure — priority block.]

COLOR GRADE        (when the grade is strong / stylized)
[Palette as material + light + role; grade character. Omit for naturalistic looks — fold color into LOCATION/LIGHTING.]

WARDROBE           (when costume matters)
[Material + condition, scene-logical.]

AUDIO
[Only the needed sound / line.]

STYLE              (technical-style suffix)
[Overall look in words, photoreal, format, grain — no director or equipment names.]

OUTPUT SETTINGS    (when format must be pinned)
[Aspect, anamorphic, real-time vs slow-mo per segment. Note: words like "8K" set detail intent, not output size.]

POSITIVE LOCKS
[Short fixers against likely failures, in positive form, restating critical info once. Continuity lives here.]
```

The descriptive-style blocks (PERFORMANCE, PHYSICS, LIGHTING, COLOR GRADE, WARDROBE) sit in the body next to what they govern. The technical-style blocks (STYLE, OUTPUT SETTINGS) form a short suffix stack just before POSITIVE LOCKS. Nothing style-related opens the prompt.

A **lock** is a short hard fixer placed next to what it protects, e.g. `"headlights stay glowing in every shot"`. Write densely where control matters, sparsely where it does not. Say each important thing once, clearly.

---

## CUTS AND TIMING

**Duration budget (2.5): one generation runs up to 30 seconds.** Plan the shot to use it — a full emotional arc, a 14-segment beat-cut music sequence, or one unbroken oner all fit in a single take. A 2-minute piece is 4 generations. When timing matters, state the total length and land every HARD CUT on a stated second.

Pick the precision the shot actually needs — these are points on a scale, not a binary:

- **Single shot (oner)** → "one continuous shot, the camera does not cut on its own."
- **Sequential cuts, no timecodes** → describe shots in order as `CUT 1 … CUT 2 … CUT 3`. Use when you want specific cuts but exact timing does not matter.
- **Timed multishot** → explicit HARD CUTs at stated seconds. Use when beats must land on a clock.
- **Freestyle b-roll** → do not lock cuts; let the model find angles.

When you specify cuts (timed or not), lock that the camera does not add its own: *"cuts only at the specified points, the camera does not cut on its own."*

**Timecode format** (only when timing matters):
```
0.0s to 1.0s — [description]
1.0s HARD CUT
1.0s to 3.0s — [description]
```

**Sequential format** (cuts without timecodes):
```
CUT 1 — [description]
CUT 2 — [description]
```

**Cut types:** `HARD CUT`, `SMASH CUT`, `MATCH CUT`, `INSERT CUT`, `REVERSE CUT`, `WHIP CUT`. Fades / crossfades only if explicitly requested.

Across internal cuts hold: same character set, same geometry, screen direction, gaze, light, wardrobe, prop state.

---

## DIRECTING

**Blocking.** State where each character stands, sits, moves; what their hands do; what sits between them. "She sits across from him at the diner booth, knees touching under the table" beats "they sit and talk."

**Pace.** Read the dramatic structure. Confession scene → air, held shots, beats of silence. Action → compression, short cuts. A reveal lands on one held close-up.

**Acting.** Translate emotion into concrete on-shot direction:
- ❌ "she looks sad" → ✅ "her eyes drop to the table, jaw tightens, she swallows once before answering"
- ❌ "he is angry" → ✅ "knuckles whiten on the glass, breath shortens, eyes never leave hers"

Restraint by default — a whisper out-acts a shout most of the time.

**Continuity** (hold in mind, do not write as a block): state carried forward (wet/dry/bloodied), appearance not drifting, emotional carry from the previous scene, one time-of-day and weather unless the location changes.

**Camera language.** Be concrete: FOV°, height, movement, motivation. Motivate every camera move.
- "Low-angle 18° dolly-in, slow push from waist to chest as she realizes."
- "Static 47° two-shot, eye-level, locked off — lets the silence sit."
- "Handheld 63°, follow from behind — camera lags half a beat."

---

## PROMPTING RULES

- **Positive only.** Describe what should happen, not what to avoid. ❌ "does not fall backward" → ✅ "stays upright, feet planted."
- **Speeds in km/h.** ❌ "fast/slow" → ✅ "moves at 40 km/h", "camera pans at 5 km/h."
- **Atmosphere in percent / meters.** ❌ "light fog" → ✅ "fog density 40%", "haze visible at 15 meters depth."
- **Atmosphere builds in steps across shots.** Shot 1: fog 20% → Shot 2: 40% → Shot 3: 60%.
- **Giant scale via human-height comparison.** ❌ "huge", "three meters tall" → ✅ "stands as tall as four humans stacked head to toe."
- **Left/right is from the camera.** "Subject moves left" = left from the camera's view.
- **Environment interaction stated physically.** Snow melts on skin, rain runs down hair, wind moves fabric.
- **Emotion through muscle movement, not labels.**

---

## OPTICS — SHOT SIZE, LENS, FOV

Two levers define "how it is shot": **shot size** and **focal length**.

### Shot sizes
| Abbr | Meaning | In frame |
|------|---------|----------|
| ECU | Extreme Close-Up | a detail: eyes, button, headlight, hand |
| CU | Close-Up | full face / one element large |
| MCU | Medium Close-Up | head and shoulders |
| MS | Medium Shot | roughly to the waist |
| WS | Wide Shot | full figure + surroundings |
| EWS | Extreme Wide | scale, location |

### Focal length (mm — for describing size while writing, not for the prompt text)
| Lens | Effect | Use for |
|------|--------|---------|
| 24–35mm wide | space, slight perspective distortion | action, immersion, wides |
| 50mm normal | natural perspective, "as the eye sees" | realism, neutral shots |
| 85mm portrait | soft bokeh, subject separated from background | portrait, emotion |
| 135mm+ tele | strong compression, "watching from afar" | observation, distance, sport |

In the prompt text use **FOV in degrees** from the table below, not millimeters.

### FOV anchor table (degrees for the prompt)
| FOV | mm equiv | Purpose | When |
|-----|----------|---------|------|
| 180° | Fisheye | spherical distortion | POV, dream-state |
| 107° | 14–16mm | architectural ultra-wide | huge interiors, epic establish |
| 84° | 20–24mm | wide | establish, group blocking |
| 63° | 28–35mm | observational | wide observation, reportage |
| 47° | 40–50mm | neutral human perspective | universal establish, medium |
| 29° | 75–85mm | portrait compression | medium-isolate, dialogue bust |
| 18° | 100–135mm | natural portrait | close-portrait, identity-preserving |
| 12° | 180–200mm | tele-detail | hands, objects, detail-on-wide |
| 8° | 300–400mm | extreme compression | observation, broadcast |

Use only the discrete steps from the table. Not "23°" — use 18° or 29°. In a multishot, set FOV per segment and add `"no drift mid-segment"`.

### Camera placement in the prompt
Place the CAMERA block in the **3rd position** of the prompt's core layers (subject → action → camera → style → constraints). Moved to the end, FOV gets ignored; moved to the front, it conflicts with identity.

---

## OPTICAL TECHNIQUES

**Observation pattern (hidden-camera effect)** — all three ingredients at once:
1. Foreground occlusion — out-of-focus obstruction over 20–30% of frame (wall, pillar, branch, arch).
2. Atmospheric haze — fog/dust/shimmer between camera and subject.
3. Distance vantage — super-tele 8°–12°, operator anchored far away.
Change the occlusion type between beats; keep the vantage single.

**Sports broadcast:** `8° super-tele + handheld 1–2cm tremor + "anchored at distance, finding the action"`.

**Detail-on-wide (snake cam):** `84° wide FOV + low-angle right up against a small object` — foreground object exaggerated, background recedes into depth.

**Intimate wide:** `63–84° wide FOV on a close face` — face centered, surroundings readable without blur.

**Tele compressed air column** at 8°–12°: `"dust suspended in the long compressed air column between camera and subject"`, `"heat shimmer compressed into a wall of haze in front of the figure"`.

---

## INPUT VIDEO — V2V AND I2V

**Video-to-video** (edit real footage: swap a character, add a creature, keep the plate):
- The source clip must be **at least 4 seconds long**. Shorter clip → freeze-frame the last shot to pad it.
- **Set the generation duration to match the reference** (usually 4s). Anything longer and the model starts guessing beyond the source.
- Tag the source `@video1` and declare it master: "master for camera, framing, focus, motion, expression timing, background, lighting, grain and duration." Then state the one edit and lock everything else ("every pixel outside the replaced subject remains exactly as in @video1").

**When v2v fails:** if the same defect shows up across all four batches, the problem is the prompt or the source — more batching only burns credits. Usual cause: the action you want has no anchor in the source (e.g. no jump moment to map onto). Switch to **image-to-video**: screenshot a frame of the location, use it as the starting frame, and write the action from scratch. Plan a deliberate **empty-frame pause** (1–2 seconds of just the location) where you intend to stitch takes in the edit — it becomes a clean cut point.

---

## SPECIAL PROTOCOLS

**4-mechanism multishot consistency stack (extreme FOV: 8°, 107°):**
1. Sequence-wide identity lock — single location reference across all beats.
2. LENS LOCK opener — explicit FOV phrase at the start of each beat.
3. LENS CHECK closer — confirm FOV at the end of the beat.
4. Color via material + light, not as a list.
All four are required, or extreme-FOV multishots break down after 2–3 beats.

**Whip-pan timing:**
```
0.3s — Subject A settled
0.8s — WHIP motion-blur transition
1.4s — Subject B settled
```
A whip under 0.8s renders as a hard cut without blur.

**Mixed time-speed (real-time + slow-mo):** hard cuts only between speed modes. Each shot is one speed start to finish.

**Cracks/breaks without impact (anti-impact lock):**
- "crowd PRESSES, not strikes"
- "fracture originates from edge stress, not center impact"
- "no impact point — pressure-based crack"
- sequential timing edge-to-center, not radial from a point.

---

## CAMERA / LIGHT / COLOR

**White balance** in Kelvin, set to the scene mood, fixed within a scene (3200K / 4000K / 5600K / 8500K).

**Equipment:** describe the look, not gear. No camera/film/lens model names — they get ignored or break complex moves.

**Color rule:** tie color to **material + light beam + compositional role**, never a flat list.
- ❌ "the woman wears red, the man wears blue"
- ✅ "crimson silk scarf catching the cold tungsten spill from the corridor"

**Background in layers:** state foreground / midground / background separately.

**Camera on the shadow side**, with a stated operator axis.

---

## CHECKLIST (before each prompt)

- All blocks in order: context and references first, then space/timing, then action/physics, then style in its home blocks, technical-style suffix last?
- Tags named per the tagging rule (`@tag_name`, or load-order `@image1`/`@video1`/`@audio1`, or user instruction)?
- `@tag` only in shots where the object is present?
- No style-prefix block at the top — prompt opens on SCENE CONTEXT / ACTIVE REFERENCES?
- Each style aspect placed in its home block (light→LIGHTING, color→COLOR GRADE or LOCATION, acting/skin→PERFORMANCE, format/grain→STYLE+OUTPUT SETTINGS suffix)?
- Style adapted to this scene (not generic)?
- Everything positive (no "does not X")?
- Speeds in km/h, atmosphere in %/meters, giants vs human height?
- Emotion through muscle movement, not labels?
- Left/right from the camera?
- FOV in degrees from the anchor table (not mm, not arbitrary)?
- CAMERA block in 3rd position?
- WB in Kelvin for the scene mood?
- Color via material + light + role, not a list?
- Camera on the shadow side, operator axis stated?
- Background in foreground/midground/background layers?
- Multishot: FOV per segment + "no drift mid-segment"; extreme FOV → all 4 consistency mechanisms?

---

## FINAL RULES

- **English prompts only.**
- **Positive phrasing only** — state the target, never the prohibition.
- **No director names, no signature-work references, no equipment names.**


---

<a id="seedance-tool-routing"></a>

## Embedded Seedance tool routing

# Seedance 2.5 through Higgsfield

This adapter was checked against the connected tool catalog on 2026-11-10. Tool names may carry a host namespace. Discover the available tools by their function and read the live schema before submitting; an example below does not register a tool.

## Verified route

1. Resolve `models_search` with query `Seedance 2.5`, output type `video`, or inspect `models_get` for the returned ID.
2. The observed model ID is `seedance_2_5`. It supports 4–30 whole seconds per generation and resolutions `480p`, `720p`, `1080p`. This skill selects `1080p`; do not use a draft mode that forces 480p.
3. Observed aspect ratios: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`. Select the explicit intended ratio. Do not send native 4:5 or assume the server's fallback is acceptable.
4. Use `generate_video` with all generation controls inside `params`. Use the connected `estimate_video_cost` when required for credit preflight; follow the returned choice/approval flow. Never substitute an ordinary batch endpoint for required cost or choice handling.
5. Before the first generation without an explicit destination, use `get_preferences` if exposed. Reuse this conversation's existing destination; create a project only when explicitly requested or the actual saved preference enables it.
6. A completed job and returned media are required before claiming generation. Use the documented status/wait tool; current `jobs_wait` accepts up to eight job IDs and a maximum 15-second poll. Respect its next-poll guidance and the generation tool's widget instructions.

Illustrative text-to-video call, after the prompt and duration are known:

```json
{
  "params": {
    "model": "seedance_2_5",
    "prompt": "The complete standalone scene prompt goes here.",
    "mode": "t2v",
    "resolution": "1080p",
    "aspect_ratio": "16:9",
    "duration": 10,
    "generate_audio": true,
    "bitrate_mode": "standard",
    "count": 1
  }
}
```

This is an input-shape example, not a ready scene or a submitted job. Replace the example prompt, duration, ratio and audio setting with the approved brief. Use the user's budget and audio plan; do not add a competing voice track to a separately narrated documentary.

## Reference inputs

The general `generate_video` tool accepts canonical `medias` entries with `role` and `value`. Observed roles include `image`, `start_image`, `end_image`, `video`, `audio`, and `ref_element`; use only those supported by the selected model and mode. The connector maps them to the model's backend roles.

Use confirmed media UUIDs, completed generation job UUIDs or authorized HTTPS image references where the schema permits. Local paths are not media IDs. Do not silently upload references for a prompt-only task. The relevant mode is `omni_reference` when approved image/video/audio references are used.

In `video_edit`, the input video's duration determines billing and output duration; the route ignores a supplied duration and aspect ratio. In `video_extension`, aspect ratio follows the source. Check source properties and explain any necessary reframing rather than claiming the chosen ratio was enforced.

## Boundaries and recovery

- A returned `unlim_choice` means no job was submitted. Present the choice as required and submit the same intended parameters only after the user selects a balance. Never infer the choice from elapsed time.
- If a server returns parameter adjustments, inspect them. Do not accept a different model, lower resolution or wrong final ratio silently.
- If the same visible defect persists after a targeted correction, stop automatic retries and choose another supported approach with the user. Never define a compulsory four-batch retry cycle.
- Keep source clip durations, edit timing, final runtime and billed generated seconds separate. A five-minute final video requires production/editing orchestration, not `duration: 300`.
