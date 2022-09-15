from leanapi.server import router
from leanapi.path import controller
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse
from sqlraw.sqlraw import SqlRaw

from fastapi import Body

from api.config import Config


class AirFreeTable(BaseModel):
    id: int
    name: str
    image_path: str
    site: str
    coin_nft_link: str
    whitepaper: str
    coin_marketcap_link: str
    total_supply: int
    is_active: bool
    platform: str


@controller("app", router)
class AirFree:
    @router.get('/airfree/{coin_id}', status_code=status.HTTP_200_OK)
    async def read_database(self, coin_id: int):
        sqlraw = SqlRaw.paths(['api/routes/airfree/models'])
        sqlraw.load('coin_name').connect(Config.conn)
        liste = sqlraw.fetchone({"coin_id": coin_id})
        if liste:
            return liste
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="coin name not found")

    @router.post('/airfree/create', status_code=status.HTTP_200_OK)
    async def create_database(self, values: list[AirFreeTable] = Body(..., embed=True)):
        sqlraw = SqlRaw.paths(['api/routes/airfree/models'])
        sqlraw.load('database_insert.sql').connect(Config.conn)
        liste = sqlraw.fetchall({"values": values})
        return "success"

    @router.put('/airfree/{coin_id}', status_code=status.HTTP_200_OK)
    async def update_database(self,
                              coin_id: int,
                              name: str = Body(..., embed=True),
                              image_path: str = Body(..., embed=True),
                              site: str = Body(..., embed=True),
                              coin_nft_link: str = Body(..., embed=True),
                              whitepaper: str = Body(..., embed=True),
                              coin_marketcap_link: str = Body(..., embed=True),
                              total_supply: int = Body(..., embed=True),
                              is_active: bool = Body(..., embed=True),
                              platform: str = Body(..., embed=True)):
        sqlraw = SqlRaw.paths(['api/routes/airfree/models'])
        sqlraw.load('database_update.sql').connect(Config.conn)
        liste = sqlraw.fetchall({"coin_id": coin_id,
                                 "name": name,
                                 "image_path": image_path,
                                 "site": site,
                                 "coin_nft_link": coin_nft_link,
                                 "whitepaper": whitepaper,
                                 "coin_marketcap_link": coin_marketcap_link,
                                 "total_supply": total_supply,
                                 "is_active": is_active,
                                 "platform": platform})

        if liste:
            return {"list": liste}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="coind id not found")
