# QA Automation Portfolio

Hands-on test automation practice using Python, pytest and Playwright.
I'm a QA professional with 7+ years of experience in financial services,
building practical automation skills on top of my manual and
data-validation testing background.

## What's in here

### API tests (`tests/api/`)
API tests for [Restful-Booker](https://restful-booker.herokuapp.com/),
a public practice API for booking management.

- Create a booking and read it back to verify the data
- List bookings and check response status, format and body
- Request an invalid booking ID and check the error handling
- Shared setup using pytest fixtures (`conftest.py`)
- Data-driven tests using `pytest.mark.parametrize`

### UI smoke test
A basic Playwright browser smoke test (`test_smoke.py`).

## Tech stack
Python · pytest · requests · Playwright · Postman · Git

## How to run

```bash
git clone https://github.com/vedaf1/qa-automation-portfolio.git
cd qa-automation-portfolio
python -m venv .venv
.venv\Scripts\activate        # Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
playwright install
pytest tests/api -v
```

## Roadmap
- [x] pytest basics and first API tests
- [ ] Auth token, update and delete endpoints, cleanup fixtures
- [ ] Negative tests and JSON schema validation
- [ ] Playwright UI tests with Page Object Model
- [ ] API + UI combined tests
- [ ] Data reconciliation project (synthetic data)
- [ ] CI with GitHub Actions and test reports

## Notes
All tests run against public practice sites and synthetic data only.
