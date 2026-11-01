# Testing - Student Records Manager

## How to run
python manage.py test

## Test types
- Unit tests: Student model
- Integration tests: list, add, edit and delete pages
- Edge cases: empty list, wrong URL (404)

## Test cases
| ID | Test | Expected | Result |
|----|------|----------|--------|
| 1 | test_create_student | Student saved, count is 1 | Pass |
| 2 | test_student_name_saved | Name stored correctly | Pass |
| 3 | test_list_page_loads | HTTP 200 | Pass |
| 4 | test_list_shows_student | Student name on page | Pass |
| 5 | test_empty_list_message | "No students yet." shown | Pass |
| 6 | test_add_page_loads | HTTP 200 | Pass |
| 7 | test_edit_page_loads | HTTP 200 | Pass |
| 8 | test_delete_removes_student | Count becomes 0 | Pass |
| 9 | test_wrong_url_gives_404 | HTTP 404 | Pass |

## Results
Ran 9 tests, all passed (OK).

## Known issues
None found so far.