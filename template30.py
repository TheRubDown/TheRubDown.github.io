import json
import base64

with open('/home/claude/build2/payload4.json') as f:
    PAYLOAD = f.read()

with open('/home/claude/build2/rubhub_logo.png', 'rb') as f:
    RUBHUB_LOGO_B64 = base64.b64encode(f.read()).decode('ascii')
with open('/home/claude/build2/therub_logo.png', 'rb') as f:
    THERUB_LOGO_B64 = base64.b64encode(f.read()).decode('ascii')
with open('/home/claude/build2/natty_avatar.png', 'rb') as f:
    NATTY_AVATAR_B64 = base64.b64encode(f.read()).decode('ascii')
with open('/home/claude/build2/wuka_avatar.png', 'rb') as f:
    WUKA_AVATAR_B64 = base64.b64encode(f.read()).decode('ascii')

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Draft Finals — The Rub Club</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow+Condensed:wght@400;600;700;800;900&family=Barlow:wght@400;500;600;700&family=Lora:ital,wght@0,400;1,400&family=Passion+One:wght@400;700;900&display=swap" rel="stylesheet">
<style>
:root{
  --gold:#f0c040;--gold-light:#ffe580;--gold-dim:#c49a20;
  --brown:#1a0800;--brown-mid:#221004;--brown-light:#3a1808;
  --cream:#ffffff;--cream-dim:#d8c8a8;
  --orange:#e07020;--purple:#7b3fa0;--blue:#2a6090;
  --bg:#0a0400;--surface:#130602;--surface2:#1a0904;
  --border:#2a1206;--text:#ffffff;--muted:#a07850;
  --sage:#7a9e6a;--mustard:#c9a227;--brick:#a04535;
  --sage-dim:rgba(122,158,106,.18);--mustard-dim:rgba(201,162,39,.18);--brick-dim:rgba(160,69,53,.18);
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Barlow',sans-serif;font-size:16.5px;background:var(--bg);color:var(--text);min-height:100vh}
body::before{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.035) 2px,rgba(0,0,0,.035) 4px);pointer-events:none;z-index:999}
a{color:inherit}
.site-header{background:var(--brown);border-bottom:3px solid var(--gold);position:relative}
.site-header::after{content:'';display:block;height:2px;background:repeating-linear-gradient(90deg,var(--gold) 0,var(--gold) 8px,transparent 8px,transparent 16px)}
.header-inner{max-width:1200px;margin:0 auto;padding:28px 24px 24px;position:relative;display:flex;flex-direction:column;align-items:center;text-align:center}
.header-brand{display:flex;flex-direction:column;align-items:center;gap:8px}
.hub-logo{height:130px;width:auto;object-fit:contain;flex-shrink:0;filter:drop-shadow(0 0 18px rgba(240,192,64,.3));margin-bottom:4px}
.htitle{font-family:'Passion One',sans-serif;font-weight:900;font-size:clamp(30px,7.5vw,80px);letter-spacing:1px;color:var(--gold);line-height:1;text-shadow:0 0 40px rgba(240,192,64,.25)}
.htitle span{color:var(--orange)}
.hsub{font-family:'Barlow Condensed',sans-serif;font-size:1rem;letter-spacing:3px;text-transform:uppercase;color:var(--cream-dim);margin-top:6px;font-weight:700}
.hpatreon{display:inline-block;margin:2px 0 6px;font-family:'Barlow Condensed',sans-serif;font-size:.9rem;letter-spacing:2px;color:var(--gold-dim);text-decoration:none}
.crumbbar{background:var(--surface);border-bottom:1px solid var(--border);padding:10px 24px;display:flex;align-items:center;gap:10px;font-family:'Barlow Condensed',sans-serif;font-size:.92rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);flex-wrap:wrap}
.crumb{cursor:pointer;transition:color .15s}
.crumb:hover{color:var(--gold)}
.crumb.active{color:var(--gold);font-weight:800}
.crumbsep{color:var(--border)}
.wrap{max-width:1200px;margin:0 auto;padding:28px 20px 80px}
.view{display:none}
.view.active{display:block}

