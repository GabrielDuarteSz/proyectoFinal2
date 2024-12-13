from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn

reseniaRouter =  APIRouter()

class resenia(BaseModel):
    idProducto : int
    idUsuario : int
    calificacion : int
    comentario : str
    
    
@reseniaRouter.get("/resenia_tienda/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'Select * from resena'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@reseniaRouter.get("/resenia_tienda_id/{cargo_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(cargo_id: int):
    select_query = "SELECT * FROM resena WHERE idResena = %s"
    cleverCursor.execute(select_query, (cargo_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="resenia no encontrada")
    
@reseniaRouter.post("/tienda_crear_resenia", status_code=status.HTTP_201_CREATED)
def insert_user(reseniaPost: resenia):
    insert_query = """
    INSERT INTO resena (idProducto, idUsuario, calificacion, comentario)
    VALUES (%s, %s,%s,%s)
    """
    values = (reseniaPost.idProducto, reseniaPost.idUsuario, reseniaPost.calificacion, reseniaPost.comentario)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysqlConn.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "User inserted successfully"}


#import hashlib
# Hash the password using SHA-256
# hashed_password = hashlib.sha256(cargoPost.password.encode()).hexdigest()

