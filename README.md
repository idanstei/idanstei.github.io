# Final CV patch

Replace these repository files:

- `assets/json/resume.json`
- `_includes/cv/render.liquid`
- `_includes/cv/education.liquid`
- `_includes/cv/publications.liquid`

Why this patch:
- the uploaded `resume.json` already contains the corrected education wording,
  the 2026-led publication set, and the cleaned early-career titles;
- the previous renderer passed Education and Publications through
  `al_cv_sort_by_date`, which can mishandle year-only dates;
- the new renderer preserves the JSON order for those sections;
- the Publications renderer defensively suppresses any legacy
  `Full List on Google Scholar` pseudo-entry so the Scholar block appears once.

After replacing the files:

```bash
bundle exec jekyll build
bundle exec al-folio upgrade overrides audit
bundle exec al-folio upgrade overrides accept --all
git add .
git commit -m "Finalize CV education and publications rendering"
git push
```
