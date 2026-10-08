# From Dublin to Little Rock

My Gilman follow-on service project, built with Jekyll and hosted on GitHub Pages. It includes four first-person posts about my internship and life in Dublin, a study-abroad guide for CS students, and 25 photos with captions.

Visit [the site](https://graysonjackson.github.io/gilman-project/).

## Content

- `_posts/`: published articles, named `YYYY-MM-DD-short-title.md`.
- `_data/photos.yml`: gallery order, locations, captions, and alt text.
- `assets/photos/`: resized photos used by the site.
- `guide.md` and `about.md`: the CS guide and background page.
- `_layouts/`, `_includes/`, and `assets/css/`: page structure and styling.

## Update the site

Edit the content, commit, and push to `main`. GitHub Pages builds automatically. Check the latest [Pages build and deployment](https://github.com/GraysonJackson/gilman-project/actions) and the live site after publishing.

The project path is configured as `baseurl: "/gilman-project"`. Use Jekyll's `relative_url` filter for local links and images so they work under that path.

## Prepare photos

Put source photos in `originals/`, then run:

```powershell
python -m pip install pillow
python scripts/prepare_photos.py originals assets/photos
```

The script limits the longest side to 1600 pixels, removes EXIF/GPS metadata, and creates web-safe JPEG filenames. Add each photo to `_data/photos.yml`. Set `featured: true` on one homepage image and `preview: true` on three images for the homepage strip.

Original photos and `.local/` notes are ignored by Git and excluded from the generated site.

## Preview locally

With Ruby and Bundler installed:

```text
bundle install
bundle exec jekyll serve
```

Then open [the local preview](http://localhost:4000/gilman-project/).
