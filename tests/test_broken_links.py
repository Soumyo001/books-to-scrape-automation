import pytest
from urllib.parse import urljoin, urlsplit
from playwright.sync_api import Error, Page
from pages.home_page import HomePage

@pytest.mark.regression
def test_homepage_links_return_http_200(home_page: Page) -> None:
    homepage = HomePage(home_page)
    anchors = homepage.all_links
    total_anchors = anchors.count()

    assert total_anchors > 0, "No links found on homepage"

    unique_urls = set()
    for index in range(total_anchors):
        href = anchors.nth(index).get_attribute("href")

        assert href is not None and href.strip(), f"Anchor {index} has a missing or empty href"

        absolute_url = urljoin(home_page.url, href)

        assert urlsplit(absolute_url).scheme in ("http", "https"), f"Unsupported link url: {absolute_url}"

        unique_urls.add(absolute_url)

    broken_links = []

    for url in sorted(unique_urls):
        try:
            response = home_page.request.get(url, max_redirects=0, fail_on_status_code=False)
        except Error as e:
            broken_links.append(f"Request failed on {url}: {e}")
            continue

        if response.status != 200:
            broken_links.append(f"{url} HTTP STATUS {response.status}")

    print(f"\nTotal anchors found: {total_anchors}")
    print(f"Unique URLs checked: {len(unique_urls)}")

    
    assert not broken_links, (
        f"{len(broken_links)} links did not return HTTP 200:\n"
        + "\n".join(broken_links)
    )