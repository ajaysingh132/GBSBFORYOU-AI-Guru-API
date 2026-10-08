from typing import Literal

from pydantic import BaseModel, Field


Provider = Literal[
    "openai",
    "gemini",
    "huggingface",
    "floot",
]


GuruMode = Literal[
    "teach",
    "diagnose",
    "assess",
    "remediate",
    "mastery",
]


class GuruRequest(BaseModel):
    question: str = Field(
        min_length=1,
        max_length=12000,
    )

    student_answer: str | None = Field(
        default=None,
        max_length=12000,
    )

    class_level: str = "XII"

    subject_code: str = "083"

    session: str = "2026-27"

    provider: Provider = "openai"


class GuruDecision(BaseModel):
    concept: str

    class_level: str

    subject_code: str

    session: str

    mode: GuruMode

    prerequisite_needed: bool

    teaching_plan: list[str]

    assessment_action: str

    mastery_status: str

    next_action: str


class GuruResponse(BaseModel):
    api_version: str = "v1"

    provider: Provider

    guru_decision: GuruDecision
