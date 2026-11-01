# Deployment - Student Records Manager

## Environments
| Environment | Where | Purpose |
|-------------|-------|---------|
| Development | Laptop, DEBUG on | Writing code |
| CI | GitHub Actions | Runs checks and 9 tests on every push |
| Staging | Laptop with production settings (DEBUG off) | Final testing before release |
| Production | PythonAnywhere, main branch | Live site |

## Preparation
- requirements.txt lists all dependencies
- SECRET_KEY, DEBUG, ALLOWED_HOSTS and email backend come from environment variables
- Secure cookies are switched on in production (DJANGO_SECURE=True)
- python manage.py check --deploy: no errors in production settings; two warnings remain (HSTS and SSL redirect)
  and are handled by the host's Force HTTPS option

## Staging results
| Check | Result |
|-------|--------|
| python manage.py test (9 tests) | Pass |
| List page loads | Pass |
| Add page loads | Pass |
| Delete page loads | Pass |
| Wrong URL gives plain 404 | Pass |
| GitHub Actions CI #1 | Pass |

## Rollback plan
1. Read the Error log to find the cause.
2. On GitHub open the merged pull request and click Revert, then merge the new pull request.
3. On PythonAnywhere run: cd student-records-django, then git pull, then click Reload on the Web tab.

## Known issues
- mail.E001 error appeared with production settings because of the development email backend. Fixed by reading the backend from an environment variable.
- The free PythonAnywhere account must be extended each month.