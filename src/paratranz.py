from zipfile import ZipFile, BadZipfile

import os
import contextlib
import httpx

from .consts import *
from .log import logger


class Paratranz:
    """Downloading localization package"""
    def __init__(self, type_: str = "common"):
        self._type = type_
        self._project_id = PARATRANZ_PROJECT_DOL_ID
        self._mention_name = "" if self._type == "common" else "dev"

    async def download_from_paratranz(self) -> bool:
        """Download language version from paratranz"""
        os.makedirs(DIR_PARATRANZ, exist_ok=True)
        with contextlib.suppress(httpx.TimeoutException):
            await self.trigger_export()

        async with httpx.AsyncClient(verify=False) as client:
            flag = False
            for _ in range(3):
                try:
                    await self.download_export(client)
                    await self.unzip_export()
                except (httpx.ConnectError, httpx.TimeoutException, BadZipfile) as e:
                    continue
                else:
                    flag = True
                    break
            if not flag:
                logger.error(f"***** Unable to download Paratranz {self._mention_name} package! Please check your network and fill correct TOKEN!\n")
                return False
            return True

    async def trigger_export(self):
        """Trigger export"""
        logger.info(f"===== Start exporting {self._mention_name} translation files ...")
        url = f"{PARATRANZ_BASE_URL}/projects/{self._project_id}/artifacts"
        httpx.post(url, headers=PARATRANZ_HEADERS, verify=False)
        logger.info(f"##### {self._mention_name} files have been exported!\n")

    async def download_export(self, client: httpx.AsyncClient):
        """Download export"""
        logger.info(f"===== Start downloading {self._mention_name} translation files ...")
        url = f"{PARATRANZ_BASE_URL}/projects/{self._project_id}/artifacts/download"
        headers = PARATRANZ_HEADERS
        content = (await client.get(url, headers=headers, follow_redirects=True)).content
        with open(DIR_TEMP_ROOT / f"paratranz_export{self._mention_name}.zip", "wb") as fp:
            fp.write(content)
        logger.info(f"##### {self._mention_name} translation file has been downloaded!\n")

    async def unzip_export(self):
        """Unzip"""
        logger.info(f"===== Start decompressing {self._mention_name} translation file ...")
        with ZipFile(DIR_TEMP_ROOT / f"paratranz_export{self._mention_name}.zip") as zfp:
            zfp.extractall(DIR_PARATRANZ / self._type)
        logger.info(f"##### {self._mention_name} translation file has been unzipped!\n")


__all__ = [
    "Paratranz"
]

