from .models import GuruRequest, GuruDecision


def build_decision(
    request: GuruRequest,
    mode: str | None = None,
) -> GuruDecision:

    text = request.question.lower()

    if mode is None:
        if request.student_answer:
            mode = "diagnose"

        elif any(
            word in text
            for word in [
                "गलत",
                "confused",
                "confusion",
                "error",
                "mistake",
                "समझ",
            ]
        ):
            mode = "remediate"

        else:
            mode = "teach"

    prerequisite_needed = any(
        word in text
        for word in [
            "python",
            "variable",
            "input",
            "function",
            "loop",
            "sql",
            "network",
        ]
    )

    teaching_plan = [
        "Identify the learner's current concept and prerequisite level.",
        "Use curriculum-approved evidence before generating instruction.",
        "Explain from simple concept to worked example.",
        "Check understanding before independent practice.",
    ]

    assessment_actions = {
        "teach": (
            "Give a short explanation, example, "
            "output prediction, then guided practice."
        ),
        "diagnose": (
            "Compare the student answer with the target concept "
            "and identify the misconception."
        ),
        "assess": (
            "Evaluate the response using concept accuracy, "
            "reasoning and application."
        ),
        "remediate": (
            "Return to the smallest missing prerequisite "
            "and provide targeted practice."
        ),
        "mastery": (
            "Require independent application and verify "
            "repeated correct performance."
        ),
    }

    next_actions = {
        "teach": "Ask one concept-check question.",
        "diagnose": "Teach the missing prerequisite and reassess.",
        "assess": "Record evidence and decide mastery status.",
        "remediate": "Give a simpler example, then recheck.",
        "mastery": "Advance to the next prerequisite-linked concept.",
    }

    return GuruDecision(
        concept=request.question.strip()[:120],
        class_level=request.class_level,
        subject_code=request.subject_code,
        session=request.session,
        mode=mode,
        prerequisite_needed=prerequisite_needed,
        teaching_plan=teaching_plan,
        assessment_action=assessment_actions[mode],
        mastery_status="not_yet_verified",
        next_action=next_actions[mode],
  )