/* LANDING */
.landing-hero{text-align:center;padding:40px 0 32px}
.landing-eyebrow{font-family:'Bebas Neue',sans-serif;font-size:15px;letter-spacing:5px;color:var(--orange);margin-bottom:10px;display:flex;align-items:center;justify-content:center;gap:8px}
.landing-eyebrow::before{content:'';width:8px;height:8px;background:var(--orange);border-radius:50%;animation:blink 1.6s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.2}}
.landing-h1{font-family:'Passion One',sans-serif;font-weight:900;font-size:clamp(40px,7vw,76px);letter-spacing:1px;color:var(--cream);line-height:1.05}
.landing-h1 span{color:var(--gold)}
.landing-sub{font-family:'Lora',serif;font-style:italic;color:var(--muted);font-size:17px;margin-top:14px;max-width:560px;margin-left:auto;margin-right:auto}
.window-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:36px}
@media(max-width:860px){.window-grid{grid-template-columns:1fr}}
.window-card{background-image:radial-gradient(circle at 1px 1px,rgba(26,8,0,.14) 1.2px,transparent 1.6px),linear-gradient(135deg,var(--gold-light) 0%,var(--gold) 55%,var(--gold-dim) 100%);background-size:14px 14px,auto;border:3px solid var(--brown);padding:30px 26px;cursor:pointer;transition:transform .18s,box-shadow .18s;position:relative;overflow:hidden;box-shadow:8px 8px 0 var(--brown)}
.window-card:hover{transform:translate(-4px,-4px);box-shadow:12px 12px 0 var(--brown)}
.wc-num{position:absolute;top:12px;right:-38px;background:var(--brown);color:var(--gold-light);font-family:'Bebas Neue',sans-serif;font-size:14px;letter-spacing:2px;padding:6px 42px;transform:rotate(45deg);box-shadow:0 2px 8px rgba(0,0,0,.35)}
.wc-eyebrow{font-family:'Barlow Condensed',sans-serif;font-size:.88rem;letter-spacing:3px;color:var(--brown);text-transform:uppercase;font-weight:800}
.wc-eyebrow::after{content:'';display:block;width:38px;height:3px;background:var(--brown);margin-top:9px;opacity:.6}
.wc-title{font-family:'Passion One',sans-serif;font-weight:900;font-size:42px;letter-spacing:1px;color:var(--brown);margin-top:10px}
.wc-sub{font-family:'Barlow Condensed',sans-serif;font-size:.98rem;color:var(--brown-mid);margin-top:4px;letter-spacing:1px;font-weight:700}
.wc-byes{margin-top:16px;font-family:'Barlow Condensed',sans-serif;font-size:1rem;letter-spacing:.3px;color:var(--brown-mid);font-weight:700}
.wc-byes b{color:var(--brown);font-weight:800;letter-spacing:1.5px}
.wc-cta{margin-top:20px;font-family:'Barlow Condensed',sans-serif;font-size:.92rem;letter-spacing:2px;color:var(--gold-light);font-weight:800;display:inline-flex;align-items:center;gap:8px;background:var(--brown);padding:11px 20px;transition:gap .15s,background .15s}
.window-card:hover .wc-cta{gap:14px;background:#000}

/* TABS */
.tabbar{display:flex;gap:0;border-bottom:2px solid var(--border);margin-bottom:28px;overflow-x:auto}
.tab{font-family:'Bebas Neue',sans-serif;font-size:20px;letter-spacing:2px;color:var(--muted);padding:12px 20px;cursor:pointer;border-bottom:3px solid transparent;transition:all .15s;white-space:nowrap}
.tab:hover{color:var(--cream)}
.tab.active{color:var(--gold);border-bottom-color:var(--gold)}
.panel{display:none}
.panel.active{display:block}

/* SECTION HEADERS */
.sh{display:flex;align-items:baseline;gap:14px;margin-bottom:18px;padding-bottom:10px;border-bottom:1px solid var(--border);flex-wrap:wrap}
.st{font-family:'Passion One',sans-serif;font-weight:900;font-size:28px;letter-spacing:.5px;color:var(--gold)}
.ss{font-size:13.5px;letter-spacing:1.5px;color:var(--muted);text-transform:uppercase;font-weight:600}

/* BYE STRIP */
.bye-strip{display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:var(--surface);border:1px solid var(--border);padding:12px 18px;margin-bottom:24px}
.bye-lbl{font-family:'Bebas Neue',sans-serif;font-size:13px;letter-spacing:2px;color:var(--muted)}
.bye-chip{font-family:'Bebas Neue',sans-serif;font-size:14px;letter-spacing:1px;border:1px solid var(--border);color:var(--cream-dim);padding:3px 10px;background:var(--surface2)}
.bye-chip b{color:var(--orange)}

/* PRELIM TOGGLE */
.prelim-toggle{display:inline-flex;border:1px solid var(--gold-dim);border-radius:3px;overflow:hidden;margin-left:auto}
.pt-btn{font-family:'Bebas Neue',sans-serif;font-size:13px;letter-spacing:1.5px;padding:6px 14px;cursor:pointer;background:transparent;color:var(--muted);transition:all .15s;border:none}
.pt-btn.active{background:var(--gold);color:var(--brown)}

/* RANK TABLE */
.rtbl{width:100%;border-collapse:collapse;font-family:'Barlow Condensed',sans-serif}
.rtbl th{text-align:left;font-size:12px;letter-spacing:1.5px;color:var(--muted);text-transform:uppercase;padding:8px 10px;border-bottom:2px solid var(--border)}
.rtbl td{padding:9px 10px;border-bottom:1px solid var(--border);font-size:15.5px}
.rtbl tr.clickable{cursor:pointer;transition:background .15s}
.rtbl tr.clickable:hover{background:var(--surface2)}
.rk{font-family:'Bebas Neue',sans-serif;font-weight:700;font-size:27px;color:var(--gold);width:34px}
.rk.rk-hi{color:var(--sage)}
.rk.rk-lo{color:var(--brick)}
.sos-pill{display:inline-block;padding:5px 13px;border-radius:4px;font-weight:700;font-size:17px;min-width:36px;text-align:center}
.sos-hi{background:var(--sage-dim);color:var(--sage)}
.sos-mid{background:var(--mustard-dim);color:var(--mustard)}
.sos-lo{background:var(--brick-dim);color:var(--brick)}

/* TEAM PILL */
.pill{display:inline-flex;align-items:center;gap:6px;padding:3px 10px 3px 4px;font-size:13.5px;letter-spacing:.5px;border-radius:14px;font-weight:800;vertical-align:middle;cursor:pointer;border:1px solid rgba(0,0,0,.25)}
.pill img{width:22px;height:22px;border-radius:50%;object-fit:cover;flex-shrink:0;display:block;background:#fff;border:1.5px solid rgba(255,255,255,.6)}
.pill span.pill-label{letter-spacing:.5px}
.pill-lg{font-size:26px;padding:8px 24px 8px 10px;border-radius:34px;gap:12px;cursor:default}
.pill-lg img{width:46px;height:46px;border:2px solid rgba(255,255,255,.6)}
.pill-md{font-size:18px;padding:6px 18px 6px 6px;border-radius:24px;gap:9px}
.pill-md img{width:32px;height:32px;border:2px solid rgba(255,255,255,.6)}
.p-DOL{background:#d6483a;color:#fff}
.p-CRO{background:#2f9aa3;color:#fff}
.p-WTG{background:#e0922f;color:#1a0d00}
.p-SYD{background:#1c2f47;color:#fff}
.p-CBY{background:#1c3868;color:#fff}
.p-SSR{background:#2d7a42;color:#fff}
.p-COW{background:#1c2f57;color:#f0c040}
.p-BRI{background:#7a2238;color:#f0c040}
.p-SEA{background:#6b1f25;color:#fff}
.p-CAN{background:#3f7a3a;color:#fff}
.p-NZW{background:#123a6b;color:#fff}
.p-MEL{background:#4b2470;color:#fff}
.p-PAR{background:#00567a;color:#f0c040}
.p-DRA{background:#b8362c;color:#fff}
.p-PEN{background:#161616;color:#fff}
.p-NCI{background:#a8302a;color:#fff}
.p-GCT{background:#1f8fa0;color:#fff}

/* DRAW GRID */
.draw-grid{display:grid;gap:1px;background:var(--border);margin:12px 0;border:1px solid var(--border)}
.dg-opp{background:var(--surface2);color:var(--cream-dim);font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:12.5px;letter-spacing:.5px;padding:6px 4px;text-align:center;display:flex;align-items:center;justify-content:center}

/* SMALL TEAM CODE CHIPS — for tight spaces where the full logo pill won't fit.
   Colors pulled from the dominant tones in each uploaded crest. */
.tchip{display:inline-block;padding:3px 8px;border-radius:5px;font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:11.5px;letter-spacing:.5px;line-height:1.3;white-space:nowrap}
.tc-DOL{background:#d6483a;color:#fff}
.tc-CRO{background:#2f9aa3;color:#fff}
.tc-WTG{background:#e0922f;color:#1a0d00}
.tc-SYD{background:#1c2f47;color:#fff}
.tc-CBY{background:#1c3868;color:#fff}
.tc-SSR{background:#2d7a42;color:#fff}
.tc-COW{background:#1c2f57;color:#f0c040}
.tc-BRI{background:#7a2238;color:#f0c040}
.tc-SEA{background:#6b1f25;color:#fff}
.tc-CAN{background:#3f7a3a;color:#fff}
.tc-NZW{background:#123a6b;color:#fff}
.tc-MEL{background:#4b2470;color:#fff}
.tc-PAR{background:#00567a;color:#f0c040}
.tc-DRA{background:#b8362c;color:#fff}
.tc-PEN{background:#161616;color:#fff}
.tc-NCI{background:#a8302a;color:#fff}
.tc-GCT{background:#1f8fa0;color:#fff}
.dg-ven{background:var(--surface);color:var(--muted);font-size:12px;text-align:center;padding:5px 6px;font-weight:700}
.dg-ven.bye{color:var(--brick)}
.dg-rd{background:var(--surface);color:var(--muted);font-family:'Barlow Condensed',sans-serif;font-size:10.5px;letter-spacing:1px;text-align:center;padding:5px 4px;font-weight:700;text-transform:uppercase}
.tchip-full{display:block;width:100%;padding:8px 4px;border-radius:5px;font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:14.5px;letter-spacing:.3px;line-height:1.2;text-align:center;white-space:normal;word-break:break-word;box-sizing:border-box}
.dg-concede{background:var(--surface2);text-align:center;padding:8px 4px;display:flex;align-items:center;justify-content:center}
.dg-concede.bye{color:var(--muted)}
.concede-pill{display:inline-block;padding:4px 11px;border-radius:6px;font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:17px;letter-spacing:.3px}

/* POSITIONAL LIST (Deep Dive highlight cards) — bold treatment matching stats pos-card */
.dd-pos-list{display:flex;flex-direction:column;gap:10px;margin-top:14px}
.dd-pos-card{display:flex;flex-direction:column;gap:10px;background:var(--surface2);border:1px solid var(--border);border-radius:4px;padding:12px 16px;cursor:pointer;transition:border-color .15s}
.dd-pos-card:hover{border-color:var(--gold-dim)}
.dd-pos-top{display:flex;justify-content:space-between;align-items:center;gap:10px}
.dd-pos-name{color:var(--cream);font-weight:800;font-size:18px;font-family:'Barlow Condensed',sans-serif}
.dd-pos-rank-badge{font-family:'Bebas Neue',sans-serif;font-weight:700;font-size:15px;letter-spacing:.5px;color:var(--bg);background:var(--gold);padding:7px 16px;border-radius:4px;white-space:nowrap;text-transform:uppercase;flex-shrink:0}
.pl-row{display:flex;align-items:center;gap:13px}
.pl-avatar{width:42px;height:42px;border-radius:50%;background:var(--bg);border:2px solid var(--gold-dim);display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;font-size:15px;color:var(--gold);overflow:hidden;flex-shrink:0}
.pl-avatar img{width:100%;height:100%;object-fit:cover;object-position:top center}

/* FULL TEAM POSITIONAL TABLE (Stats tab team click) */
.pos-cards{display:flex;flex-direction:column;gap:10px;margin-bottom:8px}
.pos-card{background:var(--surface2);border:1px solid var(--border);padding:14px 16px;border-radius:4px;transition:border-color .15s}
.pos-card.clickable{cursor:pointer}
.pos-card.clickable:hover{border-color:var(--gold-dim)}
.pos-card-top{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:12px}
.pos-card-stats{display:flex;gap:22px;flex-wrap:wrap;align-items:flex-end}
.stat-item{display:flex;flex-direction:column;gap:3px}
.stat-item-lbl{font-family:'Barlow Condensed',sans-serif;font-size:11px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;font-weight:700}
.stat-item-val{font-family:'Barlow Condensed',sans-serif;font-size:18px;font-weight:700;color:var(--cream)}
.poslabel{font-family:'Bebas Neue',sans-serif;font-size:16px;letter-spacing:1.5px;color:var(--bg);background:var(--gold);padding:7px 16px;border-radius:4px;white-space:nowrap;display:inline-block;font-weight:700}

/* TEAM CARDS GRID (deep dive) */
.team-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px;margin-top:18px}
.tcard{background:var(--surface);border:1px solid var(--border);padding:18px;position:relative;overflow:hidden}
.tcard::before{content:'';position:absolute;top:0;left:0;width:3px;height:100%}
.tcard.gn::before{background:var(--sage)}.tcard.rd::before{background:var(--brick)}
.tcard-hd{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.tcard-rank-badge{font-family:'Bebas Neue',sans-serif;font-weight:700;font-size:13.5px;letter-spacing:1px;padding:6px 12px;border-radius:4px;white-space:nowrap}
.tcard-rank-badge.gn{background:var(--sage-dim);color:var(--sage)}
.tcard-rank-badge.rd{background:var(--brick-dim);color:var(--brick)}

/* WIRE TABLE */
.wire-tbl{width:100%;border-collapse:collapse;font-family:'Barlow Condensed',sans-serif;font-size:15.5px;font-weight:600}
.wire-tbl th{font-size:11.5px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;padding:7px 8px;border-bottom:2px solid var(--border);text-align:center}
.wire-tbl th.lbl{text-align:left}
.wire-tbl td{padding:9px 8px;border-bottom:1px solid var(--border);text-align:center;vertical-align:middle}
.wire-tbl td.lbl{text-align:left}
.wire-divider{border-left:2px solid var(--gold-dim) !important}
.bdg{font-size:11px;letter-spacing:1.5px;padding:2px 7px;font-weight:800;white-space:nowrap;border-radius:2px}
.wire-player{font-weight:800;color:var(--cream);font-size:19px}
.bdg-flip{background:var(--brick-dim);color:var(--brick)}
.bdg-fetch{background:var(--sage-dim);color:var(--sage)}

/* DEEP ANALYSIS / TRADE CARDS */
.trade-cols{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media(max-width:760px){.trade-cols{grid-template-columns:1fr}}
.trade-col{background:var(--surface);border:1px solid var(--border);padding:18px}
.trade-col.sell{border-top:3px solid var(--brick)}
.trade-col.buy{border-top:3px solid var(--sage)}
.trade-hd{font-family:'Passion One',sans-serif;font-weight:700;font-size:19px;letter-spacing:.5px;margin-bottom:10px}
.trade-col.sell .trade-hd{color:var(--brick)}
.trade-col.buy .trade-hd{color:var(--sage)}
.trade-line{font-family:'Lora',serif;font-style:italic;font-size:14.5px;color:var(--cream-dim);line-height:1.6;margin-bottom:10px}
.trade-examples{margin-top:14px;padding-top:14px;border-top:1px solid var(--border)}
.trade-ex-lbl{font-size:12px;letter-spacing:2px;color:var(--muted);text-transform:uppercase;margin-bottom:8px}
.trade-ex{font-family:'Barlow Condensed',sans-serif;font-size:15px;color:var(--cream);padding:4px 0}
.trade-ex::before{content:'\\2192\\0020';color:var(--orange)}

/* TARGETS */
.target-strip{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.target-chip{background:var(--surface2);border:1px solid var(--gold-dim);color:var(--gold-light);font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:14.5px;padding:6px 14px;cursor:pointer}
.target-chip:hover{background:var(--gold);color:var(--brown)}
.picks-block{margin-top:18px}
.picks-row{display:flex;align-items:center;gap:10px}
.host-avatar{width:44px;height:44px;border-radius:50%;background:var(--gold);color:var(--brown);display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;font-size:15px;font-weight:700;flex-shrink:0;overflow:hidden;border:2px solid var(--gold-dim)}
.host-avatar img{width:100%;height:100%;object-fit:cover;object-position:top center}
.picks-lbl{font-family:'Barlow Condensed',sans-serif;font-size:14px;letter-spacing:1.5px;color:var(--muted);text-transform:uppercase;font-weight:700}
.tc-pos{color:var(--muted);font-weight:600;font-size:12.5px}
.target-chip.frothie{display:inline-flex;align-items:center;gap:8px}
.tc-rank{font-family:'Bebas Neue',sans-serif;background:var(--gold);color:var(--bg);border-radius:50%;width:18px;height:18px;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:700}
.target-chip.frothie:hover .tc-rank{background:var(--brown);color:var(--gold)}
.tc-note{color:var(--muted);font-weight:600;font-size:12px;font-style:italic}
.pick-card{display:flex;align-items:center;gap:10px;background:var(--surface2);border:1px solid var(--gold-dim);border-radius:4px;padding:8px 16px 8px 10px;cursor:pointer;transition:border-color .15s,background .15s}
.pick-card:hover{border-color:var(--gold);background:rgba(240,192,64,.08)}
.pick-card-info{display:flex;flex-direction:column;gap:3px}
.pick-card-name{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:15.5px;color:var(--gold-light);white-space:nowrap}
.pick-card-meta{display:flex;align-items:center;gap:7px}
.pick-pos{font-family:'Barlow Condensed',sans-serif;font-size:11.5px;color:var(--muted);font-weight:700;text-transform:uppercase}
.pick-card-extra{font-family:'Barlow Condensed',sans-serif;font-size:12px;color:var(--gold-dim);margin-top:2px}
.pick-card-extra b{color:var(--gold-light);font-weight:800}
.pick-rank{flex-shrink:0}
.placeholder-note{font-family:'Lora',serif;font-style:italic;color:var(--muted);font-size:14.5px;margin-top:10px}

/* PLAYER PROFILE */
.player-hero{display:flex;gap:20px;align-items:center;margin-bottom:24px;flex-wrap:wrap}
.player-avatar{width:84px;height:84px;border-radius:50%;background:var(--surface2);border:2px solid var(--gold-dim);display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;font-size:26px;color:var(--gold);overflow:hidden;flex-shrink:0}
.player-avatar img{width:100%;height:100%;object-fit:cover;object-position:top center}
.player-name{font-family:'Passion One',sans-serif;font-weight:900;font-size:38px;letter-spacing:.5px;color:var(--cream)}
.player-meta{font-family:'Barlow Condensed',sans-serif;font-size:14.5px;color:var(--muted);margin-top:4px;display:flex;gap:10px;align-items:center}
.stat-strip{display:grid;grid-template-columns:repeat(7,1fr);gap:12px;margin-bottom:28px}
@media(max-width:860px){.stat-strip{grid-template-columns:repeat(4,1fr)}}
@media(max-width:600px){.stat-strip{grid-template-columns:repeat(3,1fr)}}
@media(max-width:480px){.hub-logo{height:78px}.htitle{font-size:38px}.hsub{font-size:.8rem;letter-spacing:2px}}
.stat-box{background:var(--surface);border:1px solid var(--border);padding:14px 10px;text-align:center}
.stat-val{font-family:'Bebas Neue',sans-serif;font-size:25px;color:var(--gold)}
.stat-lbl{font-size:11px;letter-spacing:1.5px;color:var(--muted);text-transform:uppercase;margin-top:4px}
.draw-tbl{width:100%;border-collapse:collapse;font-family:'Barlow Condensed',sans-serif;font-size:14.5px}
.draw-tbl th{font-size:11.5px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;padding:7px 8px;border-bottom:2px solid var(--border)}
.draw-tbl td{padding:7px 8px;border-bottom:1px solid var(--border)}
.draw-tbl tr.bye td{color:var(--muted);font-style:italic}
.note-card{background:var(--surface2);border-left:3px solid var(--gold);padding:10px 14px;margin-top:18px;font-family:'Lora',serif;font-style:italic;font-size:14.5px;color:var(--cream-dim)}

/* BACK BUTTON */
.back-btn{font-family:'Barlow Condensed',sans-serif;font-size:14px;letter-spacing:2px;color:var(--orange);font-weight:700;cursor:pointer;text-transform:uppercase;display:inline-flex;align-items:center;gap:6px;margin-bottom:18px}
.back-btn:hover{color:var(--gold)}

/* FOOTER */
.ftr{text-align:center;padding:32px 20px;border-top:1px solid var(--border);margin-top:20px}
.ftr-logo{height:70px;width:auto;object-fit:contain;margin-bottom:14px;filter:drop-shadow(0 0 14px rgba(240,192,64,.25))}
.flog{font-family:'Barlow Condensed',sans-serif;font-size:12.5px;letter-spacing:3px;color:var(--muted);text-transform:uppercase}

.empty-state{font-family:'Lora',serif;font-style:italic;color:var(--muted);text-align:center;padding:30px;font-size:15.5px}
</style>
</head>
<body>

<div class="site-header">
  <div class="header-inner">
    <div class="header-brand">
      <img src="data:image/png;base64,__RUBHUB_LOGO__" alt="The Rub Hub" class="hub-logo">
      <a class="hpatreon" href="https://www.patreon.com/rubberstats" target="_blank">PATREON.COM/RUBBERSTATS</a>
      <div class="htitle">DRAFT <span>FINALS</span></div>
      <div class="hsub">SuperCoach Draft &middot; Strength of Schedule &middot; The Rub Club</div>
    </div>
  </div>
</div>

<div class="crumbbar" id="crumbbar">
  <span class="crumb active" onclick="goLanding()">DRAFT FINALS</span>
</div>

<div class="wrap">

  <!-- LANDING -->
  <div class="view active" id="view-landing">
    <div class="landing-hero">
      <div class="landing-eyebrow">SUPERCOACH DRAFT &middot; FINALS SYSTEM</div>
      <div class="landing-h1">WHICH SYSTEM<br>DOES <span>YOUR<br>LEAGUE</span> PLAY?</div>
      <div class="landing-sub">Built for SuperCoach Draft leagues. Full SOS rank for every team, every position. Pick the finals window that matches your draft league.</div>
    </div>
    <div class="window-grid" id="windowGrid"></div>
  </div>

  <!-- WINDOW VIEW -->
  <div class="view" id="view-window">
    <div class="back-btn" onclick="goLanding()">&larr; ALL FINALS SYSTEMS</div>
    <div class="sh">
      <div class="st" id="winTitle"></div>
      <div class="ss" id="winSub"></div>
    </div>
    <div class="bye-strip" id="byeStrip"></div>

    <div class="tabbar">
      <div class="tab active" data-tab="stats">STATS</div>
      <div class="tab" data-tab="deep">DEEP DIVE</div>
      <div class="tab" data-tab="flipfetch">FLIP &amp; FETCH</div>
    </div>

    <!-- ===== STATS PANEL ===== -->
    <div class="panel active" data-panel="stats">
      <div class="sh">
        <div class="st" style="font-size:18px">TEAM RANK / SOS &mdash; 1 TO 17</div>
        <div class="ss" id="prelimWrap"></div>
      </div>
      <table class="rtbl" id="rankTable"><thead><tr>
        <th>RK</th><th>TEAM</th><th>AVG SCORE</th><th>AVG OPP CONCEDED</th><th>SOS</th>
      </tr></thead><tbody></tbody></table>
      <div class="placeholder-note">Click any team to see every position's player and SOS rank for that window.</div>
    </div>

    <!-- ===== DEEP DIVE PANEL ===== -->
    <div class="panel" data-panel="deep">
      <div class="sh"><div class="st" style="font-size:18px">SERIES TARGETS</div><div class="ss">THE PICKS</div></div>
      <div class="picks-block">
        <div class="picks-row">
          <span class="host-avatar"><img src="data:image/png;base64,__NATTY_AVATAR__" alt="Natty"></span>
          <span class="picks-lbl">NATTY'S PICKS</span>
        </div>
        <div class="target-strip" id="nattyChips"></div>
      </div>
      <div class="picks-block">
        <div class="picks-row">
          <span class="host-avatar"><img src="data:image/png;base64,__WUKA_AVATAR__" alt="Wuka"></span>
          <span class="picks-lbl">WUKA'S PICKS</span>
        </div>
        <div class="target-strip" id="wukaChips"></div>
      </div>

      <div class="sh" style="margin-top:32px"><div class="st" style="font-size:18px">TOP 5 FREE AGENT FROTHIES</div><div class="ss">UNDER 40% OWNED</div></div>
      <div class="target-strip" id="frothieChips"></div>

      <div class="sh" style="margin-top:32px"><div class="st" style="font-size:18px">TOP SOS</div><div class="ss">TOP 5 TEAMS + POSITIONAL STANDOUTS + DRAW</div></div>
      <div class="team-cards" id="topCards"></div>

      <div class="sh" style="margin-top:32px"><div class="st" style="font-size:18px">WORST SOS</div><div class="ss">BOTTOM 3 TEAMS + HARDEST RUNS</div></div>
      <div class="team-cards" id="worstCards"></div>

      <div class="sh" style="margin-top:32px"><div class="st" style="font-size:18px">STRUGGLE STREET MOVES</div><div class="ss">SELL HIGH-LADDER COACHES, BUY FOR THE FINALS</div></div>
      <div class="trade-cols" id="struggleCols"></div>

      <div class="sh" style="margin-top:32px"><div class="st" style="font-size:18px">TOP DOG PLAYS</div><div class="ss">SELL LOW-LADDER COACHES, BUY THEIR FINALS RUN</div></div>
      <div class="trade-cols" id="topdogCols"></div>

      <div class="sh" style="margin-top:32px"><div class="st" style="font-size:18px">THE WIRE &mdash; FLIP &amp; FETCHES</div><div class="ss">RUN THE TABLE (RD17&ndash;22) VS FINALS WINDOW SOS RANK</div></div>
      <div style="overflow-x:auto">
      <table class="wire-tbl" id="wireTable"><thead><tr>
        <th>RK</th><th>SOS</th><th>AVG</th><th class="lbl">TEAM (RUN THE TABLE)</th>
        <th class="wire-divider">FLAG</th>
        <th class="lbl">TEAM (FINALS)</th><th>AVG</th><th>OPP</th><th>SOS</th><th>RK</th>
      </tr></thead><tbody></tbody></table>
      </div>
    </div>

    <!-- ===== FLIP & FETCH PANEL ===== -->
    <div class="panel" data-panel="flipfetch">
      <div class="sh">
        <div class="st" style="font-size:18px">TEAM FLIP &amp; FETCH &mdash; 1 TO 17</div>
        <div class="ss">RUN THE TABLE (RD17&ndash;22) SOS RANK &rarr; FINALS WINDOW SOS RANK</div>
      </div>
      <table class="rtbl" id="ffRankTable"><thead><tr>
        <th>RTT RANK</th><th>TEAM</th><th>RTT SOS</th><th>&rarr;</th><th>FINALS RANK</th><th>FINALS SOS</th><th>FLAG</th>
      </tr></thead><tbody></tbody></table>
      <div class="placeholder-note">FLIP = schedule gets harder heading into finals (sell signal). FETCH = schedule gets easier heading into finals (buy signal). Click any team to see every position's Flip/Fetch status.</div>
    </div>

  </div>

  <!-- TEAM VIEW (from Stats tab — full positional rank table) -->
  <div class="view" id="view-team">
    <div class="back-btn" id="teamBackBtn">&larr; BACK TO WINDOW</div>
    <div class="sh"><div class="st" id="teamTitle"></div><div class="ss" id="teamRankSub"></div></div>
    <div id="teamDrawWrap"></div>
    <div class="sh" style="margin-top:8px">
      <div class="st" style="font-size:16px">EVERY POSITION, RANKED</div>
      <div class="ss" id="teamPrelimWrap"></div>
    </div>
    <div class="pos-cards" id="teamPosTable"></div>
  </div>

  <!-- TEAM FLIP & FETCH VIEW (from Flip & Fetch tab) -->
  <div class="view" id="view-team-ff">
    <div class="back-btn" onclick="showView('window')">&larr; BACK TO WINDOW</div>
    <div class="sh"><div class="st" id="ffTeamTitle"></div><div class="ss" id="ffTeamSub"></div></div>
    <div class="pos-cards" id="ffTeamPosTable"></div>
  </div>

  <!-- PLAYER VIEW -->
  <div class="view" id="view-player">
    <div class="back-btn" id="playerBackBtn">&larr; BACK TO TEAM</div>
    <div class="player-hero">
      <div class="player-avatar" id="playerAvatar"></div>
      <div>
        <div class="player-name" id="playerName"></div>
        <div class="player-meta" id="playerMeta"></div>
      </div>
    </div>
    <div class="stat-strip" id="playerStats"></div>
    <div id="playerDrawWrap"></div>
    <div class="note-card" id="playerNote" style="display:none"></div>
  </div>

</div>

<div class="ftr">
  <img src="data:image/png;base64,__THERUB_LOGO__" alt="The Rub" class="ftr-logo">
  <div class="flog">THE WEEKLY RUB DOWN &middot; THE RUB CLUB &middot; PATREON.COM/RUBBERSTATS</div>
</div>

<script>
const DATA = __PAYLOAD__;
const WINMETA = DATA.windowMeta;
const DEEPDIVE = DATA.deepDive;
const SOSFULL = DATA.sosFull;
const FLIPFETCH = DATA.flipFetch;
const PLAYERS = DATA.players;
const TEAM_CODES = DATA.teamCodes;
const TEAM_LOGOS = DATA.teamLogos;
const POS_ORDER = DATA.positionOrder;
const POS_LABELS = DATA.positionLabels;
const PICKSTATS = DATA.pickStats || {};
const NAME_ALIASES = { 'KL Iro': 'Kayal Iro' };
const TEAM_DRAWS = DATA.teamDraws || {};
const MANUAL_PROFILES = {
  'Samuela Fainu': { team:'Tigers', pos:'2RF', avg:74, mins:78, r35:'76/71', ppm:0.95, injury:'Foot, Round 20-21' },
  'Viliame Kikau': { team:'Bulldogs', pos:'2RF', avg:57, mins:72, r35:'50/50', ppm:0.79, injury:'Pectoral, Round 20' },
  'Tom Dearden': { team:'Cowboys', pos:'HFB', avg:77, mins:80, r35:'97/91', ppm:0.96, injury:'Ankle, Round 16-18' }
};

let state = { winKey:null, prelim:false, teamName:null, teamContext:'stats', teamPrelim:false, playerName:null, playerBackTo:null, concedePeriod:'seasonAvg', drawCtx:null };

function sosTier(v){ if(v>=40) return 'sos-hi'; if(v>=28) return 'sos-mid'; return 'sos-lo'; }
function rkTier(n){ if(n<=3) return 'rk-hi'; if(n>=15) return 'rk-lo'; return ''; }
const TEAM_CODES_UC = {};
for (const k in TEAM_CODES) TEAM_CODES_UC[k.toUpperCase()] = TEAM_CODES[k];
function code(team){ return TEAM_CODES_UC[(team||'').toUpperCase()] || ''; }
function teamEq(a,b){ return (a||'').toUpperCase()===(b||'').toUpperCase(); }
function possessive(name){ return /s$/i.test(name) ? name + "'" : name + "'s"; }
function findTeamDraw(winKey, teamName){
  const teams = TEAM_DRAWS[winKey] || {};
  const key = Object.keys(teams).find(k=>teamEq(k, teamName));
  return key ? teams[key] : null;
}
function pillHtml(team, onclick, extraClass){
  const c = code(team);
  const logo = TEAM_LOGOS[c];
  const img = logo ? `<img src="${logo}" alt="${team}">` : '';
  return `<span class="pill p-${c} ${extraClass||''}" ${onclick?`onclick="${onclick}"`:''}>${img}<span class="pill-label">${team.toUpperCase()}</span></span>`;
}

// ---------- VIEW ROUTER ----------
function showView(id){
  document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
  document.getElementById('view-'+id).classList.add('active');
  window.scrollTo({top:0,behavior:'smooth'});
  updateCrumbs(id);
}
function updateCrumbs(id){
  const bar = document.getElementById('crumbbar');
  let html = `<span class="crumb${id==='landing'?' active':''}" onclick="goLanding()">DRAFT FINALS</span>`;
  if(state.winKey){
    html += `<span class="crumbsep">/</span><span class="crumb${id==='window'?' active':''}" onclick="goWindow('${state.winKey}')">${WINMETA[state.winKey].label}</span>`;
  }
  if(state.teamName){
    const teamFn = state.teamContext==='flipfetch' ? `goTeamFlipFetch('${state.teamName}')` : `goTeamByName('${state.teamName}')`;
    html += `<span class="crumbsep">/</span><span class="crumb${(id==='team'||id==='team-ff')?' active':''}" onclick="${teamFn}">${state.teamName.toUpperCase()}</span>`;
  }
  if(state.playerName){
    html += `<span class="crumbsep">/</span><span class="crumb active">${state.playerName.toUpperCase()}</span>`;
  }
  bar.innerHTML = html;
}
function goLanding(){ state={winKey:null,prelim:false,teamName:null,teamPrelim:false,playerName:null,playerBackTo:null}; showView('landing'); }

// ---------- LANDING ----------
function renderLanding(){
  const grid = document.getElementById('windowGrid');
  grid.innerHTML = Object.keys(WINMETA).map((k,i)=>{
    const w = WINMETA[k];
    const byeNames = w.byes.map(b=>b[1]).join(', ');
    return `<div class="window-card" onclick="goWindow('${k}')">
      <div class="wc-num">0${i+1}</div>
      <div class="wc-eyebrow">FINALS SYSTEM</div>
      <div class="wc-title">${w.label}</div>
      <div class="wc-sub">${w.sub}</div>
      <div class="wc-byes"><b>BYES</b> &middot; ${byeNames}</div>
      <div class="wc-cta">CHECK STATS &rarr;</div>
    </div>`;
  }).join('');
}

// ---------- WINDOW ----------
function goWindow(k){
  state.winKey = k; state.prelim=false; state.teamName=null; state.playerName=null;
  document.getElementById('winTitle').textContent = WINMETA[k].label;
  document.getElementById('winSub').textContent = WINMETA[k].sub.toUpperCase();
  renderByeStrip(k);
  renderPrelimToggle(k);
  renderRankTable(k,false);
  renderDeepDive(k);
  renderFlipFetchTable(k);
  setTab('stats');
  showView('window');
}
function renderByeStrip(k){
  const w = WINMETA[k];
  const chips = w.byes.map(b=>`<span class="bye-chip">RD <b>${b[0]}</b> &mdash; ${b[1].toUpperCase()}</span>`).join('');
  document.getElementById('byeStrip').innerHTML = `<span class="bye-lbl">TEAMS ON BYE</span>${chips}`;
}
function renderPrelimToggle(k){
  const w = WINMETA[k];
  const wrap = document.getElementById('prelimWrap');
  if(!w.hasPrelim){ wrap.innerHTML = ''; return; }
  wrap.innerHTML = `<span class="prelim-toggle">
    <button class="pt-btn ${!state.prelim?'active':''}" onclick="togglePrelim(false)">FULL WINDOW</button>
    <button class="pt-btn ${state.prelim?'active':''}" onclick="togglePrelim(true)">${w.prelimLabel.toUpperCase()}</button>
  </span>`;
}
function togglePrelim(v){
  state.prelim = v;
  renderPrelimToggle(state.winKey);
  renderRankTable(state.winKey, v);
}
function activeSosKey(winKey, prelim){
  return prelim ? WINMETA[winKey].prelimKey : winKey;
}
function renderRankTable(k, prelim){
  const sosKey = activeSosKey(k, prelim);
  const rows = SOSFULL[sosKey]['OVERALL'];
  document.querySelector('#rankTable tbody').innerHTML = rows.map(r=>`
    <tr class="clickable" onclick="goTeamByName('${r.team}')">
      <td class="rk ${rkTier(r.rank)}">${r.rank}</td>
      <td>${pillHtml(r.team)}</td>
      <td>${r.avg.toFixed(1)}</td>
      <td>${r.opp.toFixed(1)}</td>
      <td><span class="sos-pill ${sosTier(r.sos)}">${r.sos}</span></td>
    </tr>`).join('');
}
function chipHtml(team){
  if(team==='BYE' || team==='-') return `<span class="tchip" style="background:var(--surface);color:var(--muted)">BYE</span>`;
  const c = code(team);
  return `<span class="tchip tc-${c}">${c}</span>`;
}
function chipHtmlFull(team){
  if(team==='BYE' || team==='-') return `<span class="tchip-full" style="background:var(--surface);color:var(--muted)">BYE</span>`;
  const c = code(team);
  return `<span class="tchip-full tc-${c}">${team.toUpperCase()}</span>`;
}
function windowRounds(winKey){ return ((WINMETA[winKey]||{}).byes||[]).map(b=>b[0]); }
function drawGridHtml(draw, roundNums, bucket, concedePeriod){
  if(!draw) return `<div class="placeholder-note">Draw grid not confirmed for this team yet.</div>`;
  const rds = (roundNums && roundNums.length===draw.length) ? draw.map((d,i)=>`<div class="dg-rd">RD ${roundNums[i]}</div>`).join('') : '';
  const opps = draw.map(d=>`<div class="dg-opp">${chipHtmlFull(d[0])}</div>`).join('');
  const vens = draw.map(d=>`<div class="dg-ven ${d[1]==='-'?'bye':''}">${d[1]==='-'?'BYE':d[1]}</div>`).join('');
  let concedes = '';
  if(bucket){
    concedes = draw.map(d=>{
      if(d[0]==='-'||d[0]==='BYE') return `<div class="dg-concede bye">&ndash;</div>`;
      const hit = posConcedeLookup(bucket, d[0], concedePeriod);
      if(!hit) return `<div class="dg-concede">&ndash;</div>`;
      return `<div class="dg-concede"><span class="concede-pill ${concedeTier(hit.rank)}">${hit.avgConceded.toFixed(1)}</span></div>`;
    }).join('');
  }
  return `<div class="draw-grid" style="grid-template-columns:repeat(${draw.length},1fr)">${rds}${opps}${vens}${concedes}</div>`;
}
function concedeLegendHtml(bucket, concedePeriod){
  if(!bucket) return '';
  const period = concedePeriod || 'seasonAvg';
  const label = POS_LABELS[bucket] || bucket;
  return `<div class="sh" style="margin-top:14px">
    <div class="st" style="font-size:14px">CONCEDES TO ${label.toUpperCase()}</div>
    <div class="ss">AVG PTS OPPONENTS HAVE GIVEN UP TO THIS POSITION &mdash; ${period==='last6'?'LAST 6 ROUNDS':'SEASON AVERAGE'}</div>
  </div>
  <span class="prelim-toggle" style="margin-bottom:6px;display:inline-block">
    <button class="pt-btn ${period!=='last6'?'active':''}" onclick="setConcedePeriod('seasonAvg')">SEASON AVG</button>
    <button class="pt-btn ${period==='last6'?'active':''}" onclick="setConcedePeriod('last6')">LAST 6 RNDS</button>
  </span>`;
}
function setConcedePeriod(period){
  state.concedePeriod = period;
  if(state.drawCtx) renderPlayerDrawSection();
}
function renderPlayerDrawSection(){
  const ctx = state.drawCtx;
  if(!ctx) return;
  document.getElementById('playerDrawWrap').innerHTML = `
    <div class="sh" style="margin-top:18px"><div class="st" style="font-size:16px">${possessive(ctx.team.toUpperCase())} FINALS RUN</div><div class="ss">WHO THEY PLAY, HOME &amp; AWAY</div></div>
    ${drawGridHtml(ctx.draw, ctx.roundNums, ctx.bucket, state.concedePeriod)}
    ${concedeLegendHtml(ctx.bucket, state.concedePeriod)}`;
}
function posListHtml(pos){
  return `<div class="dd-pos-list">` + pos.map(p=>`
    <div class="dd-pos-card" onclick="goPlayer('${p[0]}', 'deep')">
      <div class="dd-pos-top">
        <span class="poslabel">${p[1]}</span>
        <span class="dd-pos-rank-badge">${p[2].toUpperCase()}</span>
      </div>
      <div class="pl-row">${playerAvatarHtml(p[0])}<span class="dd-pos-name">${p[0]}</span></div>
    </div>`).join('') + `</div>`;
}
function pickCardHtml(name, opts){
  opts = opts || {};
  const hit = findPlayerAcrossPositions(name);
  const team = opts.team || (hit ? hit.team : null);
  const pos = opts.pos || (hit ? hit.pos : '');
  const stats = PICKSTATS[name];
  return `<div class="pick-card" onclick="goPlayer('${name}', 'deep')">
    ${opts.rankNum ? `<span class="tc-rank pick-rank">${opts.rankNum}</span>` : ''}
    ${playerAvatarHtml(name)}
    <div class="pick-card-info">
      <div class="pick-card-name">${name}</div>
      <div class="pick-card-meta">${team?chipHtml(team):''}${pos?`<span class="pick-pos">${pos}</span>`:''}${opts.note?`<span class="tc-note">${opts.note}</span>`:''}</div>
      ${stats?`<div class="pick-card-extra">AVG <b>${stats.avg}</b> &middot; 3/5RD <b>${stats.r35}</b></div>`:''}
    </div>
  </div>`;
}
function renderDeepDive(k){
  const dd = DEEPDIVE[k];
  document.getElementById('topCards').innerHTML = dd.top.map(t=>`
    <div class="tcard gn">
      <div class="tcard-hd">
        <span class="tcard-rank-badge gn">SOS RANK #${t.rank}</span>
        ${pillHtml(t.team,`goTeamByName('${t.team}')`,'pill-md')}
      </div>
      ${drawGridHtml(t.draw, windowRounds(k))}
      ${posListHtml(t.pos)}
    </div>`).join('');
  hydrateAvatars(document.getElementById('topCards'));
  document.getElementById('worstCards').innerHTML = dd.worst.map(t=>`
    <div class="tcard rd">
      <div class="tcard-hd">
        <span class="tcard-rank-badge rd">SOS RANK #${t.rank}</span>
        ${pillHtml(t.team,`goTeamByName('${t.team}')`,'pill-md')}
      </div>
      ${drawGridHtml(t.draw, windowRounds(k))}
      ${posListHtml(t.pos)}
    </div>`).join('');
  hydrateAvatars(document.getElementById('worstCards'));
  function normalizePick(p){
  if (Array.isArray(p)) return {name:p[0], pos:p[1]};
  if (typeof p === 'object' && p !== null) return p;
  return {name:p};
}
function pickCardFromEntry(entry, extra){
  const o = normalizePick(entry);
  return pickCardHtml(o.name, Object.assign({pos:o.pos, team:o.team, note:o.note}, extra||{}));
}
document.getElementById('nattyChips').innerHTML = dd.nattyTargets.map(p=>pickCardFromEntry(p)).join('');
  hydrateAvatars(document.getElementById('nattyChips'));
  document.getElementById('wukaChips').innerHTML = (dd.wukaTargets||[]).map(p=>pickCardFromEntry(p)).join('');
  hydrateAvatars(document.getElementById('wukaChips'));
  document.getElementById('frothieChips').innerHTML = (dd.frothies||[]).map((p,i)=>pickCardFromEntry(p, {rankNum:i+1})).join('');
  hydrateAvatars(document.getElementById('frothieChips'));
  renderTradeCols(dd.struggleStreet, 'struggleCols');
  renderTradeCols(dd.topDogPlays, 'topdogCols');
  document.querySelector('#wireTable tbody').innerHTML = dd.wire.map(r=>`
    <tr>
      <td>${r.rttRank}</td><td>${r.rttSos}</td><td>${r.rttAvg}</td><td class="lbl">${pillHtml(r.team)}</td>
      <td class="wire-divider">${r.flag?`<span class="bdg ${r.flag==='FLIP'?'bdg-flip':'bdg-fetch'}">${r.flag}</span>`:''}</td>
      <td class="lbl">${pillHtml(r.fTeam)}</td><td>${r.fAvg}</td><td>${r.fOpp}</td><td>${r.fSos}</td><td>${r.fRank}</td>
    </tr>`).join('');
}
function renderTradeCols(w, elId){
  document.getElementById(elId).innerHTML = `
    <div class="trade-col sell">
      <div class="trade-hd">SELLING &mdash; ${w.selling.join(' / ').toUpperCase()}</div>
      ${w.sellingText.map(t=>`<div class="trade-line">${t}</div>`).join('')}
      <div class="trade-examples"><div class="trade-ex-lbl">EXAMPLES</div>${w.examples.map(e=>`<div class="trade-ex">${e}</div>`).join('')}</div>
    </div>
    <div class="trade-col buy">
      <div class="trade-hd">BUYING &mdash; ${w.buying.join(' / ').toUpperCase()}</div>
      ${w.buyingText.map(t=>`<div class="trade-line">${t}</div>`).join('')}
    </div>`;
}

// ---------- FLIP & FETCH TAB ----------
function flagBadge(flag){
  if(!flag) return '<span style="color:var(--muted)">&mdash;</span>';
  return `<span class="bdg ${flag==='FLIP'?'bdg-flip':'bdg-fetch'}">${flag}</span>`;
}
function renderFlipFetchTable(k){
  const rows = FLIPFETCH[k]['OVERALL'];
  document.querySelector('#ffRankTable tbody').innerHTML = rows.map(r=>`
    <tr class="clickable" onclick="goTeamFlipFetch('${r.team}')">
      <td class="rk ${rkTier(r.rttRank)}">${r.rttRank}</td>
      <td>${pillHtml(r.team)}</td>
      <td><span class="sos-pill ${sosTier(r.rttSos)}">${r.rttSos}</span></td>
      <td style="color:var(--muted)">&rarr;</td>
      <td class="rk ${rkTier(r.finalsRank)}">${r.finalsRank}</td>
      <td><span class="sos-pill ${sosTier(r.finalsSos)}">${r.finalsSos}</span></td>
      <td>${flagBadge(r.flag)}</td>
    </tr>`).join('');
}
function goTeamFlipFetch(teamName){
  state.teamName = teamName; state.teamContext = 'flipfetch'; state.playerName = null;
  document.getElementById('ffTeamTitle').innerHTML = pillHtml(teamName, null, 'pill-lg');
  const overall = FLIPFETCH[state.winKey]['OVERALL'].find(r=>teamEq(r.team,teamName));
  document.getElementById('ffTeamSub').textContent = overall
    ? `RTT RANK #${overall.rttRank} \u2192 FINALS RANK #${overall.finalsRank} ${overall.flag ? '\u00b7 '+overall.flag : ''}`
    : '';
  const rows = POS_ORDER.map(pos=>{
    const entry = FLIPFETCH[state.winKey][pos].find(r=>teamEq(r.team,teamName));
    return {pos, entry};
  });
  document.getElementById('ffTeamPosTable').innerHTML = rows.map(r=>{
    if(!r.entry) return `<div class="pos-card"><div class="pos-card-top"><span class="poslabel">${POS_LABELS[r.pos]}</span></div><div style="color:var(--muted);font-style:italic">No data</div></div>`;
    const e = r.entry;
    return `<div class="pos-card clickable" onclick="goPlayer('${e.player}')">
      <div class="pos-card-top">
        <span class="poslabel">${POS_LABELS[r.pos]}</span>
        <div class="pl-row">${playerAvatarHtml(e.player)}<span class="wire-player">${e.player}</span></div>
      </div>
      <div class="pos-card-stats">
        <div class="stat-item"><span class="stat-item-lbl">RTT Rank</span><span class="rk ${rkTier(e.rttRank)}">#${e.rttRank}</span></div>
        <div class="stat-item"><span class="stat-item-lbl">Finals Rank</span><span class="rk ${rkTier(e.finalsRank)}">#${e.finalsRank}</span></div>
        <div class="stat-item"><span class="stat-item-lbl">Flag</span>${flagBadge(e.flag) || '<span style="color:var(--muted)">&mdash;</span>'}</div>
      </div>
    </div>`;
  }).join('');
  hydrateAvatars(document.getElementById('ffTeamPosTable'));
  showView('team-ff');
}

// ---------- TABS ----------
document.querySelectorAll('.tab').forEach(t=>{
  t.addEventListener('click', ()=>setTab(t.dataset.tab));
});
function setTab(tab){
  document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('active', t.dataset.tab===tab));
  document.querySelectorAll('.panel').forEach(p=>p.classList.toggle('active', p.dataset.panel===tab));
}

// ---------- TEAM VIEW (full positional rank, from Stats tab) ----------
function goTeamByName(teamName){
  state.teamName = teamName; state.teamContext = 'stats'; state.teamPrelim = false; state.playerName = null;
  document.getElementById('teamBackBtn').onclick = ()=>showView('window');
  renderTeamView();
  showView('team');
}
function renderTeamPrelimToggle(){
  const w = WINMETA[state.winKey];
  const wrap = document.getElementById('teamPrelimWrap');
  if(!w.hasPrelim){ wrap.innerHTML=''; return; }
  wrap.innerHTML = `<span class="prelim-toggle">
    <button class="pt-btn ${!state.teamPrelim?'active':''}" onclick="toggleTeamPrelim(false)">FULL WINDOW</button>
    <button class="pt-btn ${state.teamPrelim?'active':''}" onclick="toggleTeamPrelim(true)">${w.prelimLabel.toUpperCase()}</button>
  </span>`;
}
function toggleTeamPrelim(v){ state.teamPrelim = v; renderTeamView(); }
function renderTeamView(){
  const sosKey = activeSosKey(state.winKey, state.teamPrelim);
  const overall = SOSFULL[sosKey]['OVERALL'].find(r=>teamEq(r.team,state.teamName));
  document.getElementById('teamTitle').innerHTML = pillHtml(state.teamName, null, 'pill-lg');
  document.getElementById('teamRankSub').textContent = overall
    ? `OVERALL SOS RANK #${overall.rank} \u00b7 AVG ${overall.avg.toFixed(1)} \u00b7 OPP CONCEDED ${overall.opp.toFixed(1)} \u00b7 SOS ${overall.sos}`
    : '';
  const tDraw = findTeamDraw(state.winKey, state.teamName);
  document.getElementById('teamDrawWrap').innerHTML = tDraw ? drawGridHtml(tDraw, windowRounds(state.winKey)) : '';
  renderTeamPrelimToggle();
  const rows = POS_ORDER.map(pos=>{
    const tbl = SOSFULL[sosKey][pos];
    const entry = tbl.find(r=>teamEq(r.team,state.teamName));
    return {pos, entry};
  });
  document.getElementById('teamPosTable').innerHTML = rows.map(r=>{
    if(!r.entry) return `<div class="pos-card"><div class="pos-card-top"><span class="poslabel">${POS_LABELS[r.pos]}</span></div><div style="color:var(--muted);font-style:italic">No data</div></div>`;
    const e = r.entry;
    return `<div class="pos-card clickable" onclick="goPlayer('${e.player}')">
      <div class="pos-card-top">
        <span class="poslabel">${POS_LABELS[r.pos]}</span>
        <div class="pl-row">${playerAvatarHtml(e.player)}<span class="wire-player">${e.player}</span></div>
      </div>
      <div class="pos-card-stats">
        <div class="stat-item"><span class="stat-item-lbl">Avg Score</span><span class="stat-item-val">${e.avg.toFixed(1)}</span></div>
        <div class="stat-item"><span class="stat-item-lbl">Opp Conceded</span><span class="stat-item-val">${e.opp.toFixed(1)}</span></div>
        <div class="stat-item"><span class="stat-item-lbl">SOS</span><span class="sos-pill ${sosTier(e.sos)}">${e.sos}</span></div>
        <div class="stat-item"><span class="stat-item-lbl">Rank</span><span class="rk ${rkTier(e.rank)}">#${e.rank}</span></div>
      </div>
    </div>`;
  }).join('');
  hydrateAvatars(document.getElementById('teamPosTable'));
}

// ---------- PLAYER VIEW ----------
function slugify(name){
  return name.toLowerCase().replace(/'/g,'').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
}
// Each entry below was individually verified by Claude by visiting that exact player's
// official NRL.com profile page and reading the photo URL straight out of the page's own
// <img>/og:image tag. This is a hotlink to NRL's own hosted image — nothing is downloaded
// or embedded here. Only add a player once you've actually checked their real page; do not
// guess slugs. Everyone not listed here falls back to initials.
const VERIFIED_PLAYER_PHOTOS = {
  "Jahream Bula": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Jahream%20Bula%20260106_MK1483.png?center=0.3%2C0.5&preset=share",
  "Apisai Koroisau": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Api%20Koroisau%20260106_MK1011.png?center=0.3%2C0.5&preset=share",
  "Starford Toa": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Star%20To%27a%20260106_MK1248.png?center=0.3%2C0.5&preset=share",
  "Patrick Herbert": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Patrick%20Herbert%2014760.png?center=0.3%2C0.5&preset=share",
  "Sione Fainu": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Sione_Fainu_11.png?center=0.3%2C0.5&preset=share",
  "Tony Sukkar": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Tanous%20Sukkar%20260106_MK1921.png?center=0.3%2C0.5&preset=share",
  "Sunia Turuva": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Sunia%20Turuva%20260106_MK1098.png?center=0.3%2C0.5&preset=share",
  "Tom Trbojevic": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Tom%20Trbojevic_260128_SeaEgales_MK1441.png?center=0.3%2C0.5&preset=share",
  "Lehi Hopoate": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Lehi%20Hopoate%20_260128_SeaEgales_MK395.png?center=0.3%2C0.5&preset=share",
  "Haumole Olakauatu": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Haumole%20Olakauatu%20_260128_SeaEgales_MK1679.png?center=0.3%2C0.5&preset=share",
  "William Kennedy": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Will%20Kennedy_260114_Sharks_MK789a.png?center=0.3%2C0.5&preset=share",
  "Sione Katoa": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2025/500028/Katoa%2CS%20250117_BC_2746-COPY.png?center=0.3%2C0.5&preset=share",
  "Kayal Iro": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/KL%20Iro_260114_Sharks_MK375a.png?center=0.3%2C0.5&preset=share",
  "Teig Wilton": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Teig%20Wilton_260114_Sharks_MK207.png?center=0.3%2C0.5&preset=share",
  "Braydon Trindall": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Braydon%20Trindall_260114_Sharks_MK032.png?center=0.3%2C0.5&preset=share",
  "Jesse Ramien": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Jesse%20Ramien_260114_Sharks_MK1804.png?center=0.3%2C0.5&preset=share",
  "Cameron McInnes": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Cam%20Mcinnes_260114_Sharks_MK665.png?center=0.3%2C0.5&preset=share",
  "Niwhai Puru": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Niwhai%20Puru_260114_Sharks_MK006.png?center=0.3%2C0.5&preset=share",
  "Jayden Berrell": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Jayden%20Berrell_260114_Sharks_MK944.png?center=0.3%2C0.5&preset=share",
  "Cameron Munster": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Munster%2CC_260204_AR_3.png?center=0.3%2C0.5&preset=share",
  "Moses Leo": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Leo%2CM_260204_AR_3.png?center=0.3%2C0.5&preset=share",
  "Ativalu Lisati": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Lisati%2CA_260204_AR_4.png?center=0.3%2C0.5&preset=share",
  "Jahrome Hughes": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Hughes%2CJ_260204_AR_2.png?center=0.3%2C0.5&preset=share",
  "Sua Faalogo": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Fa%27alogo%2CS_260204_AR_3.png?center=0.3%2C0.5&preset=share",
  "William Warbrick": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Warbrick%2CW_260204_AR_4.png?center=0.3%2C0.5&preset=share",
  "Trent Loiero": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Loiero%2CT_260204_AR_3.png?center=0.3%2C0.5&preset=share",
  "Harry Grant": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Grant%2CH_260204_AR_18.png?center=0.3%2C0.5&preset=share",
  "Cooper Clarke": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Clarke%2CC_260204_AR_2.png?center=0.3%2C0.5&preset=share",
  "Joe Chan": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Chan%2CJ_260204_AR_14.png?center=0.3%2C0.5&preset=share",
  "Jack Howarth": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Howarth%2CJ_260204_AR_2.png?center=0.3%2C0.5&preset=share",
  "Jarome Luai": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Jarome%20Luai%20260106_MK169-2.png?center=0.3%2C0.5&preset=share",
  "Alex Seyfarth": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Alex%20Seyfarth%20260106_MK667.png?center=0.3%2C0.5&preset=share",
  "Jock Madden": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Jock%20Madden%20260106_MK440.png?center=0.3%2C0.5&preset=share",
  "Taylan May": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Taylan%20May%20260106_MK1189.png?center=0.3%2C0.5&preset=share",
  "Josh Addo-Carr": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/ADDO-CARR%2CJ_20251211_1064.png?center=0.3%2C0.5&preset=share",
  "Joash Papalii": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/Papali%27i%2C%20Joash%20-%20EELS%2C%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Kitione Kautoga": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/KAUTOGA%2CK_20251211_2279.png?center=0.3%2C0.5&preset=share",
  "Isaiah Iongi": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/IONGI%2CI_20251211_2189.png?center=0.3%2C0.5&preset=share",
  "Brian Kelly": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/KELLY%2C%20BRIAN%20-%20EELS%2C%20HEADSHOT.png?center=0.3%2C0.5&preset=share",
  "Kelma Tuilagi": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/TUILAGI%2CK_20251211_1690.png?center=0.3%2C0.5&preset=share",
  "Ronald Volkman": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/VOLKMAN%2CR_20251211_1137.png?center=0.3%2C0.5&preset=share",
  "Sean Russell": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/RUSSELL%2CS_20251211_2465-COPY.png?center=0.3%2C0.5&preset=share",
  "Tallyn DaSilva": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/DA%20SILVA%2CT_20251211_1957-COPY.png?center=0.3%2C0.5&preset=share",
  "Jordan Samrani": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/SAMRANI%2CJ_20251211_1728.png?center=0.3%2C0.5&preset=share",
  "Jack deBelin": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/DE%20BELIN%2CJ_20251211_1895.png?center=0.3%2C0.5&preset=share",
  "Reuben Cotter": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Cotter%2CR%20260109_CD_0826.JPG.png?center=0.3%2C0.5&preset=share",
  "Braidon Burns": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Burns%2CB%20260109_CD_1790.JPG.png?center=0.3%2C0.5&preset=share",
  "Jake Clifford": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Clifford%2CJ%20260109_CD_0637.JPG.png?center=0.3%2C0.5&preset=share",
  "Jaxon Purdue": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Purdue%2CJ%20260109_CD_1198.JPG.png?center=0.3%2C0.5&preset=share",
  "Zac Laybutt": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Laybutt%2CZ%20260109_CD_2232.JPG.png?center=0.3%2C0.5&preset=share",
  "Murray Taulagi": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Taulagi%2CM%20260109_CD_0911.JPG.png?center=0.3%2C0.5&preset=share",
  "Scott Drinkwater": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Drinkwater%2CS%20260109_CD_0729.JPG.png?center=0.3%2C0.5&preset=share",
  "Tom Chester": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Chester%2CT%20260109_CD_1486.JPG.png?center=0.3%2C0.5&preset=share",
  "Jeremiah Nanai": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Nanai%2CJ%20260109_CD_1685.JPG.png?center=0.3%2C0.5&preset=share",
  "Heilum Luki": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Luki%2CH%20260109_CD_1403.JPG.png?center=0.3%2C0.5&preset=share",
  "Reed Mahoney": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Mahoney%2CR%20260109_CD_1311.JPG.png?center=0.3%2C0.5&preset=share",
  "Hudson Young": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Hudson%20Young%20_260121_Raiders_MK1989.png?center=0.3%2C0.5&preset=share",
  "Zac Hosking": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Zac%20Hosking_260121_Raiders_MK161.png?center=0.3%2C0.5&preset=share",
  "Ethan Strange": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Ethan%20Strange%20_260121_Raiders_MK2161.png?center=0.3%2C0.5&preset=share",
  "Sebastian Kris": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Sebastian%20Kris%20_260121_Raiders_MK356.png?center=0.3%2C0.5&preset=share",
  "Savelio Tamale": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Savelio%20Tamale%20_260121_Raiders_MK2380.png?center=0.3%2C0.5&preset=share",
  "Kaeo Weekes": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Kaeo%20Weekes%20_260121_Raiders_MK1349.png?center=0.3%2C0.5&preset=share",
  "Xavier Savage": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Xavier%20Savage%20_260121_Raiders_MK062.png?center=0.3%2C0.5&preset=share",
  "Jayden Brailey": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Jayden%20Brailey%20_260121_Raiders_MK723.png?center=0.3%2C0.5&preset=share",
  "Tom Starling": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Tom%20Starling%20_260121_Raiders_MK2072.png?center=0.3%2C0.5&preset=share",
  "Ethan Sanders": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Ethan%20Sanders%20_260121_Raiders_MK1832.png?center=0.3%2C0.5&preset=share",
  "Matthew Timoko": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Matt%20Timoko%20_260121_Raiders_MK288.png?center=0.3%2C0.5&preset=share",
  "Dylan Edwards": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Dylan%20Edwards%20_260123_Panthers_MK2086.png?center=0.3%2C0.5&preset=share",
  "Freddy Lussick": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Freddy%20Lussick%20_260123_Panthers_MK449.png?center=0.3%2C0.5&preset=share",
  "Liam Martin": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Liam%20Martin%20_260123_Panthers_MK1012.png?center=0.3%2C0.5&preset=share",
  "Isaiah Papalii": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Isaiah%20Papali%E2%80%99i%20_260123_Panthers_MK2347.png?center=0.3%2C0.5&preset=share",
  "Lindsay Smith": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Lindsay%20Smith%20_260123_Panthers_MK950.png?center=0.3%2C0.5&preset=share",
  "Paul Alamoti": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Paul%20Alamoti%20_260123_Panthers_MK1222.png?center=0.3%2C0.5&preset=share",
  "Blaize Talagi": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Blaize%20Talagi%20_260123_Panthers_MK1291.png?center=0.3%2C0.5&preset=share",
  "Thomas Jenkins": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Tom%20Jenkins%20_260123_Panthers_MK004.png?center=0.3%2C0.5&preset=share",
  "Luke Garner": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Luke%20Garner%20_260123_Panthers_MK1889.png?center=0.3%2C0.5&preset=share",
  "Izack Tago": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Izack%20Tago%20_260123_Panthers_MK1983.png?center=0.3%2C0.5&preset=share",
  "Jack Cogger": "https://www.penrithpanthers.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Jack%20Cogger%20_260123_Panthers_MK816.png?center=0.3%2C0.5&preset=share",
  "Reece Walsh": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Walsh.png?center=0.3%2C0.5&preset=share",
  "Adam Reynolds": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Reynolds%2CA%20Headshot%2014.png?center=0.3%2C0.5&preset=share",
  "Tom Duffy": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Duffy.png?center=0.3%2C0.5&preset=share",
  "Jesse Arthars": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Arthars%2CJ%20Headshot%2011.png?center=0.3%2C0.5&preset=share",
  "Josiah Karapani": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Karapani.png?center=0.3%2C0.5&preset=share",
  "Jordan Riki": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Riki.png?center=0.3%2C0.5&preset=share",
  "Grant Anderson": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Anderson.png?center=0.3%2C0.5&preset=share",
  "Kotoni Staggs": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Staggs%2CK%20Headshot%2008.png?center=0.3%2C0.5&preset=share",
  "Brendan Piakura": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Piakura%2CB%20Headshot%2011.png?center=0.3%2C0.5&preset=share",
  "Xavier Willison": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Willison%2CX%20Headshot%2011.png?center=0.3%2C0.5&preset=share",
  "Cory Paix": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/Paix%2CC%20Headshot%2013.png?center=0.3%2C0.5&preset=share",
  "James Tedesco": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/James%20Tedesco%20260203_Roosters813.png?center=0.3%2C0.5&preset=share",
  "Mark Nawaqanitawase": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Mark%20Nawaqanitawase%20260203_Roosters96.png?center=0.3%2C0.5&preset=share",
  "Billy Smith": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Billy%20Smith%20260203_Roosters148.png?center=0.3%2C0.5&preset=share",
  "Daly Cherry-Evans": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Daly%20Cherry-Evans%20260203_Roosters313.png?center=0.3%2C0.5&preset=share",
  "Victor Radley": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Victor%20Radiey%20260203_Roosters680.png?center=0.3%2C0.5&preset=share",
  "Angus Crichton": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Angus%20Crichton%20260203_Roosters1332.png?center=0.3%2C0.5&preset=share",
  "Reece Robson": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Reece%20Robson%20260203_Roosters1449.png?center=0.3%2C0.5&preset=share",
  "Tommy Talau": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Tommy%20Talau%20260203_Roosters55.png?center=0.3%2C0.5&preset=share",
  "Sam Walker": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2025/500001/WALKER%2CS%20NRL_2025_7170.png?center=0.3%2C0.5&preset=share",
  "Robert Toia": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Rob%20Toia%20260203_Roosters1729.png?center=0.3%2C0.5&preset=share",
  "Siua Wong": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2025/500001/WONG%2CS%20NRL_2025_6735.png?center=0.3%2C0.5&preset=share",
  "Chanel Harris-Tavita": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Chanel%20Harris-Tavita_003.png?center=0.3%2C0.5&preset=share",
  "Charnze Nicoll-Klokstad": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Charnze%20Nicoll-Klokstad_003.png?center=0.3%2C0.5&preset=share",
  "Erin Clark": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Erin%20Clark-004.png?center=0.3%2C0.5&preset=share",
  "Jacob Laban": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Jacob%20Laban-004.png?center=0.3%2C0.5&preset=share",
  "Ali Leiataua": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Ali%20Leiataua-003.png?center=0.3%2C0.5&preset=share",
  "Taine Tuaupiki": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Taine%20Tuaupiki-004.png?center=0.3%2C0.5&preset=share",
  "Marata Niukore": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Marata%20Niukore_003.png?center=0.3%2C0.5&preset=share",
  "Dallin Watene-Zelezniak": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Dallin%20Watene-Zelezniak-003.png?center=0.3%2C0.5&preset=share",
  "Adam Pompey": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Adam%20Pompey-004.png?center=0.3%2C0.5&preset=share",
  "TeMaire Martin": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Te%20Maire%20Martin-004.png?center=0.3%2C0.5&preset=share",
  "Wayde Egan": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Wayde%20Egan_007.png?center=0.3%2C0.5&preset=share",
  "Stephen Crichton": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/CRICHTON%2CS_20251212_3377.png?center=0.3%2C0.5&preset=share",
  "Matt Burton": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/BURTON%2CM_20251212_3199.png?center=0.3%2C0.5&preset=share",
  "Jaeman Salmon": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/SALMON%2CJ_20251212_3610.png?center=0.3%2C0.5&preset=share",
  "Harry Hayes": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/HAYES%2CH_20251212_3724.png?center=0.3%2C0.5&preset=share",
  "Jacob Kiraz": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2025/500010/KIRAZ%2CJacob_NRL_2025_GP00001-COPY.png?center=0.3%2C0.5&preset=share",
  "Sitili Tupouniua": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/TUPOUNIUA%2CS_20251212_3846.png?center=0.3%2C0.5&preset=share",
  "Kurt Mann": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/MANN%2CK_20251212_3445.png?center=0.3%2C0.5&preset=share",
  "Enari Tuala": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/TUALA%2CE_20251212_3659.png?center=0.3%2C0.5&preset=share",
  "Connor Tracey": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/TRACEY%2CC_20251212_4147.png?center=0.3%2C0.5&preset=share",
  "Jethro Rinakama": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/RINAKAMA%2CJ_20251212_2781.png?center=0.3%2C0.5&preset=share",
  "Lachlan Galvin": "https://www.bulldogs.com.au/contentassets/d273071a05924d229208b444f35779f2/galvin-headshot.png?center=0.3%2C0.52&preset=player-profile-small",
  "Cameron Murray": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Cameron%20Murray_260113_Rabbitohs_MK0101.png?center=0.3%2C0.5&preset=share",
  "David Fifita": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Fifita%2C%20David%20-%20Souths%2C%20Headshot%281%29.png?center=0.3%2C0.5&preset=share",
  "Cody Walker": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Cody%20Walker_260113_Rabbitohs_MK0220.png?center=0.3%2C0.5&preset=share",
  "Ashton Ward": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Ashton%20Ward_260113_Rabbitohs_MK1423.png?center=0.3%2C0.5&preset=share",
  "Tallis Duncan": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Tallis%20Duncan_260115_Rabbitohs194.png?center=0.3%2C0.5&preset=share",
  "Latrell Siegwalt": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Seigwalt%2C%20Latrell%20-%20Souths%2C%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Alex Johnston": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Alex%20Johnston_260113_Rabbitohs_MK0562.png?center=0.3%2C0.5&preset=share",
  "Jye Gray": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Jye%20Gray_260115_Rabbitohs_MK003.png?center=0.3%2C0.5&preset=share",
  "Brandon Smith": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Brandon%20Smith_260113_Rabbitohs_MK1562.png?center=0.3%2C0.5&preset=share",
  "Edward Kosi": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500005/Ed%20Kosi_260115_Rabbitohs745.png?center=0.3%2C0.5&preset=share",
  "Euan Aitken": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2025/500005/AITKEN%2CE_2025_NRL_5891.png?center=0.3%2C0.5&preset=share",
  "Valentine Holmes": "https://www.dragons.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Valentine%20Holmes%20_260119_Dragons_MK1700.png?center=0.3%2C0.5&preset=share",
  "Dylan Egan": "https://www.dragons.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Dylan%20Egan%20_260119_Dragons_MK1380.png?center=0.3%2C0.5&preset=share",
  "Setu Tu": "https://www.dragons.com.au/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Setu%20Tu%20_260119_Dragons_MK363.png?center=0.3%2C0.5&preset=share",
  "Hamish Stewart": "https://www.dragons.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Hamish%20Stewart%20_260119_Dragons_MK1499.png?center=0.3%2C0.5&preset=share",
  "Moses Suli": "https://www.dragons.com.au/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Moses%20Suli%20_260119_Dragons_MK561.png?center=0.3%2C0.5&preset=share",
  "Damien Cook": "https://www.dragons.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Damien%20Cook%20_260119_Dragons_MK914.png?center=0.3%2C0.5&preset=share",
  "Ryan Couchman": "https://www.dragons.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Ryan%20Couchman%20_260119_Dragons_MK001.png?center=0.3%2C0.5&preset=share",
  "Tyrell Sloan": "https://www.dragons.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Tyrell%20Sloan%20_260119_Dragons_MK618.png?center=0.3%2C0.5&preset=share",
  "Daniel Atkinson": "https://www.dragons.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Daniel%20Atkinson%20_260119_Dragons_MK1444.png?center=0.3%2C0.5&preset=share",
  "Clint Gutherson": "https://www.dragons.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Clint%20Gutherson%20_260119_Dragons_MK1077.png?center=0.3%2C0.5&preset=share",
  "Kyle Flanagan": "https://www.dragons.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Kyle%20Flanagan%20_260119_Dragons_MK1246.png?center=0.3%2C0.5&preset=share",
  "Kalyn Ponga": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Kalyn%20Ponga%20_260129_Knights_MK725.png?center=0.3%2C0.5&preset=share",
  "Bradman Best": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Bradman%20Best%20_260129_Knights_MK222.png?center=0.3%2C0.5&preset=share",
  "Thomas Cant": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Thomas%20Cant%20_260129_Knights_MK681.png?center=0.3%2C0.5&preset=share",
  "Dane Gagai": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Dane%20Gagai%20_260129_Knights_MK1405.png?center=0.3%2C0.5&preset=share",
  "Dominic Young": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Dominic%20Young%20_260129_Knights_MK885.png?center=0.3%2C0.5&preset=share",
  "Dylan Brown": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Dylan%20Brown%20_260129_Knights_MK1866.png?center=0.3%2C0.5&preset=share",
  "Greg Marzhew": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Greg%20Marzhew%20_260129_Knights_MK1584.png?center=0.3%2C0.5&preset=share",
  "Francis Manuleleua": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Francis%20Manuleleua%20_260129_Knights_MK439.png?center=0.3%2C0.5&preset=share",
  "Fletcher Sharpe": "https://www.newcastleknights.com.au/contentassets/c07be5d44dc543a09ef9e61ca5476540/sharpe-website-head.png?center=0.38%2C0.5&preset=player-profile-small",
  "Matt Croker": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Mathew%20Croker%20_260129_Knights_MK795.png?center=0.3%2C0.5&preset=share",
  "Phoenix Crossland": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Phoenix%20Crossland%20_260129_Knights_MK1521.png?center=0.3%2C0.5&preset=share",
  "Jayden Campbell": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/CAMPBELL%2C%20Jayden%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Zane Harrison": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/HARRISON%2C%20Zane%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Oliver Pascoe": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/PASCOE%2C%20Oliver%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Alexander Brimson": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/BRIMSON%2C%20AJ%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Arama Hau": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/HAU%2C%20Arama%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Beau Fermor": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/FERMOR%2C%20Beau%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Cooper Bai": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/BAI%2C%20Cooper%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Jojo Fifita": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/FIFITA%2C%20Jojo%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Keano Kini": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/KINI%2C%20Keano%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Jensen Taumoepeau": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/TAUMOEPEAU%2C%20Jensen%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Phillip Sami": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/SAMI%2C%20Phil%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Isaiya Katoa": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Katoa.png?center=0.3%2C0.5&preset=share",
  "Herbie Farnworth": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Farnworth.png?center=0.3%2C0.5&preset=share",
  "Jack Bostock": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Bostock.png?center=0.3%2C0.5&preset=share",
  "Jamayne Isaako": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Isaako.png?center=0.3%2C0.5&preset=share",
  "Kodi Nikorima": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Nikorima.png?center=0.3%2C0.5&preset=share",
  "Trai Fuller": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Fuller.png?center=0.3%2C0.5&preset=share",
  "Morgan Knowles": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Knowles.png?center=0.3%2C0.5&preset=share",
  "Connelly Lemuelu": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Lemuelu.png?center=0.3%2C0.5&preset=share",
  "Hamiso Tabuai-Fidow": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-TabuaiFidow.png?center=0.3%2C0.5&preset=share",
  "Selwyn Cobbo": "https://www.dolphinsnrl.com.au/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Cobbo.png?center=0.3%2C0.5&preset=share",
  "Kulikefu Finefeuiaki": "https://www.dolphinsnrl.com.au/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Finefeuiaki.png?center=0.3%2C0.5&preset=share",
  "Jeral Skelton": "https://www.weststigers.com.au/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Jeral%20Skelton%20260106_MK2267.png?center=0.3%2C0.5&preset=share",
  "Adam Doueihi": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Adam%20Doueihi%20260106_MK365.png?center=0.3%2C0.5&preset=share",
  "Alex Twal": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Alex%20Twal%20260106_MK776-21.png?center=0.3%2C0.5&preset=share",
  "Nicholas Hynes": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Nicho%20Hynes_260114_Sharks_MK1633.png?center=0.3%2C0.5&preset=share",
  "Blayke Brailey": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Blayke%20Brailey_260114_Sharks_MK1512.png?center=0.3%2C0.5&preset=share",
  "Nathan Cleary": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Nathan%20Cleary%20_260123_Panthers_MK1836.png?center=0.3%2C0.5&preset=share",
  "Isaah Yeo": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Isaah%20Yeo%20_260123_Panthers_MK886.png?center=0.3%2C0.5&preset=share",
  "Brian Too": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500014/Brian%20To%E2%80%99o%20_260123_Panthers_MK1706.png?center=0.3%2C0.5&preset=share",
  "Ben Hunt": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500011/B%20Hunt.png?center=0.3%2C0.5&preset=share",
  "Chris Randall": "https://www.titans.com.au/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/RANDALL%2C%20Chris%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Jaylan deGroot": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500004/DE%20GROOT%2C%20Jaylan%20-%20Headshot.png?center=0.3%2C0.5&preset=share",
  "Dylan Lucas": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Dylan%20Lucas%20_260129_Knights_MK1927.png?center=0.3%2C0.5&preset=share",
  "Jermaine McEwen": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500003/Jermain%20McEwan%20_260129_Knights_MK497.png?center=0.3%2C0.5&preset=share",
  "Hugo Savala": "https://www.roosters.com.au/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Hugo%20Savala%20260203_Roosters1064.png?center=0.3%2C0.5&preset=share",
  "Nat Butcher": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500001/Nat%20Butcher%20260203_Roosters874.png?center=0.3%2C0.5&preset=share",
  "Jake Simpkin": "https://www.seaeagles.com.au/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Jake%20Simpkin%20_260128_SeaEgales_MK1108.png?center=0.3%2C0.5&preset=share",
  "Josh Feledy": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Josh%20Feledy%20_260128_SeaEgales_MK651.png?center=0.3%2C0.5&preset=share",
  "Joshua Curran": "https://www.bulldogs.com.au/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/CURRAN%2CJ_20251212_4081.png?center=0.3%2C0.5&preset=share",
  "Kurt Capewell": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500032/Kurt%20Capewell_004.png?center=0.3%2C0.5&preset=share",
  "Mathew Feagai": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500022/Mathew%20Feagai%20_260119_Dragons_MK771.png?center=0.3%2C0.5&preset=share",
  "Mitchell Moses": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500031/MOSES%2CM_20251211_1643.png?center=0.3%2C0.5&preset=share",
  "Owen Pattie": "https://www.raiders.com.au/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Owen%20Pattie%20_260121_Raiders_MK943.png?center=0.3%2C0.5&preset=share",
  "Simi Sasagi": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500013/Simi%20Sasagi%20_260121_Raiders_MK803.png?center=0.3%2C0.5&preset=share",
  "Tyran Wishart": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500021/Wishart%2CT__260204_AR_3.png?center=0.3%2C0.5&preset=share",
  "Tevita Naufahu": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Naufahu.png?center=0.3%2C0.5&preset=share",
  "Oryn Keeley": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Keeley.png?center=0.3%2C0.5&preset=share",
  "Jeremy Marshall-King": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-MarshallKing.png?center=0.3%2C0.5&preset=share",
  "Ronaldo Mulitalo": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Ronaldo%20Mulitalo_260114_Sharks_MK1178a.png?center=0.3%2C0.5&preset=share",
  "Briton Nikora": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/Briton%20Nikora_260114_Sharks_MK150.png?center=0.3%2C0.5&preset=share",
  "Brandon Wakeham": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Brandon_Wakeham_744.png?center=0.3%2C0.5&preset=share",
  "Jamal Fogarty": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Jamal%20Fogarty%20_260128_SeaEgales_MK044.png?center=0.3%2C0.5&preset=share",
  "Tolutau Koula": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Tolu%20Koula%20_260128_SeaEgales_MK2447.png?center=0.3%2C0.5&preset=share",
  "Ben Trbojevic": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Ben%20Trbojevic%20_260128_SeaEgales_MK1909.png?center=0.3%2C0.5&preset=share",
  "Reuben Garrick": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Reuben%20Garrick%20_260128_SeaEgales_MK085.png?center=0.3%2C0.5&preset=share",
  "Jake Trbojevic": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Jake%20Trbojevic%20_260128_SeaEgales_MK2030.png?center=0.3%2C0.5&preset=share",
  "Jason Saab": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Jason%20Saab%20_260128_SeaEgales_MK219.png?center=0.3%2C0.5&preset=share",
  "Luke Brooks": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500002/Luke%20Brooks%20_260128_SeaEgales_MK004.png?center=0.3%2C0.5&preset=share",
  "Samuela Fainu": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500023/Samuela%20Fainu%20260106_MK2345.png?center=0.3%2C0.5&preset=share",
  "KL Iro": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500028/KL%20Iro_260114_Sharks_MK375a.png?center=0.3%2C0.5&preset=share",
  "Viliame Kikau": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500010/KIKAU%2CV_20251212_3909.png?center=0.3%2C0.5&preset=share",
  "Tom Gilbert": "https://www.nrl.com/remote.axd?http://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500723/Headshot-Gilbert.png?center=0.3%2C0.5&preset=share",
  "Tom Dearden": "https://www.nrl.com/remote.axd?https://rugbyimages.statsperform.com/Player%20Profile%20Headshots/111/2026/500012/Dearden%2CT%20260109_CD_0477.JPG.png?center=0.3%2C0.5&preset=share",
};
// Per-player object-position overrides for the circular avatar crop.
// Default crop (no entry here) is "top center" via CSS (.pl-avatar img).
// Populated from manual review using the photo crop audit tool — add to this
// as more players are checked.
const PHOTO_POSITION_OVERRIDES = {
  "Kaeo Weekes": "58% 0%",
  "Kitione Kautoga": "54% 0%",
  "KL Iro": "54% 0%",
  "Luke Brooks": "58% 0%",
  "Luke Garner": "46% 0%",
  "Matthew Timoko": "58% 0%",
  "Mitchell Moses": "42% 0%",
  "Moses Suli": "54% 0%",
  "Nicholas Hynes": "46% 0%",
  "Patrick Herbert": "46% 0%",
  "Reuben Cotter": "42% 0%",
  "Reece Robson": "62% 0%",
  "Robert Toia": "46% 0%",
  "Ronald Volkman": "46% 0%",
  "Ronaldo Mulitalo": "58% 0%",
  "Ryan Couchman": "58% 0%",
  "Scott Drinkwater": "46% 0%",
  "Savelio Tamale": "46% 0%",
  "Sione Katoa": "62% 0%",
  "Sitili Tupouniua": "46% 0%",
  "Taine Tuaupiki": "46% 0%",
  "Taylan May": "58% 0%",
  "Tom Chester": "46% 0%",
  "Tom Dearden": "46% 0%",
  "Tom Trbojevic": "54% 0%",
  "Tommy Talau": "54% 0%",
  "Valentine Holmes": "58% 0%",
  "Victor Radley": "46% 0%",
  "William Warbrick": "42% 0%",
  "Wayde Egan": "38% 0%",
  "Zane Harrison": "46% 0%",
  "Zac Laybutt": "46% 0%",
  "Zac Hosking": "58% 0%",
};
function playerAvatarHtml(name){
  const initials = name.split(' ').map(n=>n[0]).join('').slice(0,2);
  return `<span class="pl-avatar" data-player="${name}">${initials}</span>`;
}
function hydrateAvatars(root){
  if(!root) return;
  root.querySelectorAll('.pl-avatar[data-player]').forEach(el=>{
    loadPlayerPhoto(el, el.dataset.player);
  });
}
function swapInPhoto(el, url, name){
  if(el.dataset.photoFor !== name) return; // user navigated away before this load finished
  el.innerHTML = '';
  const photo = document.createElement('img');
  photo.src = url;
  const posOverride = PHOTO_POSITION_OVERRIDES[name];
  if(posOverride) photo.style.objectPosition = posOverride;
  el.appendChild(photo);
}
function loadPlayerPhoto(el, name){
  el.dataset.photoFor = name;
  const url = VERIFIED_PLAYER_PHOTOS[name];
  if(!url) return; // not yet verified — leave initials showing
  // primary attempt: NRL's own resizing proxy (cropped headshot)
  const img = new Image();
  img.onload = function(){ swapInPhoto(el, url, name); };
  img.onerror = function(){
    // fallback: if NRL's remote.axd proxy blocks the request (hotlink protection),
    // try the raw statsperform CDN source directly (uncropped, but still a real photo)
    const m = url.match(/remote\.axd\?(https?:\/\/[^?]+)/);
    if(!m){ return; } // no fallback URL available — leave initials showing
    const directUrl = m[1];
    const img2 = new Image();
    img2.onload = function(){ swapInPhoto(el, directUrl, name); };
    img2.onerror = function(){ /* both sources failed — leave initials showing */ };
    img2.src = directUrl;
  };
  img.src = url;
}
function findPlayerAcrossPositions(name){
  // search current window's full SOS data (current prelim state) for this player
  const sosKey = activeSosKey(state.winKey, state.teamPrelim || state.prelim);
  for(const pos of POS_ORDER){
    const hit = SOSFULL[sosKey][pos].find(r=>r.player===name);
    // NOTE: hit.pos (raw SC position e.g. "CTW") intentionally overwrites the outer
    // `pos` for backwards compatibility with existing display code. The bucket key
    // (LW/RW/LC/RC/etc — needed to look up positional concede data) is preserved
    // separately under `bucket` so it survives the spread below.
    if(hit) return {pos, bucket:pos, ...hit};
  }
  return null;
}
const POSCONCEDING = DATA.posConceding || {seasonAvg:{}, last6:{}};
function posConcedeLookup(bucket, teamName, period){
  const tbl = (POSCONCEDING[period||'seasonAvg']||{})[bucket];
  if(!tbl) return null;
  return tbl.find(r=>teamEq(r.team, teamName)) || null;
}
function concedeTier(rank){
  // inverted vs rkTier: for an ATTACKING matchup, a team ranked near the bottom
  // of "points conceded" (i.e. they leak a lot to this position) is a GOOD/juicy
  // matchup, so high rank numbers get the favourable colour.
  if(rank>=15) return 'sos-hi';
  if(rank<=3) return 'sos-lo';
  return 'sos-mid';
}
function findTeamOverall(teamName){
  const sosKey = activeSosKey(state.winKey, state.teamPrelim || state.prelim);
  return SOSFULL[sosKey]['OVERALL'].find(r=>teamEq(r.team,teamName));
}
function goPlayer(name, backTo){
  state.playerName = name;
  state.playerBackTo = backTo || (state.teamContext==='flipfetch' ? 'team-ff' : 'team');
  const backBtn = document.getElementById('playerBackBtn');
  if(state.playerBackTo === 'deep'){
    backBtn.innerHTML = '&larr; BACK';
    backBtn.onclick = ()=>{ showView('window'); setTab('deep'); };
  } else {
    backBtn.innerHTML = '&larr; BACK TO TEAM';
    backBtn.onclick = ()=>showView(state.playerBackTo);
  }
  const lookupName = NAME_ALIASES[name] || name;
  const p = PLAYERS[lookupName];
  document.getElementById('playerName').textContent = name.toUpperCase();
  const avatar = document.getElementById('playerAvatar');
  avatar.innerHTML = name.split(' ').map(n=>n[0]).join('').slice(0,2);
  loadPlayerPhoto(avatar, name);

  const sosHit = findPlayerAcrossPositions(lookupName);
  const manual = MANUAL_PROFILES[name];

  if(p){
    // full SC profile available (price/BE/PPM/draw)
    state.drawCtx = null;
    document.getElementById('playerMeta').innerHTML = `${pillHtml(p.team)}<span>${p.pos}</span>`;
    document.getElementById('playerStats').innerHTML = `
      <div class="stat-box"><div class="stat-val">$${(p.price/1000).toFixed(1)}k</div><div class="stat-lbl">PRICE</div></div>
      <div class="stat-box"><div class="stat-val">${p.be}</div><div class="stat-lbl">~BE</div></div>
      <div class="stat-box"><div class="stat-val">${p.pts}</div><div class="stat-lbl">AVG PTS</div></div>
      <div class="stat-box"><div class="stat-val">${p.mins}</div><div class="stat-lbl">MINS</div></div>
      <div class="stat-box"><div class="stat-val">${p.r35}</div><div class="stat-lbl">3/5RD</div></div>
      <div class="stat-box"><div class="stat-val">${p.ppm}</div><div class="stat-lbl">PPM</div></div>
      <div class="stat-box"><div class="stat-val">$${p.perPt}</div><div class="stat-lbl">$/PT</div></div>`;
    document.getElementById('playerDrawWrap').innerHTML = `
      <div class="sh"><div class="st" style="font-size:18px">2026 DRAW &mdash; ROUND BY ROUND</div><div class="ss">OPPONENT, SCORE, PRICE &amp; BREAKEVEN</div></div>
      <table class="draw-tbl"><thead><tr><th>RD</th><th>OPP</th><th>VEN</th><th>PTS</th><th>MIN</th><th>PRICE</th><th>BE</th><th>PPM</th></tr></thead>
      <tbody>${p.draw.map(d=>{
        if(d.vs==='BYE') return `<tr class="bye"><td>${d.rd}</td><td colspan="7">BYE</td></tr>`;
        return `<tr><td>${d.rd}</td><td>${chipHtml(d.vs)}</td><td>${d.ven}</td><td>${d.pts}</td><td>${d.min}</td><td>$${(d.price/1000).toFixed(1)}k</td><td>${d.be}</td><td>${d.ppm}</td></tr>`;
      }).join('')}</tbody></table>`;
    const note = document.getElementById('playerNote');
    note.style.display='block'; note.textContent = p.note || '';
  } else if(sosHit){
    // SOS-only profile (real data, no price/BE)
    const teamOverall = findTeamOverall(sosHit.team);
    document.getElementById('playerMeta').innerHTML = `${pillHtml(sosHit.team)}<span>${POS_LABELS[sosHit.pos]}</span>`;
    document.getElementById('playerStats').innerHTML = `
      <div class="stat-box"><div class="stat-val">#${sosHit.rank}</div><div class="stat-lbl">PLAYER SOS RANK</div></div>
      <div class="stat-box"><div class="stat-val">${teamOverall ? '#'+teamOverall.rank : '\u2013'}</div><div class="stat-lbl">TEAM SOS RANK</div></div>
      <div class="stat-box"><div class="stat-val">${sosHit.avg.toFixed(1)}</div><div class="stat-lbl">SEASON AVG</div></div>
      <div class="stat-box"><div class="stat-val">${sosHit.opp.toFixed(1)}</div><div class="stat-lbl">AVG OPP CONCEDED</div></div>
      <div class="stat-box"><div class="stat-val">${sosHit.sos}</div><div class="stat-lbl">SOS RATING</div></div>`;
    const sosTeamDraw = findTeamDraw(state.winKey, sosHit.team);
    state.concedePeriod = 'seasonAvg';
    state.drawCtx = sosTeamDraw ? { team: sosHit.team, draw: sosTeamDraw, roundNums: windowRounds(state.winKey), bucket: sosHit.bucket } : null;
    renderPlayerDrawSection();
    const note = document.getElementById('playerNote');
    note.style.display='block';
    note.textContent = '3RD/5RD rolling averages, minutes and PPM require live SuperCoach round-by-round data, which isn\u2019t available yet \u2014 showing season SOS data only.';
  } else if(manual){
    // Manually-tracked profile (injured / outside main roster) — no live SOS position data
    const teamOverall = findTeamOverall(manual.team);
    document.getElementById('playerMeta').innerHTML = `${pillHtml(manual.team)}<span>${manual.pos}</span>`;
    document.getElementById('playerStats').innerHTML = `
      <div class="stat-box"><div class="stat-val">${teamOverall ? '#'+teamOverall.rank : '\u2013'}</div><div class="stat-lbl">TEAM SOS RANK</div></div>
      <div class="stat-box"><div class="stat-val">${manual.avg}</div><div class="stat-lbl">AVG PTS</div></div>
      <div class="stat-box"><div class="stat-val">${manual.mins}</div><div class="stat-lbl">MINS</div></div>
      <div class="stat-box"><div class="stat-val">${manual.r35}</div><div class="stat-lbl">3/5RD</div></div>
      <div class="stat-box"><div class="stat-val">${manual.ppm}</div><div class="stat-lbl">PPM</div></div>`;
    const manualTeamDraw = findTeamDraw(state.winKey, manual.team);
    // No live SOS bucket for manual/off-roster players, so the draw renders without
    // positional concede badges (drawGridHtml/concedeLegendHtml both no-op without a bucket).
    state.concedePeriod = 'seasonAvg';
    state.drawCtx = manualTeamDraw ? { team: manual.team, draw: manualTeamDraw, roundNums: windowRounds(state.winKey), bucket: null } : null;
    renderPlayerDrawSection();
    const note = document.getElementById('playerNote');
    note.style.display='block';
    note.textContent = `${manual.injury} \u2014 currently outside the main roster, so no live position-table SOS data. Stats above are manually tracked from SuperCoach.`;
  } else {
    document.getElementById('playerMeta').innerHTML = `<span>No data loaded</span>`;
    document.getElementById('playerStats').innerHTML = `<div class="empty-state" style="grid-column:1/-1">No SOS or SC data found for ${name} in this window.</div>`;
    state.drawCtx = null;
    document.getElementById('playerDrawWrap').innerHTML = '';
    document.getElementById('playerNote').style.display='none';
  }
  showView('player');
}

renderLanding();
</script>
</body>
</html>
"""

final = HTML.replace("__PAYLOAD__", PAYLOAD)
final = final.replace("__RUBHUB_LOGO__", RUBHUB_LOGO_B64)
final = final.replace("__THERUB_LOGO__", THERUB_LOGO_B64)
final = final.replace("__NATTY_AVATAR__", NATTY_AVATAR_B64)
final = final.replace("__WUKA_AVATAR__", WUKA_AVATAR_B64)
with open('/mnt/user-data/outputs/DraftFinals.html','w', encoding='utf-8') as f:
    f.write(final)
print("Written", len(final), "chars")
