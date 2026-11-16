# Publication status & download setup

## Published now

Two public GitHub Releases are live:

| Release | Tag | Public file |
|---|---|---|
| Soundtrack 001 — The Thirteenth Bell | [`soundtrack-001`](https://github.com/Brinkhagen/the-black-grimoire/releases/tag/soundtrack-001) | [MP3](https://github.com/Brinkhagen/the-black-grimoire/releases/download/soundtrack-001/The.Black.Grimoire.The.Thirteenth.Bell.Official.Original.Soundtrack.001.mp3) |
| Free Preview Edition — English | [`preview-en-001`](https://github.com/Brinkhagen/the-black-grimoire/releases/tag/preview-en-001) | [PDF](https://github.com/Brinkhagen/the-black-grimoire/releases/download/preview-en-001/THE.BLACK.GRIMOIRE.A.Dark.Fantasy.5.5e.Sourcebook.pdf) |

**Visitors do not need a GitHub account to download either file.** Both are currently hosted as release assets.

## Activate the illustrated download website

The [website source](index.html) and artwork in [assets](../assets) are committed. To publish the site at the GitHub Pages URL:

1. Open [Settings → Pages](https://github.com/Brinkhagen/the-black-grimoire/settings/pages).
2. Choose **Deploy from a branch**.
3. Set **main** and folder **/docs**, then click **Save**.
4. When GitHub confirms publishing, open [The Black Grimoire download website](https://brinkhagen.github.io/the-black-grimoire/) in a private window.
5. Test both file download buttons and the layout on desktop and mobile.

We cannot confirm Pages is enabled solely from committing HTML files. The two current button URLs point directly to the published assets, so they also work when GitHub API rate limits block live statistics.

## Publish additional PDF previews

- German: tag `preview-de-001` + one PDF asset
- Turkish: tag `preview-tr-001` + one PDF asset

Only publish these after the actual translated **PDF documents** are completed and checked. The artwork/banner images are not substitutes for PDF content. After publication, the website automatically enables the appropriate language card if it finds one matching PDF asset.

## Download analytics

- Use [GitHub's public Releases API](https://api.github.com/repos/Brinkhagen/the-black-grimoire/releases).
- Or run `python scripts/download_stats.py` after cloning the repo.
- Export with `python scripts/download_stats.py --csv > downloads.csv`.

Download counts measure **events, not unique visitors or backers**. The website does not track visitor numbers by itself.

## AI and publication

The soundtrack was produced with assistance from Suno. Public/promotional rights depend on the applicable terms and the subscription held **at the time of generation**. Confirm those before promoting or distributing the recording commercially.
