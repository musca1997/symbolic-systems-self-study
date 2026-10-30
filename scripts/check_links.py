#!/usr/bin/env python3
"""Check Markdown links with curl. HTTP reachability is not content verification."""
import concurrent.futures
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
URL = re.compile(r"\]\((https?://[^\s)]+)\)")
LOCAL = re.compile(r"\]\(([^\s)]+)\)")


def check(url):
    try:
        p = subprocess.run(
            ["curl", "-L", "-s", "-o", "/dev/null", "--max-time", "18",
             "--connect-timeout", "7", "-w", "%{http_code}", url],
            capture_output=True, text=True, timeout=22,
        )
        code = p.stdout.strip()
        status = "OK" if p.returncode == 0 and code.startswith("2") else "REVIEW"
        return status, code or "000", url
    except (subprocess.TimeoutExpired, OSError) as exc:
        return "REVIEW", type(exc).__name__, url


def main():
    urls = set()
    missing = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text()
        urls.update(URL.findall(text))
        for link in LOCAL.findall(text):
            if link.startswith(("http:", "https:", "#", "mailto:")):
                continue
            target = link.split("#", 1)[0]
            if target and not (path.parent / target).exists():
                missing.append((path.relative_to(ROOT), target))
    for path, target in missing:
        print(f"MISSING_LOCAL\t{path}\t{target}")
    if "--local-only" in sys.argv:
        print(f"Local links: {len(missing)} missing")
        return bool(missing)
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        results = sorted(pool.map(check, sorted(urls)))
    for row in results:
        print("\t".join(row))
    review = sum(row[0] != "OK" for row in results)
    print(f"SUMMARY\t{len(results)} URLs\t{review} need review\t{len(missing)} missing local")
    return bool(missing or review)


if __name__ == "__main__":
    sys.exit(main())
