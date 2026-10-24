# Tech Brand Website Skill

**English** · [简体中文](README.zh-CN.md)

A reusable Codex skill for creating cinematic technology brand websites as a complete, responsive `index.html` using Tailwind CSS v3, vanilla JavaScript, and optional Anime.js.

The visual direction combines generous whitespace, modular Bento layouts, dark technical sections, and cinematic scroll storytelling. References to Apple, Google, Microsoft, and 影视飓风 (MediaStorm) describe design influences only. This project is independent and does not claim affiliation, endorsement, or an Awwwards award.

## What you get

- A ready-to-install skill manifest with detailed design and implementation guidance.
- A six-part page structure: navigation, Hero, Bento features, alternating narrative sections, technical metrics, and footer.
- Theme tokens, automatic light/dark mode, responsive layouts, keyboard access, reduced-motion behavior, and practical fallback requirements.
- Animation guidance for reveal sequences, pointer highlights, subtle tilt, particles, counters, and progress indicators.
- Bilingual documentation, copyable prompts, a publishing checklist, and a dependency-free package validation script.

This repository contains instructions for an AI coding agent. It is not an npm library, an animation engine, a finished website, or a guarantee that generated code will pass every accessibility or performance audit. No demo website or screenshots are included in this release.

## Quick start

Download or clone this repository, then install **only** `skills/tech-brand-website/` into the skills directory recognized by your Codex installation. Keep `SKILL.md` inside that folder. Do not copy the entire repository as the skill.

The following examples use the `$CODEX_HOME/skills` convention supported by the skill installer in the environment where this package was prepared, falling back to `~/.codex/skills`. Other Codex distributions may use different discovery paths; consult your client's documentation. [Official skill authoring documentation](https://learn.chatgpt.com/docs/build-skills).

### Windows PowerShell

Run from the downloaded repository root:

```powershell
$skillBase = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex/skills' }
$skillTarget = Join-Path $skillBase 'tech-brand-website'
if (Test-Path -LiteralPath $skillTarget) { throw 'Skill already exists. Back it up before updating.' }
New-Item -ItemType Directory -Path $skillBase -Force | Out-Null
Copy-Item -LiteralPath './skills/tech-brand-website' -Destination $skillTarget -Recurse
```

### macOS / Linux

Run from the downloaded repository root:

```bash
skill_base="${CODEX_HOME:-$HOME/.codex}/skills"
skill_target="$skill_base/tech-brand-website"
if [ -e "$skill_target" ]; then
  echo 'Skill already exists. Back it up before updating.' >&2
else
  mkdir -p "$skill_base" && cp -R ./skills/tech-brand-website "$skill_target"
fi
```

### Install from GitHub with the skill installer

After publishing your repository, ask Codex:

```text
Use $skill-installer to install skills/tech-brand-website from
https://github.com/YOUR_USERNAME/YOUR_REPOSITORY
```

Replace both uppercase placeholders with your actual GitHub owner and repository name. This method requires an available skill-installer and network access. This package has no published remote URL yet.

Start a new turn after installation. If discovery has not refreshed, open a new chat or reload your client. Invoke the skill:

```text
Use $tech-brand-website to create a website for “Orbit Labs”, an edge AI
hardware brand. Write the page in English. Target product teams and developers.
Use a dark cinematic Hero and bright Bento feature sections.
Primary CTA: jump to #technology. Secondary CTA: jump to #contact.
Use clearly labeled sample metrics, no external video, and vanilla JavaScript.
Save the complete runnable page as index.html.
```

The skill's default website copy is Chinese; specify English or another language in your request when needed. The canonical skill instructions are written in Chinese, while the English documentation explains the same capability and defaults.

## Design and technical contract

| Area | Default behavior |
| --- | --- |
| Layout | 8px spacing rhythm; 12-column desktop Bento with 7:5 and 6:6 combinations |
| Hero | Full viewport, approximately 64px desktop / 48px mobile title, two working CTAs |
| Typography | Inter or system sans-serif, mostly 300–600 weights |
| Color | Neutral base; restrained blue accents; blue/purple/cyan technical lighting |
| Motion | 400–600ms transitions; 24px scroll reveals; 150ms grouped stagger |
| Interaction | Pointer-only tilt and tracking, hover lift, pressed state, optional ripple |
| Responsive | Mobile first; 640px, 768px, and 1024px layout adjustments; 320px overflow check |
| Accessibility | Visible focus, keyboard menu, Escape behavior, text contrast target ≥4.5:1 |
| Reduced motion | Stop decorative motion and reveal final content, counters, and progress immediately |
| Delivery | Semantic HTML, inline CSS/JS, Tailwind v3 CDN, optional single Anime.js dependency |

The skill favors vanilla JS. If Anime.js is used, the agent must verify the selected version's API and loading format. GSAP is not required. CDN resources require an internet connection; a single HTML file is not necessarily an offline file. Tailwind's browser CDN approach is convenient for the requested deliverable; before a production rollout, review the delivery setup, asset licensing, CSP, and performance. A compiled CSS variant can be requested separately.

## Recommended workflow

1. Provide a brand brief, audience, content language, product benefits, assets, and real CTA targets.
2. Ask for a complete `index.html`, then open it in a browser with network access.
3. Review mobile and desktop layouts, light/dark themes, reduced motion, keyboard navigation, resource failures, and console errors.
4. Replace clearly labeled sample content with verified product claims and properly licensed assets.
5. Deploy only when the output is reviewed and the deployment destination is authorized.

Read [bilingual prompt examples](docs/EXAMPLES.md) and the [publishing guide](docs/PUBLISHING.md) for more detail.

## Repository layout

```text
.
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/
│   ├── EXAMPLES.md
│   └── PUBLISHING.md
├── scripts/
│   └── validate.py
└── skills/
    └── tech-brand-website/
        ├── SKILL.md
        └── agents/
            └── openai.yaml
```

## Validate and troubleshoot

Requires Python 3.10+ for the repository validator; installing and reading the skill does not require Python or npm.

```bash
python scripts/validate.py
```

The validator checks packaging structure, frontmatter identity, required documentation, UTF-8 readability, and local Markdown link targets. It does not evaluate generated websites or guarantee agent behavior.

- **Not discovered:** check the actual client skill path, folder nesting, and presence of `SKILL.md`; refresh the client and explicitly use `$tech-brand-website`.
- **Already installed:** back up the existing folder before replacing it. Removing the installed folder uninstalls this skill; generated websites remain separate.
- **Wrong page language:** specify the desired language in the prompt.
- **CDN unavailable:** use available resources or request bundled/compiled assets; do not hide the core content behind initialization.
- **Motion is absent:** check reduced-motion preferences and coarse-pointer/mobile behavior before treating this as a defect.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). Released under the [MIT License](LICENSE). Third-party libraries, fonts, images, and videos retain their own licenses; this repository does not redistribute those assets. Version history is in [CHANGELOG.md](CHANGELOG.md).
