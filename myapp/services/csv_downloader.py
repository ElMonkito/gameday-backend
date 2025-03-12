import os
import logging
from playwright.sync_api import sync_playwright
from apscheduler.schedulers.background import BackgroundScheduler
import time

UPLOADS_FOLDER = os.path.abspath("../../uploads")
FIXED_FILENAME = "matchs.csv"

# Configuration des logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def download_csv():
    """Télécharge le fichier CSV et le sauvegarde dans le bon dossier."""
    logging.info("Début du téléchargement du fichier CSV...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.sihf.ch/fr/game-center/other-leagues#/today/time/asc/page/0/")
        page.wait_for_load_state("networkidle")

        with page.expect_download() as download_info:
            page.click(".fa.fa-table.u-pull-right")

        download = download_info.value
        fixed_path = os.path.join(UPLOADS_FOLDER, FIXED_FILENAME)

        if os.path.exists(fixed_path):
            os.remove(fixed_path)
            logging.info("Ancien fichier supprimé.")

        download.save_as(fixed_path)
        logging.info(f"CSV téléchargé avec succès : {fixed_path}")

        browser.close()


os.makedirs(UPLOADS_FOLDER, exist_ok=True)

scheduler = BackgroundScheduler()
scheduler.add_job(download_csv, "cron", hour=1, minute=0)
scheduler.start()

logging.info("Planificateur APScheduler démarré. Le script tournera en tâche de fond.")

try:
    while True:
        time.sleep(60)
except (KeyboardInterrupt, SystemExit):
    logging.info("Arrêt du script...")
    scheduler.shutdown()
