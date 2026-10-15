#!/usr/bin/env python3
"""Comprueba en un repositorio aislado el rango usado por el workflow."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="hosteleria-workflow-diff-") as tmp:
        repo = Path(tmp) / "repo"
        repo.mkdir()
        git(repo, "init", "--quiet")
        git(repo, "config", "user.name", "Documentation Test")
        git(repo, "config", "user.email", "documentation-test@example.invalid")

        sample = repo / "sample.md"
        sample.write_text("# Base\n", encoding="utf-8")
        git(repo, "add", "sample.md")
        git(repo, "commit", "--quiet", "-m", "base")
        base = git(repo, "rev-parse", "HEAD").stdout.strip()

        sample.write_text("# Base\n\nLínea con espacio final. \n", encoding="utf-8")
        git(repo, "add", "sample.md")
        git(repo, "commit", "--quiet", "-m", "whitespace defect")
        defective = git(repo, "rev-parse", "HEAD").stdout.strip()
        rejected = git(repo, "diff", "--check", f"{base}..{defective}", check=False)
        assert rejected.returncode != 0
        assert "trailing whitespace" in rejected.stdout

        sample.write_text("# Base\n\nLínea corregida.\n", encoding="utf-8")
        git(repo, "add", "sample.md")
        git(repo, "commit", "--quiet", "-m", "whitespace corrected")
        corrected = git(repo, "rev-parse", "HEAD").stdout.strip()
        accepted = git(repo, "diff", "--check", f"{base}..{corrected}", check=False)
        assert accepted.returncode == 0, accepted.stdout

    print("WORKFLOW DIFF SELF-TEST: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
