import pytest
from health_assessment import health_status, calculate_health_score, display_summary

def test_health_score():
    assert calculate_health_score([100, 200]) == 150
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
        "Age: 20\n"
        "Average Health Score: 155.00\n"
        "Health Status: Critical Condition"
    )

    result = display_summary("Kavya", "101", "20", 155.00, "Critical Condition")
    assert result == expected_output
