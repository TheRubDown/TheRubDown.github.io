# Draft Finals Dashboard — Source Files

This repo contains the **source files** for the Draft Finals dashboard (SuperCoach Draft, Strength of Schedule), not just the final built HTML. Keeping these in GitHub (not just the output file) means any Claude chat — this one or a brand new one — can pick the project back up properly instead of editing the final HTML blind.

## Files

| File | What it is |
|---|---|
| `template30.py` | The build script. Python string-templates the full HTML/CSS/JS, embeds the logos/avatars as base64, and writes the final file. |
| `payload4.json` | **All the data.** Team SOS tables (`sosFull`), Deep Dive content (`deepDive` — Top/Worst SOS, Series Targets, Frothies, Struggle Street, Top Dog Plays), Flip & Fetch tables, team draws (`teamDraws`), pick stats (`pickStats`), team codes/logos/position labels. |
| `rubhub_logo.png`, `therub_logo.png` | Header/footer brand logos. |
| `natty_avatar.png`, `wuka_avatar.png` | Host avatars shown next to "NATTY'S PICKS" / "WUKA'S PICKS". |
| `DraftFinals.html` | The built output — what actually gets deployed/shared. **Don't hand-edit this** — it's regenerated from the files above. |

## How to rebuild

```bash
python3 template30.py
```

Reads `payload4.json` + the 4 PNGs from the same folder, writes the final self-contained `DraftFinals.html`.

## Picking this up in a new Claude chat

Give Claude the GitHub repo URL and say something like:

> "Pull my Draft Finals files from this repo: `https://github.com/<you>/<repo>`"

Claude can fetch the raw files directly (`raw.githubusercontent.com` is reachable), rebuild to confirm it matches what's live, then keep editing from there.

## Known gaps (as of this build)

- **Points-conceded-by-position data** (what each team concedes to a specific position, e.g. Left Wing / Right Centre / Left 2RF) is not yet in the payload. The player profile and pick cards show season-aggregate SOS stats (Avg Opp Conceded, SOS Rating) but not a per-opponent positional breakdown. Source: a "Positional Points Conceding" sheet (Season Average + Last 6 Rounds versions) that's been discussed but not yet successfully uploaded into this build.
- Three picks are intentionally **off the live roster table** (injured, but still tracked as picks): Samuela Fainu, Viliame Kikau, Tom Dearden. They use a manual profile (`MANUAL_PROFILES` in `template30.py`) built from SuperCoach screenshot stats rather than the live `sosFull` position tables.
- KL Iro is aliased to "Kayal Iro" in the roster (`NAME_ALIASES`) since that's how he's stored in `sosFull`, but he now goes by "KL Iro".
