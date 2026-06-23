from pathlib import Path
import subprocess
import re
import unicodedata

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def count_files(folder: Path, pattern: str) -> int:
    return len(list(folder.rglob(pattern))) if folder.exists() else 0

def run_command(command: str, cwd: Path) -> str:
    try:
        result = subprocess.run(
            command,
            cwd=str(cwd),
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
        return result.stdout.strip() or result.stderr.strip() or "Comando ejecutado sin salida."
    except Exception as exc:
        return f"Error ejecutando comando: {exc}"
