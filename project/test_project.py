import pytest
import json
from unittest.mock import mock_open, patch
from project import add_task, list_tasks, mark_as_completed, remove_task


@pytest.fixture
def mock_file():
    return json.dumps([])


def test_add_task(mock_file):
    with patch("builtins.open", mock_open(read_data=mock_file)) as mocked_file:
        with patch("os.path.exists", return_value=True):
            add_task("Buy milk")
            mocked_file.assert_called_with("tasks.json", "w", encoding="utf-8")


def test_list_tasks_empty(mock_file, capsys):
    with patch("builtins.open", mock_open(read_data=mock_file)):
        with patch("os.path.exists", return_value=True):
            list_tasks()
    captured = capsys.readouterr()
    assert "No tasks available. Add one!" in captured.out



def test_mark_as_completed():
    data = json.dumps([{"task": "Study English", "status": "pending"}])
    with patch("builtins.open", mock_open(read_data=data)) as mocked_file:
        with patch("os.path.exists", return_value=True):
            mark_as_completed("Study English")
            mocked_file.assert_called_with("tasks.json", "w", encoding="utf-8")


def test_remove_task():
    data = json.dumps([{"task": "Make dinner", "status": "pending"}])
    with patch("builtins.open", mock_open(read_data=data)) as mocked_file:
        with patch("os.path.exists", return_value=True):
            remove_task("Make dinner")
            mocked_file.assert_called_with("tasks.json", "w", encoding="utf-8")