from health_assessment import health_status

def test_health_status():
    assert health_status(95) == "Excellent Health"
    assert health_status(85) == "Good Health"
    assert health_status(70) == "Moderate Health"
    assert health_status(60) == "Fair Health"
    assert health_status(45) == "Poor Health"
    assert health_status(30) == "Critical Condition"


def test_display_summary():
    expected_output = (
        "\n--- Patient Health Report ---\n"
        "Name: Kavya\n"
        "Patient ID: 101\n"
        "Age: 25\n"
        "Average Health Score:155\n"
        "Health Status: Critical Condition"
    )

    result = health_status(
        "Kavya",
        "101",
        "20",
        155.00,
        "Critical Condition"
    )

    assert result == expected_output
