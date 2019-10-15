from app.parsers.heresy import heresy
from app.parsers.killteam import killteam

KILLTEAM_ID: str = "a467-5f42-d24c-6e5b"

HORUS_HERESY_ID: str = "ca571888-56a9-c58e-ddaf-54f4713538bc"

SUPPORTED_PARSERS = {KILLTEAM_ID: killteam, HORUS_HERESY_ID: heresy}
TEMPLATES = {KILLTEAM_ID: "killteam.html", HORUS_HERESY_ID: "sandbox.html"}

WARHAMMER_40K_ID: str = ""
WARHAMMER_40K_NAME: str = ""

AGE_OF_SIGMAR_ID: str = ""
AGE_OF_SIGMAR_NAME: str = ""

BATTLESCRIBE_VERSION = "2.02"
