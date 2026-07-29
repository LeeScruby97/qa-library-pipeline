"""Tests for data ingestion functions."""

import json
from pathlib import Path

import pytest
import pandas as pd
from data_processing.ingestion import (
    load_csv,
    load_json,
    load_excel
)


def test_load_csv_success():
    """Test loading real CSV file."""
    df = load_csv('data/circulation_data.csv')

    assert len(df) > 0
    assert 'transaction_id' in df.columns


def test_load_csv_file_not_found():
    """Test error handling when file doesn't exist."""
    with pytest.raises(FileNotFoundError):
        load_csv('data/nonexistent.csv')


def test_load_json_success():
    """Test loading real JSON file."""
    df = load_json('data/events_data.json')

    assert len(df) > 0
    assert isinstance(df, pd.DataFrame)


def test_load_csv_empty_file(tmp_path):
    """Test that an empty CSV raises an error."""
    empty = tmp_path / "empty.csv"
    empty.write_text("")

    with pytest.raises(pd.errors.EmptyDataError):
        load_csv(str(empty))


def test_load_json_file_not_found():
    """Test error handling when JSON file doesn't exist."""
    with pytest.raises(FileNotFoundError):
        load_json('data/nonexistent.json')


def test_load_json_invalid(tmp_path):
    """Test that invalid JSON raises an error."""
    bad = tmp_path / "bad.json"
    bad.write_text("not valid json {{{")

    with pytest.raises(json.JSONDecodeError):
        load_json(str(bad))


def test_load_csv_error_loading(monkeypatch, tmp_path):
    """Test generic CSV loading error handling."""

    csv_file = tmp_path / "test.csv"
    csv_file.write_text("id,name\n1,Alice")

    def mock_read_csv(*args, **kwargs):
        raise RuntimeError("Unexpected error")

    monkeypatch.setattr(pd, "read_csv", mock_read_csv)

    with pytest.raises(RuntimeError):
        load_csv(str(csv_file))


def test_load_json_error_loading(monkeypatch, tmp_path):
    """Test generic JSON loading error handling."""

    json_file = tmp_path / "test.json"
    json_file.write_text('{"id": 1}')

    def mock_json_load(*args, **kwargs):
        raise RuntimeError("Unexpected error")

    monkeypatch.setattr(json, "load", mock_json_load)

    with pytest.raises(RuntimeError):
        load_json(str(json_file))


def test_load_excel_file_not_found():
    """Test Excel file not found handling."""
    with pytest.raises(FileNotFoundError):
        load_excel('data/nonexistent.xlsx')


def test_load_excel_error_loading(monkeypatch, tmp_path):
    """Test generic Excel loading error handling."""

    excel_file = tmp_path / "test.xlsx"
    excel_file.write_text("dummy")

    def mock_read_excel(*args, **kwargs):
        raise RuntimeError("Unexpected error")

    monkeypatch.setattr(pd, "read_excel", mock_read_excel)

    with pytest.raises(RuntimeError):
        load_excel(str(excel_file))