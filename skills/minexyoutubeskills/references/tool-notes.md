# Tool notes: verified routes, inputs and prices

> Part of **minexyoutubeskills**. Observed on **11 Nov 2026**. Tool names can carry a host prefix, and prices and limits change. Re-check the live schema and call `get_cost: true` before relying on any number here.

## Higgsfield

| Job | Call | Observed facts |
|---|---|---|
| Balance | `balance` | Returns `credits` and the plan. Check it before quoting a plan as doable. |
| Model limits | `models_explore` `{action:"get", model_id:"seedance_2_5"}` | 4–30 s per generation (whole seconds); 480p/720p/1080p/4k; ratios auto, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16; modes t2v / omni_reference / video_edit / video_extension; 480p draft that can be finalized within 7 days |
| Video cost | `generate_video` `{params:{model:"seedance_2_5", resolution, aspect_ratio, duration, get_cost:true}}` | 30 s shot: **1080p = 480 cr (16/s)**, 720p = 210 cr (7/s), 480p draft = 90 cr (3/s). `generate_audio: true` did **not** change the price, so native clip SFX are effectively free |
| Thumbnail cost | `generate_image` `{params:{model:"gpt_image_2_6", aspect_ratio:"16:9", resolution:"4k", size:"3840x2160", quality:"high", output_format:"png", get_cost:true}}` | ≈ **4.25 cr** per 4K image |
| Project destination | `get_preferences` | `auto_create_project:false` means generate without creating a project |
| Workflows | `get_workflow_instructions` | Relevant: `video-editing` (Higgsedit motion graphics), `video-montage` (assembly, soundtrack, captions), `faceless-video` (non-photoreal narrated route), `narration`, `thumbnail-generation` |
| Content Factory recipe | `get_preset_instructions` `{preset:"/content-factory"}` | Code-rendered 9:16 What If shorts (about 60 s) with 56 styles and preset_ids. It is a separate route from Seedance |
| Buying credits | `show_plans_and_credits` | Only when the user asks to buy or upgrade |

Budget formula for footage: `generated seconds × per-second rate`, plus 10–15 % for retakes. A 5-minute video with about 283 s of Seedance footage came to ≈ 4,530 cr at 1080p.

## Everygen / viewmax (Content Factory reference catalog)

- `list_content_factory_references`: 56 styles, each with `views`, `likes` and `durationSeconds`. Top three by views on 11 Nov 2026:
  - Gas Giant: 54.5M views, 2.1M likes
  - Lowpoly Skyline: 26.6M views, 2.0M likes
  - Night Ledger: 10.9M views, 861K likes
- `get_content_factory_template` `{templateId:"style:<id>"}` returns a `kitId`.
- `get_video_kit` `{kitId}` returns a large result (it is saved to a file). Grep it for `"default":"What if` to find the topic title slots.
- `ask_video` refuses catalog videos that are not in the user's account, and `media.viewmax.io` downloads are blocked by the session proxy. Do not promise to watch catalog videos.

## Apify (YouTube research)

Cost: a few cents per run. Set `callOptions.maxTotalChargeUsd` as a cap.

**Search (worked):** `delicious_zebu/youtube-video-scraper-by-keyword`
```json
{"search_keywords":["what if Apophis hit Earth","Apophis asteroid impact"],
 "max_results":12,"type":"videos","sort_by":"popularity","fetch_video_details":true}
```
Notes: `type` must be `videos` or `shorts`; `sort_by` must be `relevance` or `popularity`. Read results with `get-dataset-items` and `fields: title,publisher,view_count_exact,like_count,published_at_exact,duration_seconds,detail_url,channel_subscriber_count`.

**Comments (worked):** `streamers/youtube-comments-scraper`
```json
{"startUrls":[{"url":"https://www.youtube.com/watch?v=VIDEO_ID"}],
 "maxComments":80,"sortCommentsBy":"TOP_COMMENTS"}
```
Read with `fields: videoId,voteCount,comment`, in pages of 200.

`solidcode/youtube-comments-scraper` failed with exit code 91 ("Initializing session"); don't use it.

**Page fetch:** `apify--web-fetch` `{method:"GET", path:"/", query:{url, formats:["text"], unwrap:true}}` reads NASA, Planetary Society and other pages when a direct fetch isn't available.

## Local environment

- Playwright Chromium is pre-installed. Use it to render and screenshot HTML moodboards and storyboards for self-checks.
- Write helper scripts with the file-write tool rather than shell heredocs that run Node; the latter tripped a shell safety check.
