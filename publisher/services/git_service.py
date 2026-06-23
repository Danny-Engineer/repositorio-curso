from config.settings import ROOT
from utils.helpers import run_command

def git_status() -> str:
    return run_command("git status", ROOT)

def git_log() -> str:
    return run_command("git log --oneline -10", ROOT)

def git_pull() -> str:
    return run_command("git pull", ROOT)

def git_push(message: str = "Actualización desde Publisher") -> str:
    return run_command(f'git add . && git commit -m "{message}" && git push', ROOT)
