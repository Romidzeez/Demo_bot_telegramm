from decouple import config
import asyncpg





async def Pars_from_users(row:str,
                          param= None, 
                          disable_param=False, 
                          all_from=True):
    conn = await asyncpg.connect(user=config("USER"), password=config("PASSWORD"),
                                 database=config("DB_NAME"), host=config("HOST"), port=config("PORT"), timeout=120 )

    
    f"""
    
    
    функция для получения данных с бд
    возвращает столбик данных по условию WHERE <param>
    :param param:то что нужно найти в базе данных


        """
    try:
        if disable_param == False and all_from== True:
            rows = await conn.fetch(f'SELECT * FROM "users" WHERE {param}')

            rowret= [dict(row) for row in rows]
            # return [dict(row) for row in rows]
        if disable_param == False and all_from== False:
            rows = await conn.fetch(f'SELECT "{row}" FROM "users" WHERE {param}')
            rowret= [dict(row) for row in rows]
            # return [dict(row) for row in rows]
        elif disable_param == True and all_from==False:
            rows = await conn.fetch(f'SELECT "{row}" FROM "users"')
            rowret= [dict(row) for row in rows]
        
            # return [dict(row) for row in rows]
        elif disable_param == True and all_from==True:
            rows = await conn.fetch(f'SELECT * FROM "users"')
            rowret= [dict(row) for row in rows]
        names=[]
        row1= rows[0]
        for x in row1:
            names.append(x)
        ret=''
        for row in rows:
            for name in names:

                ret+=f"{row}"
        
        
    finally: conn.close()
    
    
    


# async def Connection_DB():
#     await conn = await asyncpg.connect(user=config("USER"), password=config("PASSWORD"),
#                                  database=config("DATABASE"), host=config("HOST"), port=config("port"), timeout=120 )