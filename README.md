# AI eBook Agent 📘🤖

An autonomous agent that does everything the "make money with AI eBooks"
workflow does — **and more**. It takes you from *"I want to sell an eBook"* to a
finished, sellable product: it finds a niche, writes the whole book, designs a
cover, packages **PDF + EPUB**, and generates the full **sell-it-online kit**
(sales page, pricing, KDP/Gumroad listing, launch email, social captions).

Inspired by the video *"How to Create an eBook with AI and Sell it Online"* —
rebuilt as a real, repeatable pipeline you own, with no third-party subscription
required.

---

## Two ways to use it

### 1. As a Claude Code agent (the hands-off way)
The agent lives at [`.claude/agents/ebook-creator.md`](.claude/agents/ebook-creator.md).
In Claude Code, just ask:

> "Use the ebook-creator agent to write and package an eBook about *[your topic]*."

The agent will research a niche, propose titles, check the angle with you, write
the **full manuscript**, then run the toolkit below to produce every deliverable.

### 2. As a standalone toolkit (the do-it-yourself way)
Write a manuscript in Markdown, then run one command to package everything.

```bash
pip install -r requirements.txt

python -m ebook_agent build \
  --manuscript examples/manuscript.md \
  --author "Your Name" \
  --subtitle "A practical guide" \
  --price 9 \
  --benefits "Outcome one|Outcome two|Outcome three" \
  --hooks "One killer hook line for the sales page" \
  --badge "2026 Edition" \
  --out dist/
```

This produces, in `dist/`:

| File | What it is |
|------|-----------|
| `cover.png` | 1600×2560 print-ready cover (auto-designed) |
| `<slug>.pdf` | Formatted PDF with cover, contents, chapters |
| `<slug>.epub` | Reflowable EPUB for e-readers / KDP |
| `<slug>.html` | Web preview of the whole book |
| `sales_kit.md` / `.json` | Sales page, pricing tiers, launch email, social captions, KDP keywords & categories |

---

## Manuscript format

Plain Markdown. The first `#` is the title; each `##` starts a chapter.

```markdown
# Book Title
Optional intro paragraphs.

## Chapter One
Prose with **bold**, *italic*, - bullets, > quotes.

## Chapter Two
...
```

See [`examples/manuscript.md`](examples/manuscript.md) for a complete sample
(and run the command above to see its output).

---

## Individual commands

```bash
# Just a cover
python -m ebook_agent cover --title "My Book" --author "Me" --subtitle "Sub" --out dist/cover.png

# Just the sales / listing kit
python -m ebook_agent sales --title "My Book" --author "Me" --price 12 --out dist/
```

---

## What makes it "and more"

- **Auto-designed covers** — deterministic palettes, no design skills needed.
- **Two formats out of the box** — PDF for print/download, EPUB for e-readers.
- **A complete go-to-market kit**, not just the book: pricing strategy, launch
  email, social captions, and Amazon KDP keywords + categories.
- **A premium-cover path** — swap in an AI-generated cover from an image tool by
  dropping it in as `dist/cover.png`.
- **Series & bundle guidance** baked into the agent for repeat revenue.

## Launch checklist (what the agent hands you)

1. Create a Gumroad or Amazon KDP product; upload the PDF + EPUB.
2. Paste the sales description from `sales_kit.md`; add the cover.
3. Set the launch price; add the 7 KDP keywords + categories.
4. Send the launch email; post the 3 social captions.
5. Launch low for 48h to gather reviews, then raise to the standard price.

> Income depends on your niche, quality, and marketing — this gives you the
> product and the plan, not a guarantee.
