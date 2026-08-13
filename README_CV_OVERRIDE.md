# CV override package for idanstei.com

This package is a site-specific override for the JSONResume CV page.

## Copy these files into the repository

- `_includes/cv/render.liquid`
- `_includes/cv/education.liquid`
- `_includes/cv/publications.liquid`
- `assets/json/resume.json`
- `_pages/cv.md`

The `_includes/cv/*` files intentionally shadow the matching `al_folio_cv` plugin templates.

## What changes

- removes the large Contact Information card
- moves Technical & Leadership Expertise directly below Professional Summary
- uses only `work` for Experience, so volunteer/service entries are not merged into the career timeline
- renders Education with the intended EE/BME wording and clean single-year/range dates
- updates Selected Publications to the 2026-led set and displays actual titles
- keeps the downloadable PDF button

## After copying

Build locally if available, then deploy. After the site builds successfully, run:

```bash
bundle exec al-folio upgrade overrides audit
bundle exec al-folio upgrade overrides accept
```

Review the generated `.al-folio-overrides.yml` and commit it so future plugin updates can flag drift in these shadowed files.

## Scope

This renderer intentionally supports the site's current `cv_format: jsonresume`. If you later switch to RenderCV, remove or adapt `_includes/cv/render.liquid`.
