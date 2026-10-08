# From Dublin to Little Rock

Static site for my Gilman follow-on project: photos, blog posts, and a guide for CS students. Built with Jekyll and hosted on GitHub Pages.

## Publish it

This repo is `GraysonJackson/gilman-project`, with `baseurl: "/gilman-project"`. GitHub Pages is already configured to build from `main`.

1. Commit and push the finished files to `main`.
2. Check the latest **pages build and deployment** run in [GitHub Actions](https://github.com/GraysonJackson/gilman-project/actions).
3. After the deployment succeeds, open [the site](https://graysonjackson.github.io/gilman-project/). Check the home page, all four posts, guide, About page, and gallery before sharing it.

The four completed posts have been moved into `_posts/` with October 8, 2026 publication dates. New work can start in `_drafts/` until it is ready.

## Add photos

1. Put full-size photos in a folder named `originals` (git-ignored).
2. Run `pip install pillow` once, then `python scripts/prepare_photos.py originals assets/photos`. This resizes them and strips GPS data.
   The script also gives photos web-safe filenames, such as `mg-4122.jpg` for `_MG_4122.JPG`, without leading underscores that Jekyll may skip.
3. Add an entry for each photo in `_data/photos.yml`. Delete the placeholder entries.
4. Set `featured: true` on the one photo for the home page.

## Finish the writing

Use [the writing questionnaire](project-notes/writing-questions.md) to fill in the personal details. Answers can be rough notes in chat or in `project-notes/answers.local.md`, which is ignored by Git. The `project-notes` folder is excluded from the generated site; ordinary files there can still be visible in the GitHub repo.

The photos from `Fall.zip` have been processed, and all 25 gallery entries have locations, captions, and alt text. The [numbered photo index](project-notes/photo-index.jpg) and [filename list](project-notes/photo-index.md) remain available for reference.

## Write a post

1. Finish a draft in `_drafts/`.
2. Move it to `_posts/` and name it `YYYY-MM-DD-short-title.md`.
3. Commit and push. It shows up on the Blog page and the home page.

## Before you share the link

Run this from PowerShell and fix any unfinished content in the results:

```powershell
rg -n 'TODO|placeholder' _posts _data _includes _layouts assets/css about.md guide.md index.html gallery.html blog.html
```

Drafts can keep their TODOs until they are ready. Private local notes and original photos are ignored by Git and excluded from the generated site.

## Share the finished project

Draft club messages are in `project-notes/club-sharing.local.md`, and the activity record is `project-notes/outreach-log.local.md`. These files are ignored by Git. Share the site after checking the deployment, then record actual sharing dates and responses for the report.

The physical photo display has been removed from the plan. The replacement is the online gallery and photo essay. A Gilman proposal-revision request is drafted in `project-notes/project-revision-request.local.md`; it has not been sent.

## Preview locally (optional)

```
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.
