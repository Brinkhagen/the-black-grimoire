# Publish your free downloads — two remaining steps

The README, landing page, license notes and release draft have been created. **The soundtrack MP3 is not yet published as a GitHub Release asset.**

## 1. Publish the soundtrack

1. Go to [GitHub → New release](https://github.com/Brinkhagen/the-black-grimoire/releases/new).
2. Create tag `soundtrack-001` from the `main` branch.
3. Title: `The Black Grimoire — The Thirteenth Bell (Official Soundtrack 001)`.
4. Paste the prepared public release description from [RELEASE_NOTES.md](RELEASE_NOTES.md).
5. Drag in your MP3 as an attachment with the **exact** name:
   `The_Black_Grimoire_OST_001_The_Thirteenth_Bell.mp3`
6. Publish release.
7. Test the link in an incognito/private browser window.

**Important:** Check that the Suno subscription at the **time of generation** allows the planned public promotional distribution. Do not publish if rights are still uncertain.

## 2. Enable the customer-friendly GitHub Pages download hub

1. Open [Settings → Pages](https://github.com/Brinkhagen/the-black-grimoire/settings/pages).
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Choose branch **main** and folder **/docs**, then click **Save**.
4. Once GitHub reports successful publication, the page should be at:
   `https://brinkhagen.github.io/the-black-grimoire/`

The landing page automatically queries public GitHub Releases and, when the expected filename appears, shows a **Download MP3** button and the download event count. The three PDF buttons behave the same way once the actual preview PDFs have been published.

**Do not put the MP3 in the Git source tree.** Use Release assets to keep the repository clean and preserve download statistics.

## Tracking

- Per-file download events appear on the download page after release publication.
- To inspect all counts locally: `python scripts/download_stats.py`
- To export a spreadsheet-ready count: `python scripts/download_stats.py --csv > counts.csv`

GitHub counts downloads; these are not necessarily unique people. The Pages landing page does not automatically count page visits or collect email addresses.
