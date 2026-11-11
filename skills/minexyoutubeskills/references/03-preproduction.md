# Stage 3 — Pre-production: moodboard, storyboard and budget

> Part of **minexyoutubeskills**. Before any paid footage is generated, show the user a moodboard, a timed storyboard and a costed production plan, and get approval. This stage spends **no credits**.

## Why this stage exists

Footage is the expensive part. A 5-minute 1080p Seedance video is several thousand credits. The user should approve the look, the shot list and the budget while changes are still free.

## Before drawing anything: check what is actually possible

Run these read-only checks first. Put their results in the plan.
1. `models_explore` → `get` for the chosen video model (default `seedance_2_5`): durations, resolutions, aspect ratios, media roles.
2. `balance`: if it is 0 or below the budget, **say so prominently**. Generation is blocked until credits are added.
3. `generate_video` with `get_cost: true` for one representative shot at each candidate resolution, plus a draft. Prices change, so quote live numbers with the date.
4. `get_preferences`: project destination behaviour.
5. `get_workflow_instructions` (no argument): confirm the editing and assembly routes exist (`video-editing` for Higgsedit motion graphics, `video-montage` for assembly, soundtrack and captions).

## Build one self-contained HTML file

Write `moodboard-storyboard.html` next to the script. Use vector sketches only: no generated images, no external fonts or assets. That keeps it free and lets it render offline. A worked example is in `examples/apophis/moodboard-storyboard.html`; reuse its structure.

**Section 1 — Moodboard**
- A one-line look statement (for example, "observed, not imagined" for realism).
- 4–6 mood tiles drawn in CSS/SVG: orbit, ground, water, subject, night, graphics-over-footage.
- **Palette**: 6–8 swatches, each tied to a material or light and a role (for example, "Impact amber · fireball, key numbers").
- **Camera and light rules** that will go into every prompt: camera behaviour, one light source per scene with Kelvin, scale anchors, treatment of sound in space.
- **Motion-graphics system**: line weight, number font, "estimate" labels, a SIMULATION tag for illustrated events, both unit systems.
- **Captions**: max lines, characters per line, placement, a highlight rule (only the key number).
- **Sound and music palette**: narrator treatment, one music arc (draw the energy curve), the SFX source, and planned silences.

**Section 2 — Storyboard**
One frame per shot, each with:
- a 16:9 SVG thumbnail sketch
- the shot ID and planned time
- a narration excerpt
- the shot description: a camera that stays steady and the action, written as visible events
- graphics and captions
- sound
- the route: **Seedance** or **graphics-only**

Mark graphics-only shots (diagrams, maps, counters over a reused plate). They are cheaper and more accurate than generating them.

Honour user-specific requests visibly. For example, "open with the impact" means frame 1 is the impact.

**Section 3 — Pipeline and budget**
- Pipeline table: voice pick → narration → footage → music → motion graphics → assembly, captions and mix → checks → delivery.
- Credits table from the live quotes: requested resolution, drafts-then-finals, and a cheaper fallback, plus a 10–15 % retake buffer. Narration and music are quoted separately before generation.
- Current balance.

## Verify before sending

Render the HTML in the pre-installed Playwright Chromium. Screenshot the full page plus 3–4 individual frames, then look at them. Fix clipped labels, overlaps and unreadable text, and check there are no page errors. Then send the file to the user (render display) and commit it.

## Approval gate

End the turn with exactly what is needed:
1. Approve the moodboard and storyboard, or name the frames to change.
2. Choose the resolution or budget option.
3. Add credits, if the balance is short.

Do not start Stage 4 until the user approves. Treat a budget answer as approval of that spend; nothing more.
