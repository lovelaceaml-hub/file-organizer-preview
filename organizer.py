"""Show how files in one chosen folder could be grouped by type."""

import argparse
import json
from pathlib import Path

GROUPS = {
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".md": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".webp": "Images",
    ".zip": "Archives",
    ".gz": "Archives",
    ".7z": "Archives",
    ".mp4": "Media",
    ".mp3": "Media",
    ".wav": "Media",
}


def plan(folder: Path) -> list[dict[str, str]]:
    if folder.is_symlink() or not folder.is_dir():
        raise ValueError("Select an existing directory")
    proposed = []
    for entry in sorted(folder.iterdir(), key=lambda item: (item.name.casefold(), item.name)):
        if entry.name.startswith(".") or entry.is_symlink() or not entry.is_file():
            continue
        group = GROUPS.get(entry.suffix.lower())
        if group is None:
            continue
        destination_folder = folder / group
        if destination_folder.is_symlink() or (destination_folder.exists() and not destination_folder.is_dir()):
            continue
        destination = destination_folder / entry.name
        if destination.exists() or destination.is_symlink():
            continue
        proposed.append({"source": entry.name, "destination": f"{group}/{entry.name}"})
    return proposed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Only this directory is scanned")
    args = parser.parse_args()
    try:
        print(json.dumps(plan(args.folder), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
