import pytest, re
from urllib.parse import urljoin
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

@pytest.mark.regression
def test_product_images_and_pagination(home_page: Page) -> None:
    catalogue = HomePage(home_page)

    pages_checked = 0

    for expected_page in range(1, 6):
        expect(catalogue.pager).to_be_visible()
        pagination_text = catalogue.pager.inner_text()
        match = re.search(r"Page\s+(\d+)\s+of\s+(\d+)", pagination_text)

        assert match is not None, f"Invalid pagination information: {pagination_text}"

        current_page = int(match.group(1))
        total_pages = int(match.group(2))

        assert current_page == expected_page, f"Expected page {expected_page}, found page {current_page}"
        assert current_page <= total_pages, "Current page exceeds total page count"

        images = catalogue.product_images

        expect(images.first).to_be_visible()
        image_count = images.count()

        assert image_count > 0, f"No product images found on page {current_page}"

        print()
        for index in range(image_count):
            image = images.nth(index)

            expect(image).to_be_visible()

            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            classes = image.get_attribute("class")

            assert src and src.strip(), f"Page {current_page}, image {index+1}: Missing src"
            assert alt and alt.strip(), f"Page {current_page}, image {index+1}: Missing alt"
            assert classes and "thumbnail" in classes.split(), f"Page {current_page}, image {index+1}: Missing thumbnail class"

        pages_checked += 1
        print(f"Page {current_page}: {image_count} product images validated")

        if pages_checked == 5 or current_page == total_pages:
            break

        assert catalogue.next_link.count() == 1, f"Next link missing on page {current_page} of {total_pages}"
        expect(catalogue.next_link).to_be_visible()
        expect(catalogue.next_link).to_be_enabled()

        next_href = catalogue.next_link.get_attribute("href")

        assert next_href and next_href.strip(), f"Next link has no valid href on page {current_page}"

        current_url = home_page.url
        expected_url = urljoin(current_url, next_href)

        assert expected_url != current_url, "Next link points to the current page"

        catalogue.open_next_page()

        expect(home_page).to_have_url(expected_url)

    print(f"Total catalouge pages validated: {pages_checked}")