from __future__ import annotations

import os

from dotenv import find_dotenv
from dotenv import load_dotenv
from facebook_business.api import FacebookAdsApi


_ = load_dotenv(find_dotenv())
META_APP_ID = os.getenv("META_APP_ID")
META_APP_SECRET = os.getenv("META_APP_SECRET")
META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")


def main():
    FacebookAdsApi.init(META_APP_ID, META_APP_SECRET, META_ACCESS_TOKEN)


if __name__ == "__main__":
    main()
