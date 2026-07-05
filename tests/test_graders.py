from env.graders import grade_easy


def test_grade_easy_range():
    context = {
        "expected_keywords": ["refund"],
        "sentiment": "Frustrated"
    }

    score = grade_easy(
        context,
        "Sorry, we will process your refund."
    )

    assert 0 < score < 1