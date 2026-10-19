# Enterprise UI Automation Framework – Books to Scrape

A UI automation framework built using Python, Playwright, and Pytest to validate website functionality, book navigation, data consistency, hyperlinks, product images, pagination, and login behavior.

## Project Overview

This project automates six functional test scenarios across two public sandbox websites:

- **Books to Scrape:** Homepage validation, random book navigation, book data consistency, broken-link validation, product image validation, and pagination.
- **Quotes to Scrape:** Login functionality and authenticated-state validation through the Logout link.

The framework uses reusable page classes, Pytest fixtures, modular test cases, and automated reporting. It supports local execution, Docker-based execution, and GitHub Actions CI/CD.

### Live Test Reports

- [Pytest HTML Report](https://soumyo001.github.io/books-to-scrape-automation/report.html)
- [Allure Report](https://soumyo001.github.io/books-to-scrape-automation/allure-report/index.html)
- [Pytest Execution Log](https://soumyo001.github.io/books-to-scrape-automation/pytest.log)

## Features

- Homepage URL, title, heading, and book-list validation.
- Random selection of five books for navigation testing.
- Book title and price consistency validation.
- Homepage hyperlink validation using HTTP responses.
- Product image attribute and visibility validation.
- Pagination validation across a maximum of five catalogue pages.
- Login form submission and authenticated-state validation.
- Reusable page classes and Pytest fixtures.
- Pytest HTML and Allure reporting.
- Screenshot, video, and trace capture configured for failures.
- Docker-based test execution.
- GitHub Actions automation and GitHub Pages report publishing.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| Playwright Python 1.63.0 | Browser automation |
| Pytest 9.1.1 | Test execution and organization |
| pytest-playwright 0.10.0 | Playwright integration with Pytest |
| pytest-html 4.2.0 | HTML test reporting |
| allure-pytest 2.16.2 | Allure result generation |
| Allure Commandline 2.46.1 | Allure HTML report generation |
| Chromium | Browser used for automated tests |
| Docker | Containerized test execution |
| GitHub Actions | CI/CD automation |
| GitHub Pages | Publishing test reports |

## Installation Guide

### Prerequisites

Install Python 3.12 and Git. Docker is required if you want to run the tests in a container.

For local Allure HTML report generation, Java and Node.js/npm are also required.

### Clone the Repository

```bash
git clone https://github.com/Soumyo001/books-to-scrape-automation.git
cd books-to-scrape-automation
```

### Create a Virtual Environment

On Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install --with-deps chromium
```

## Environment Setup

The project configuration is maintained in `config.py`, which defines:

- `BOOKS_HOME_URL`
- `BOOKS_HOME_TITLE`
- `QUOTES_HOME_URL`

No `.env` file or additional environment variables are required for local test execution.

The login test uses the sandbox credentials defined in `tests/test_login_logout.py`.

## Running Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Run the smoke test:

```bash
python -m pytest -m smoke -v
```

Run an individual test module:

```bash
python -m pytest tests/test_book_navigation.py -v
```

Other available modules are:

```bash
python -m pytest tests/test_book_data_consistency.py -v
python -m pytest tests/test_broken_links.py -v
python -m pytest tests/test_product_images.py -v
python -m pytest tests/test_login_logout.py -v
```

### Docker Execution

Build the Docker image:

```bash
docker build -t books-to-scrape-tests .
```

Run the test suite inside the container:

```bash
docker run --name books-to-scrape-check --init --ipc=host books-to-scrape-tests
```

To copy the generated Pytest report and raw Allure results to the host before removing the container:

```bash
mkdir -p ../books-to-scrape-docker-output

docker cp books-to-scrape-check:/app/report.html \
  ../books-to-scrape-docker-output/report.html

docker cp books-to-scrape-check:/app/allure-results \
  ../books-to-scrape-docker-output/allure-results

docker rm books-to-scrape-check
```

The Docker image generates raw Allure results but does not install the Allure Commandline tool. Generate the Allure HTML report separately using the Allure Report Guide.

## Project Structure

```text
books-to-scrape-automation/
├── .github/
│   └── workflows/
│       └── playwright.yml
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── book_details_page.py
│   ├── quotes_home_page.py
│   └── quotes_login_page.py
├── tests/
│   ├── test_smoke.py
│   ├── test_book_navigation.py
│   ├── test_book_data_consistency.py
│   ├── test_broken_links.py
│   ├── test_product_images.py
│   └── test_login_logout.py
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── LICENSE
└── README.md
```

## Test Case Coverage

The current test suite contains 14 test cases across the six assignment scenarios.

| Test case | Test module | Coverage |
|---|---|---|
| 1. Homepage Validation | `test_smoke.py` | Validates URL, title, visible headings, heading text, and the book list. |
| 2. Random Book Navigation Validation | `test_book_navigation.py` | Five parameterized cases validate book navigation, details-page title, book information, and return navigation. |
| 3. Book Data Consistency Validation | `test_book_data_consistency.py` | Five parameterized cases compare homepage and details-page titles and prices. |
| 4. Broken Link Validation | `test_broken_links.py` | Validates homepage anchor URLs and checks for HTTP 200 responses. |
| 5. Product Image Validation | `test_product_images.py` | Checks image visibility, `src`, `alt`, the `thumbnail` class, and pagination across up to five pages. |
| 6. Login Functionality and Logout Link Validation | `test_login_logout.py` | Validates login submission, authenticated state, and the visibility and enabled state of the Logout link. |

The five navigation cases and five data-consistency cases use randomly selected, distinct book indices.

## Report Generation Guide

The report options are configured in `pytest.ini`.

Run the test suite to generate the Pytest HTML report and raw Allure results:

```bash
python -m pytest -v
```

The generated files are:

- `report.html` — Pytest HTML report.
- `allure-results/` — raw Allure test results.
- `test-results/` — Playwright output directory for configured test artifacts.

Generate the Allure HTML report using the command in the Allure Report Guide.

## HTML Report Guide

The Pytest HTML report is generated automatically when tests run.

On Linux, open the report with:

```bash
xdg-open report.html
```

Alternatively, open `report.html` directly in a browser.

## Allure Report Guide

Install Java and Node.js/npm, then install the Allure Commandline tool:

```bash
npm install --global allure-commandline@2.46.1
```

Run the tests to generate `allure-results/`:

```bash
python -m pytest -v
```

Generate the HTML report:

```bash
allure generate allure-results --clean -o allure-report
```

Open the report:

```bash
allure open allure-report
```

## GitHub Actions Setup

The workflow is located at `.github/workflows/playwright.yml`.

It runs automatically on push and pull request events and can also be triggered manually.

The pipeline installs the required dependencies and Chromium browser, executes the test suite, generates Pytest and Allure reports, and uploads the reports and available test artifacts.

The workflow publishes the generated report site to GitHub Pages for eligible runs on the repository's default branch. Pull requests run the tests but do not publish a Pages deployment.

Published results:

- [Pytest HTML Report](https://soumyo001.github.io/books-to-scrape-automation/report.html)
- [Allure Report](https://soumyo001.github.io/books-to-scrape-automation/allure-report/index.html)
- [Pytest Execution Log](https://soumyo001.github.io/books-to-scrape-automation/pytest.log)

## Design Decisions

- **Object-Oriented Programming:** Page classes encapsulate page-specific locators and UI interactions.
- **Modularity:** Test modules are separated by functional scenario.
- **Reusability:** Shared fixtures and page methods reduce repeated setup and interaction logic.
- **Configuration separation:** Website URLs and the expected homepage title are defined in `config.py`.
- **Synchronization:** Playwright's built-in waiting and `expect` assertions are used instead of hardcoded sleeps.
- **Reporting:** Pytest HTML reporting and Allure reporting provide separate views of test execution.
- **Execution separation:** Docker supports local containerized execution, while GitHub Actions runs the CI/CD pipeline and publishes reports.

## Known Limitations

- **Browser coverage:** The current configuration uses Chromium only.
- **External website dependency:** Results depend on the availability and behavior of the public sandbox websites.
- **Random selection:** The five books selected for navigation and data-consistency tests may differ between runs.
- **Broken-link scope:** The test checks links collected from the homepage, not every link throughout the catalogue.
- **Pagination scope:** Product image validation visits a maximum of five catalogue pages.
- **Image loading:** The image test validates visibility and required attributes but does not independently assert that each image loaded successfully at the browser level.
- **Logout behavior:** The login test verifies that the Logout link becomes visible and enabled but does not click it or verify the logged-out state.
- **Report history:** Local reports are regenerated on subsequent runs. Historical results are not automatically preserved by the local configuration.
