# Simple Journal App

A beginner-friendly Python project for writing and storing journal entries in a JSON file.  
Each entry includes an ID, date, title, message, and timestamp.

## Features
- Add journal entries with title, message, and time
- Stores data in a JSON file (organized by year)
- Automatically creates a new file if it doesn’t exist
- Beginner-friendly and easy to extend

## Example

**Run:**
```bash
python main.py
```

**Input:**
```
Entry Title: My First Note
Entry Message: Today I started learning Python!
```

**Output in JSON file (e.g., 2025.json):**
```json
{
  "2025": [
    {
      "id": 1,
      "date": "09-14",
      "title": "My First Note",
      "message": "Today I started learning Python!",
      "time": "13:25"
    }
  ]
}
```

## Notes
- This is a practice project to learn Python basics (modules, file handling, JSON).
- Still under development — `rm_entry` and `display_entry` are not yet implemented.
- Very minimal, meant for beginners.

## Todo
- [ ] Add function to remove entries  
- [ ] Add function to display all entries  
- [ ] Improve user interface  
