from config.settings import ROOT
from utils.helpers import run_command

def build_site() -> str:
    return run_command("mkdocs build", ROOT)

def serve_command() -> str:
    return "mkdocs serve"
