# From Dublin to Little Rock

Static site for my Gilman follow-on project: photos, blog posts, and a guide for CS students. Built with Jekyll and hosted on GitHub Pages.

## Publish it

1. Create a new public repo on GitHub. A repo named `GraysonJackson.github.io` gives the URL `https://GraysonJackson.github.io`. Any other name gives `https://GraysonJackson.github.io/repo-name`.
2. Open `_config.yml`. For a project repo, set `baseurl: "/repo-name"`. For the `.github.io` repo, leave it as `""`.
3. Push this folder to the repo's default branch.
4. In the repo, go to Settings, then Pages. Set Source to "Deploy from a branch", pick your branch and `/ (root)`, and save.
5. Wait a minute or two. The URL appears at the top of the Pages settings.

## Add photos

1. Put full-size photos in a folder named `originals` (git-ignored).
2. Run `pip install pillow` once, then `python scripts/prepare_photos.py originals assets/photos`. This resizes them and strips GPS data.
   The script also gives photos web-safe filenames, such as `mg-4122.jpg` for `_MG_4122.JPG`, without leading underscores that Jekyll may skip.
3. Add an entry for each photo in `_data/photos.yml`. Delete the placeholder entries.
4. Set `featured: true` on the one photo for the home page.

## Finish the writing

Use [the writing questionnaire](project-notes/writing-questions.md) to fill in the personal details. Answers can be rough notes in chat or in `project-notes/answers.local.md`, which is ignored by Git. The `project-notes` folder is excluded from the generated site; ordinary files there can still be visible in the GitHub repo.

The photos from `Fall.zip` have been processed. Use [the numbered photo index](project-notes/photo-index.jpg) and [filename list](project-notes/photo-index.md) to identify places and supply caption notes before adding them to the gallery.

## Write a post

1. Finish a draft in `_drafts/`.
2. Move it to `_posts/` and name it `YYYY-MM-DD-short-title.md`.
3. Commit and push. It shows up on the Blog page and the home page.

## Before you share the link

Run `grep -rn "TODO" . --include="*.md" --include="*.html" --include="*.yml"` and fix every hit in published files. Drafts can keep their TODOs until you publish them.

## Preview locally (optional)

```
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.
