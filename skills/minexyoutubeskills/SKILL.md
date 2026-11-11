---
name: minexyoutubeskills
description: End-to-end faceless YouTube pipeline for "What if…" science videos on Higgsfield. Runs as five stages: 1) research topics with repeated cross-creator demand plus the Content Factory catalog, 2) mine viewer comments and write an original, sourced script with a timed scene plan, 3) show a moodboard, storyboard and live credit budget before spending, 4) write Seedance 2.5 prompts and produce the video (narration, footage, music, SFX, motion graphics, captions, edit), 5) package it with three title and thumbnail pairs, description, chapters and tags. Use when the user asks for viral or What-if topic ideas, a faceless or documentary YouTube script, a moodboard or storyboard, Seedance prompts or production of a faceless science video, or YouTube thumbnails, titles, descriptions and tags. Runs any single stage or the whole pipeline.
---

# minexyoutubeskills

One skill for the whole faceless-video job: **topic → script → pre-production → production → packaging**. Each stage has its own reference file. Load only the file for the stage you're in.

| Stage | Load | Output | Spends credits? |
|---|---|---|---|
| 1 · Topic research | `references/01-topic-research.md` | 3 (or 10) topics with proof | Apify cents, if used |
| 2 · Script | `references/02-script-writing.md` (+ comment mining below) | Narration, timed scene table, sources, handoff | Apify cents, if used |
| 3 · Pre-production | `references/03-preproduction.md` | Moodboard, storyboard and budget HTML | No |
| 4a · Scene prompts | `references/04-seedance-prompts.md` | Seedance 2.5 prompts | Only if generation is requested |
| 4b · Production | `references/05-production.md` | Finished video | Yes |
| 5 · Packaging | `references/06-packaging.md` | 3 title + thumbnail pairs and upload copy | Thumbnails ≈ 4 cr each |

Verified tool calls, input shapes and prices are in `references/tool-notes.md`. A complete worked run (Apophis) is in `examples/apophis/`: `script.md`, `moodboard-storyboard.html` and `packaging.md`. Use it as the quality bar and the format reference. Don't copy its content into new topics.

## Routing

- Start at the stage the user asks for. A user with a topic skips Stage 1; a user with a script skips Stage 2; "just the thumbnails" is Stage 5 alone.
- Carry forward everything already decided in the conversation: topic, platform, aspect ratio, length, structure, style and approved lines. Never re-ask a settled choice.
- When the platform is unknown and it changes the output, ask once with the host's clickable question tool: **YouTube video (16:9)** / **YouTube Shorts (9:16)** / **Instagram Reels or TikTok (9:16)**. For a 5-minute "documentary", default to 16:9 and say so. Aspect ratio and resolution are separate settings.
- Don't ask for narrator gender. The voice is picked from `list_voices` at production time.

## Gates (non-negotiable)

1. **No paid generation without an explicit request.** Writing prompts, scripts or storyboards never authorizes spending.
2. **Before footage: Stage 3 approval.** If the user asks to "see a moodboard and storyboard first", stop after Stage 3 and wait.
3. **Check `balance` before promising generation.** At 0 or below the budget, say so in the first lines of the reply. Deliver everything that needs no credits (scripts, prompts, briefs, HTML boards, packaging copy) and state what is blocked and its live cost. Offer `show_plans_and_credits` only if the user wants to buy.
4. **Quote live costs** (`get_cost: true`) with the date before any batch. Footage budget = generated seconds × per-second rate, plus 10–15 % for retakes.
5. **Keep routes distinct.** Content Factory (code-rendered What If shorts) and Seedance (generated footage) are different workflows. Never relabel one as the other.

## Stage 2 add-on: comment mining (do this before writing)

When the user asks what viewers care about, or for any new full script:
1. Find 4–6 popular **faceless** videos on the topic from at least 3 creators (Apify YouTube search, sorted by popularity). Prefer outliers (high views ÷ subscribers) and at least one recent upload.
2. Pull about 80 top comments per video (`streamers/youtube-comments-scraper`, `TOP_COMMENTS`).
3. Cluster them into: **what people care about**, **what's missing** (questions the videos never answer), **what grabs them** (dates, jokes, comparisons), and **production complaints** (camera, CGI realism, pacing).
4. Turn each cluster into a script decision: a beat that answers the unanswered question, a hook detail, a unit choice, a camera rule or a "SIMULATION" label.
5. Put the evidence table (comment theme + like count + where the script answers it) in the script file, with videos, views, subscribers and the pull date.

The comments are evidence of audience interest, not scientific sources. Verify every factual claim through primary sources (NASA, ESA, peer-reviewed or institutional pages). Label model estimates as estimates and state their assumptions. For impact-style numbers, compute from published equations and show the inputs.

## Pacing rules carried across stages

- When the brief asks for fast pacing, the first minute can change shots every 5–10 s, but each change must add information.
- "30-second one-shots" are continuous, evolving shots, never static holds. Seedance 2.5 renders up to 30 s per generation, so one oner is one generation. Other models may cap at about 5–15 s, which means chaining clips or a coded/3D render.
- 5 minutes ≈ 650–750 spoken words as a first estimate. Measure the real take before timing captions and cues.

## Deliverables and files

- Save each project under `scripts/<topic-slug>/` in the working repo: `script.md`, `moodboard-storyboard.html`, `packaging.md`, plus production assets.
- Render HTML boards with the pre-installed Playwright Chromium and look at screenshots before sending. Send finished files to the user and commit and push when working in a repo.
- Label every deliverable honestly: **concept**, **generation prompt**, **queued job** or **generated result**. Claim completion only with a returned result.
- End each stage with a short summary, what's blocked (if anything), and the one decision needed for the next stage.
