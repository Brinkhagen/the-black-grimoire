#!/usr/bin/env python3
"""Display public GitHub Release asset download counts for The Black Grimoire.

Requires Python 3 only. Run:
    python scripts/download_stats.py
    python scripts/download_stats.py --csv

GitHub records download events, NOT unique visitors or completed plays.
"""
import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API = "https://api.github.com/repos/Brinkhagen/the-black-grimoire/releases?per_page=100"

def load_releases():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "The-Black-Grimoire-Download-Stats",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    with urlopen(Request(API, headers=headers), timeout=20) as response:
        return json.load(response)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", action="store_true", help="Print CSV for spreadsheets")
    args = parser.parse_args()
    try:
        releases = load_releases()
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        print("Could not read GitHub releases: " + str(exc), file=sys.stderr)
        return 1
    rows = []
    for release in releases:
        if release.get("draft") or release.get("prerelease"):
            continue
        for asset in release.get("assets", []):
            if asset.get("state") != "uploaded":
                continue
            rows.append((
                release.get("tag_name", ""),
                asset.get("name", ""),
                int(asset.get("download_count", 0)),
                asset.get("browser_download_url", "")
            ))
    if args.csv:
        writer = csv.writer(sys.stdout)
        writer.writerow(["release", "filename", "downloads", "url"])
        writer.writerows(rows)
    else:
        print("The Black Grimoire — Release downloads")
        print("Checked (UTC):", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"))
        print()
        if not rows:
            print("No published release assets found yet.")
        else:
            for tag, filename, downloads, url in rows:
                print(f"{downloads:>7}  {filename}   [{tag}]")
            print("-" * 50)
            print(f"{sum(row[2] for row in rows):>7}  TOTAL download events")
        print()
        print("Counts are download events, not unique people or Kickstarter backers.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
