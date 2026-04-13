from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_IMPORT = "from Common.Tags import"


def file_has_required_import(file_path: Path) -> bool:
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return any(line.strip().startswith(REQUIRED_IMPORT) for line in file)
    except (OSError, UnicodeDecodeError):
        return False


def find_missing_imports_in_directory(root_path: Path) -> list[Path]:
    missing_files: list[Path] = []

    for file_path in sorted(root_path.rglob("*")):
        if not file_path.is_file() or file_path.suffix != ".py":
            continue

        if not file_has_required_import(file_path):
            missing_files.append(file_path.absolute())

    return missing_files


def find_missing_imports(paths: list[Path]) -> list[Path]:
    missing_files: list[Path] = []

    for path in sorted(paths):
        resolved_path = path.expanduser().resolve()

        if not resolved_path.exists():
            continue

        if resolved_path.is_dir():
            missing_files.extend(find_missing_imports_in_directory(resolved_path))
            continue

        if resolved_path.is_file() and resolved_path.suffix == ".py":
            if not file_has_required_import(resolved_path):
                missing_files.append(resolved_path)

    return sorted(set(missing_files))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find Python files missing 'from Common.Tags import'."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="One or more files or folders to scan.",
    )
    args = parser.parse_args()

    current_directory = Path.cwd().resolve()
    input_paths = [Path(path) for path in args.paths]
    missing_files = find_missing_imports(input_paths)

    for file_path in missing_files:
        try:
            print(file_path.relative_to(current_directory))
        except ValueError:
            print(file_path)

    if missing_files:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
