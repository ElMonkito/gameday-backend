import os
from playwright.sync_api import sync_playwright

UPLOADS_FOLDER = os.path.abspath("../../uploads")
FIXED_FILENAME = "matchs.csv"


def download_csv():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.sihf.ch/fr/game-center/heute/#/today/time/asc/page/0/")

        page.wait_for_load_state("networkidle")

        with page.expect_download() as download_info:
            page.click(".fa.fa-table.u-pull-right")

        download = download_info.value

        fixed_path = os.path.join(UPLOADS_FOLDER, FIXED_FILENAME)

        if os.path.exists(fixed_path):
            os.remove(fixed_path)
            print("Delete old file.")

        download.save_as(fixed_path)
        print(f"CSV file download successfuly : {fixed_path}")

        browser.close()


os.makedirs(UPLOADS_FOLDER, exist_ok=True)

download_csv()