# UI Automation Framework – Books to Scrape

A UI automation framework built with **Python, Playwright, and Pytest** to validate website functionality, book navigation, data consistency, hyperlinks, product images, pagination, and login behavior.

The project supports local execution, Docker-based execution, automated testing through GitHub Actions, and publishing test reports through GitHub Pages.

## Project Overview

This project automates functional and basic quality-assurance scenarios for two public sandbox websites:

- **Books to Scrape:** Homepage validation, random book navigation, book data consistency, broken-link validation, product image validation, and pagination.
- **Quotes to Scrape:** Login functionality and validation of the authenticated page's Logout link.

The framework uses Pytest for test organization and execution, Playwright for browser automation, reusable page classes for UI interactions, and fixtures for test setup and resource management.

Automated test results are available through Pytest HTML reports, Allure reports, and GitHub Actions execution logs.

### Live Test Reports

The latest published reports are available here:

- [Automation Reports Dashboard](https://soumyo001.github.io/books-to-scrape-automation/)
- [Pytest HTML Report](https://soumyo001.github.io/books-to-scrape-automation/report.html)
- [Allure Report](https://soumyo001.github.io/books-to-scrape-automation/allure-report/index.html)
- [Pytest Execution Log](https://soumyo001.github.io/books-to-scrape-automation/pytest.log)

The published reports are updated by the GitHub Actions workflow when it deploys a new report from the repository's default branch.

## Features

- Automated homepage URL and page-title validation.
- Validation of visible headings and non-empty heading text.
- Random selection of five books for navigation testing.
- Verification that book details pages display the expected title and book information.
- Comparison of book titles and prices between the homepage and details pages.
- Validation of unique homepage hyperlinks against HTTP 200 responses.
- Product image visibility and required attribute validation.
- Pagination validation across a maximum of five catalogue pages.
- Login form submission and authenticated-state validation on Quotes to Scrape.
- Reusable page classes and Pytest fixtures.
- Automatic Pytest HTML report generation.
- Allure test-result generation and HTML report generation.
- Screenshot, video, and trace capture configured for test failures.
- Docker-based local execution.
- GitHub Actions automation on push and pull request events.
- GitHub Pages publishing for viewing reports online.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language and CI runtime |
| Playwright Python 1.63.0 | Browser automation |
| Pytest 9.1.1 | Test framework |
| pytest-playwright 0.10.0 | Pytest integration and browser fixtures |
| pytest-html 4.2.0 | HTML test reporting |
| allure-pytest 2.16.2 | Allure test-result generation |
| Allure Commandline 2.46.1 | Allure HTML report generation |
| Chromium | Configured test browser |
| Java 21 | Runtime for the local Allure CLI |
| Node.js 24 and npm | Allure CLI installation in CI |
| Docker | Containerized test execution |
| GitHub Actions | CI/CD automation |
| GitHub Pages | Publishing HTML reports |

Python dependencies and their versions are pinned in `requirements.txt`.

## Installation Guide

### Prerequisites

For local execution, install:

- Python 3.12
- Git
- A supported operating system for Playwright and Chromium

Docker is required only if you want to run the project in a container.

To generate an Allure HTML report locally, you also need Java and Node.js/npm to install and run the Allure Commandline tool.

### Clone the Repository

```bash
git clone https://github.com/Soumyo001/books-to-scrape-automation.git
cd books-to-scrape-automation
```

### Create a Virtual Environment

On Linux or macOS:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install Python Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Install the Playwright Browser

On Ubuntu/Linux:

```bash
python -m playwright install --with-deps chromium
```

On other supported operating systems, use:

```bash
python -m playwright install chromium
```

The project is now ready for local test execution.

## Environment Setup

The website URLs and expected Books to Scrape page title are centralized in `config.py`.

The current configuration includes:

- `BOOKS_HOME_URL`
- `BOOKS_HOME_TITLE`
- `QUOTES_HOME_URL`

No `.env` file or environment variables are required by the current implementation.

The login test uses the sandbox credentials defined directly in `tests/test_login_logout.py`. These are for the public test website, not personal or production credentials.

If the target websites or their authentication behavior change, the corresponding configuration or test implementation may need to be updated.

## Running Tests

Run the complete test suite from the repository root:

```bash
python -m pytest -v
```

Pytest uses `pytest.ini` to configure Chromium, HTML reporting, Allure results, and failure artifact capture.

### Run the Smoke Test

```bash
python -m pytest -m smoke -v
```

### Run Individual Test Modules

Book navigation:

```bash
python -m pytest tests/test_book_navigation.py -v
```

Book data consistency:

```bash
python -m pytest tests/test_book_data_consistency.py -v
```

Broken-link validation:

```bash
python -m pytest tests/test_broken_links.py -v -s
```

Product images and pagination:

```bash
python -m pytest tests/test_product_images.py -v -s
```

Login and Logout link validation:

```bash
python -m pytest tests/test_login_logout.py -v
```

The default configuration uses Chromium. The random-book fixture selects five distinct book indices for each relevant test module execution.

## Docker Execution

Docker allows the tests to run in an environment based on the official Playwright Python image, without requiring the project dependencies to be installed in a local Python virtual environment.

### Build the Docker Image

From the project root:

```bash
docker build -t books-to-scrape-tests .
```

### Run the Tests

```bash
docker run --name books-to-scrape-check --init --ipc=host books-to-scrape-tests
```

The container executes:

```bash
python -m pytest -v
```

The test reports are initially generated inside the container.

### Copy Reports to the Host

After the container finishes, copy the reports before removing the container:

```bash
mkdir -p ../books-to-scrape-docker-output

docker cp books-to-scrape-check:/app/report.html \
  ../books-to-scrape-docker-output/report.html

docker cp books-to-scrape-check:/app/allure-results \
  ../books-to-scrape-docker-output/allure-results

docker rm books-to-scrape-check
```

The Pytest HTML report and Allure raw results are now available on the host.

The Docker image does not install the Allure Commandline tool. To generate an Allure HTML report from the copied results, install the CLI on the host and follow the Allure Report Guide below.

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

Generated reports and test artifacts are output files rather than source modules. The `.gitignore` and `.dockerignore` files exclude generated reports, test artifacts, virtual environments, and other files that should not be included in normal source control or Docker build contexts.

## Test Case Coverage

The current suite contains 14 test cases across six functional scenarios.

| Assignment test case | Test module | Coverage |
|---|---|---|
| 1. Homepage Validation | `test_smoke.py` | URL, title, visible headings, non-empty heading text, books section, and book items |
| 2. Random Book Navigation Validation | `test_book_navigation.py` | Five parameterized cases checking book navigation, details-page title, information table, and return navigation |
| 3. Book Data Consistency Validation | `test_book_data_consistency.py` | Five parameterized cases comparing homepage and details-page titles and prices |
| 4. Broken Link Validation | `test_broken_links.py` | Unique homepage URLs, valid HTTP(S) schemes, and HTTP 200 responses |
| 5. Product Image Validation | `test_product_images.py` | Image visibility, `src`, `alt`, `thumbnail` class, and pagination over up to five pages |
| 6. Login Functionality and Logout Link Validation | `test_login_logout.py` | Login page, form submission, authenticated state, and visible, enabled Logout link |

The five navigation cases and five data-consistency cases are parameterized Pytest cases. Their selected book indices are chosen randomly, so the exact books can differ between runs.

## Report Generation Guide

The project is configured to generate reports through `pytest.ini`.

The relevant options include:

- `--html=report.html`: generates the Pytest HTML report.
- `--self-contained-html`: embeds the report's required resources.
- `--alluredir=allure-results`: writes raw Allure result files.
- `--clean-alluredir`: clears previous Allure results before the next test run.
- `--screenshot=only-on-failure`: captures screenshots on failure.
- `--video=retain-on-failure`: retains videos on failure.
- `--tracing=retain-on-failure`: retains Playwright traces on failure.
- `--output=test-results`: configures the Playwright artifact output directory.

Run:

```bash
python -m pytest -v
```

The Pytest HTML report is written to `report.html`, and raw Allure results are written to `allure-results/`.

Failure screenshots, videos, and traces are retained according to the Playwright configuration. On successful local runs, the artifact directory may contain no failure artifacts.

Because `--clean-alluredir` is enabled, a subsequent test run replaces the previous Allure results. Generate or preserve any report you need before running another test command.

## HTML Report Guide

The Pytest HTML report is generated automatically during test execution.

To open it locally on Linux:

```bash
xdg-open report.html
```

Alternatively, open `report.html` directly in a browser.

The report displays the test results, execution durations, environment details, and test summary.

The report is regenerated by each Pytest run, so the file reflects the most recent run rather than preserving a historical record.

## Allure Report Guide

The project generates Allure result files during Pytest execution. The Allure Commandline tool converts those results into a browsable HTML report.

### Install Allure Commandline

Install Java and Node.js/npm first, then run:

```bash
npm install --global allure-commandline@2.46.1
```

Verify the installation:

```bash
java -version
allure --version
```

### Generate the Allure Report

Run the test suite:

```bash
python -m pytest -v
```

Generate the HTML report:

```bash
allure generate allure-results --clean -o allure-report
```

Open the generated report:

```bash
allure open allure-report
```

The Allure report includes test cases, results, execution information, and any supported attachments recorded during the run.

The `allure-results/` directory contains raw result data; `allure-report/` contains the generated HTML report. They serve different purposes.

## GitHub Actions Setup

The workflow is located at:

```text
.github/workflows/playwright.yml
```

It is configured to run on:

- Push events
- Pull request events
- Manual workflow dispatch

### Test Pipeline

The workflow:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Sets up Node.js 24 and Java 21 for Allure reporting.
4. Installs Python dependencies.
5. Installs Chromium and its required dependencies.
6. Installs Allure Commandline.
7. Runs Pytest and captures the execution log in `pytest.log`.
8. Generates the Allure HTML report when result files are available.
9. Prepares the static GitHub Pages site.
10. Uploads test reports and artifacts.

The `playwright-test-artifacts` artifact includes the generated HTML report, execution log, Allure results, Allure HTML report, and test artifact directory when available. The configured artifact retention period is 14 days.

### GitHub Pages Publishing

The workflow uses a separate deployment job to publish the report site.

For repository setup:

1. Open the repository's **Settings**.
2. Select **Pages**.
3. Set the publishing source to **GitHub Actions**.

The workflow publishes the reports site for eligible runs on the repository's default branch. Pull requests run the tests but do not publish a Pages deployment.

When a new eligible deployment completes, the landing page links to the generated Pytest HTML report, Allure report, and Pytest execution log.

If a test run fails, the workflow is configured to attempt report generation and publication as long as the run is not cancelled and the deployment conditions are met. This helps make failure results available for investigation.

## Design Decisions

### Object-Oriented Design

The framework uses page classes to encapsulate page-specific locators and reusable UI interactions:

- `HomePage`
- `BookDetailsPage`
- `QuotesHomePage`
- `QuotesLoginPage`

This provides a lightweight Page Object Model structure without introducing unnecessary abstraction.

### Reusable Fixtures

`conftest.py` provides:

- `home_page`: navigates to the Books to Scrape homepage using the Playwright page fixture.
- `random_book_indices`: selects five distinct random book indices using a separate browser context and closes that context after selection.

This avoids repeating common navigation and selection setup across related tests.

### Configuration Separation

Website URLs and the expected homepage title are stored in `config.py`, making these values easier to maintain.

### Synchronization

The tests use Playwright locators, automatic waiting, and Playwright's `expect` assertions instead of fixed sleeps. This helps synchronize actions with page and element state.

### Reporting Separation

Pytest HTML reporting and Allure reporting are configured independently. Pytest produces its HTML report and raw Allure results; Allure Commandline generates the browsable Allure report.

### CI/CD and Docker Separation

Docker provides a local containerized execution path. GitHub Actions provides a separate automated testing and reporting path. GitHub Pages publishes reports generated by the CI workflow.

## Known Limitations

- **Browser coverage:** The current configuration runs Chromium only. Firefox and WebKit are not configured in the default test run.
- **External website dependency:** The tests depend on the availability and behavior of public sandbox websites. Website changes, network failures, or service interruptions can affect results.
- **Random selection:** The five books selected for navigation and data-consistency tests can vary between runs.
- **Broken-link scope:** The broken-link test checks links collected from the homepage, not every link across the complete catalogue.
- **Pagination scope:** Product image validation visits a maximum of five catalogue pages, as specified by the assignment scenario; it does not traverse all 50 pages.
- **Image-load verification:** The current image test checks element visibility and required attributes but does not independently assert that every image has loaded successfully at the browser level.
- **Login scope:** The login test validates the authenticated state and the Logout link's visibility and enabled state. It does not click Logout or verify the subsequent logged-out state.
- **Report history:** Local report files are regenerated, and Allure results are cleaned before each test run. Historical results are not automatically preserved by the current local configuration.

These limitations describe the current implementation and do not imply that the corresponding assignment scenarios have been omitted.
