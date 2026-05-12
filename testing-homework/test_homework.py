from Python_tools_2026 import homework
import pytest
import os
import json

def test_indices_out_of_range():
    with pytest.raises(IndexError):
        homework.take_from_list([1, 2, 4], 10)

def test_negative_indices():
    with pytest.raises(IndexError):
        homework.take_from_list([1, 2, 4], -1)

def test_empty_list():
    with pytest.raises(IndexError):
        homework.take_from_list([], 0)

def test_string_input_in_indices():
    with pytest.raises(ValueError):
        homework.take_from_list([1, 2, 3], "auto")

def test_float_input():
    with pytest.raises(ValueError):
        homework.take_from_list([1, 2, 3], [3.14, 7])

def test_take_from_list_single_index():
    assert homework.take_from_list(["x", "y", "z"], 2) == ["z"]

def test_take_from_list_list_of_indices():
    assert homework.take_from_list(["x", "y", "z"], [1, 2]) == ["y", "z"]

def fake_take_from_list(list, indices): # Fake function to avoid massive calculations
    return [1, 2, 3]

def test_calculate_input_no_json(tmpdir):
    input_file = tmpdir/"input.json"
    output_file = tmpdir/"output.json"
    input_file.write_text("IT_IS_A_STRING_NO_JSON", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        homework.calculate(input_file, output_file)

def test_calculate_function_mocked_results(tmpdir, monkeypatch):
    input_file = tmpdir/"input.json"
    output_file = tmpdir/"output.json"
    test_data = {
        "list": [1, 2, 3, 4, 5, 6, 7],
        "indices": [0, 2, 4]
    }
    input_file.write_text(json.dumps(test_data), encoding="utf-8")
    monkeypatch.setattr(homework, "take_from_list", fake_take_from_list)
    homework.calculate(str(input_file), str(output_file))

    with open(output_file) as f:
        result = json.load(f)
    assert result == [1, 2, 3]

def test_calculate_function_actual_results():
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, "input.json")
    output_file = os.path.join(current_dir, "testing-homework/output.json")

    homework.calculate(input_file, output_file)

    with open(output_file) as f:
        result = json.load(f)
    assert result == [81, 62, 78, 67, 89, 33, 106, 126, 112, 20, 56, 128, 106, 3, 107]
