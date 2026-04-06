# The Weekly Rub Down — Run Sheet Tool · Project Brief

## What We're Building
A weekly HTML run sheet for The Weekly Rub Down NRL SuperCoach Draft podcast (hosts Natty & Wuka). Published to GitHub Pages for Rub Club Patreon subscribers. Generated fresh each week from a prompt template + attached files.

---

## Brand
- **Palette:** Deep brown `#0d0500` bg, gold `#f0c040`, cream `#fff8ee`, orange `#e07020`
- **Fonts:** Bebas Neue (display/numbers), Barlow Condensed (labels/UI), Barlow (body)
- **Aesthetic:** 1970s retro broadcast / football programme
- **Logo:** Custom "The Rub" badge (uploaded, embedded as base64)
- **Team logos:** 17 custom illustrated round logos for every NRL team (uploaded, compressed, embedded as base64) — NOT the NRL.com SVGs

---

## Page Structure (top to bottom)
1. **Site header** — The Rub logo (large), "NRL SuperCoach Draft · 2026 Season", "Exclusive to Rub Club Members", Round number (large Bebas Neue), "Run Sheet"
2. **Update bar** — Round X · Updated [date] · Natty & Wuka · The Weekly Rub Down Podcast
3. **Bye teams banner** — chips showing bye teams with their custom logos
4. **Injuries & Suspensions** — player cards with status tags (OUT/LONG/SHORT/SUS/HIA/NAMED)
5. **Waiver Wire Targets** — position blocks (FLB/CTW/5-8/HFB/HOK/2RF/FRF), each with:
   - Wire player cards (simplified)
   - Deep Dive section (Natty pick + Wuka pick)
6. **Top 3 Picks** — Natty's 3 + Wuka's 3
7. **Top Claim Per Position** — one player per position
8. **Last Round's Calls** — how did they go
9. **Footer**

---

## Wire Player Cards (non-deep dive)
Each card shows:
- **Line 1:** [Custom team logo 26px] · Player Name (bold)
- **Line 2:** POS · XX% owned · XX avg · *notes (italic)*
- **Line 3:** [Rank number coloured] EASY/MID/TOUGH · vs [Opp logo] OPPONENT (H/A)
- Left border colour = matchup difficulty colour
- No full coloured background — subtle border + coloured rank number only

**Matchup colour scale (display rank = 18 - PDF rank):**
- 1-2 = red (TOUGH)
- 3-6 = orange (TOUGH)  
- 7-11 = yellow (MID)
- 12-15 = light green (EASY)
- 16-17 = bright green (EASY)

---

## Deep Dive Cards (Natty & Wuka picks)
Full treatment per player:
- **Header:** Large custom team logo circle (gold/orange border) + Player name + POS · X games played · Price · BE
- **Last 3 Scores** — 3 score boxes, colour coded (gold=50+, grey=30+, red=poor)
- **SC Stats** — Avg / PPM / Mins / >60pts% (4-col grid, Bebas Neue numbers)
- **Score Breakdown** — Base / Scr / Cre / Evd / Neg as avg per game (5-col grid, colour coded)
- **Matchup & SOS** — coloured left border, rank + EASY/MID/TOUGH + vs [opp logo] OPP (H/A) · avg conceded, then 6-period SOS grid showing pos rank + team rank per period

**SOS Periods:** R1-8 / R9-16 / R17-22 / R22-25 / R23-26 / R24-27

---

## Data Sources Per Week
| Data | Source |
|------|--------|
| Matchup defence ranks | Game By Game Sheets PDF (attached) |
| Strength of Schedule | SOS PDF (attached) |
| Wire player ownership/avg | Waiver wire screenshots (ticked players only) |
| Player team | Read from team logo in screenshot |
| Deep dive stats | nrlsupercoachstats.com screenshots OR player profile page URL |
| Score breakdown (Base/Scr/Cre/Evd/Neg) | nrlsupercoachstats.com player profile screenshot |

---

## Weekly Workflow
1. Attach Game By Game PDF + SOS PDF
2. Attach waiver wire screenshots (7 positions) — tick the players you want included
3. Attach nrlsupercoachstats.com screenshots for each deep dive player (optional but recommended)
4. Fill in the prompt template (deep dive picks, top 3s, top claims, last round's calls)
5. Claude generates the full HTML run sheet ready to upload to GitHub Pages

---

## Key Technical Decisions
- Pure HTML/CSS — no frameworks, no build tools
- All assets (logos, fonts) embedded — works offline, no external dependencies for images
- Custom team logos are base64 encoded PNGs stored in `/home/claude/team_logos.json`
- Defence rank display = 18 - PDF rank (so PDF rank 1 = hardest = display 17)
- GitHub Pages hosting at `weeklyrubdown.github.io`

---

## What's Still Pending
- [ ] GitHub Pages setup (one-time)
- [ ] Wook to create a lightweight Google Sheet mirror of key player stats (replaces screenshots)
- [ ] First real Round 6 run sheet
- [ ] 5-8 / HFB / FRF positions not yet demoed (same card format applies)

---

## Files
- `weekly-rub-down-DEMO.html` — current demo with placeholder Rd 6 data
- `weekly-workflow-template.md` — weekly prompt template
- `/home/claude/team_logos.json` — all 17 custom team logos as base64
- `/home/claude/assets.json` — The Rub logo, Natty + Wuka avatars as base64
