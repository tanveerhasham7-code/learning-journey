"""Create a SHA-256 manifest for files in a chosen lab folder."""
import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", help="Dedicated lab folder to hash")
    parser.add_argument("--output", default="integrity-manifest.json")
    args = parser.parse_args()
    root = Path(args.folder).resolve()
    output = Path(args.output).resolve()
    if not root.is_dir():
        parser.error("folder must be an existing directory")
    if output == root or root in output.parents:
        parser.error("output must be outside the scanned folder")
    records = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            records.append({
                "relative_path": str(path.relative_to(root)),
                "sha256": sha256_file(path),
                "size_bytes": path.stat().st_size,
            })
    manifest = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "algorithm": "SHA-256",
        "root_folder_name": root.name,
        "files": records,
        "note": "Hashes support integrity comparison; they do not prove safety or origin."
    }
    output.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Hashed {len(records)} file(s). Manifest: {output}")


if __name__ == "__main__":
    main()
