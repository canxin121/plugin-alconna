from pathlib import Path
from typing import Literal

from tarina import lang

lang.load(Path(__file__).parent / "i18n")
ALCONNA_RESULT: Literal["_alc_result"] = "_alc_result"
ALCONNA_EXEC_RESULT: Literal["_alc_exec_result"] = "_alc_exec_result"
ALCONNA_ARG_KEY: Literal["_alc_arg_{key}"] = "_alc_arg_{key}"
SEGMATCH_RESULT: Literal["_segmatch_result"] = "_segmatch_result"
SEGMATCH_MSG: Literal["_segmatch_msg"] = "_segmatch_msg"
