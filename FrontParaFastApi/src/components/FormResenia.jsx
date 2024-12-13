import React from 'react';
import axiosInstance from '../api/axioInstance';


const cargarButton = async (e) => {
    e.preventDefault();
    const idProducto = document.querySelector("#idProducto").value;
    const idUsuario = document.querySelector("#idUsuario").value;
    const calificacion  = document.querySelector("#calificacion").value;
    const comentario = document.querySelector("#comentario").value;

    const nuevoRegistro = {
      idProducto,
      idUsuario,
      calificacion,
      comentario
      
    }
    console.log(nuevoRegistro)
    try {
      const response =  await axiosInstance.post("http://localhost:8000/tienda_crear_resenia", nuevoRegistro);
      console.log("el nuevo registro fue un exito..." , nuevoRegistro)
      console.log(response)
    } catch (error) {
      if (error.response) {
        console.error("Error del servidor:", error.response.data);
      } else {
        console.error("Error de la solicitud:", error.message);
      }

    }
}

const Formresenia = () => {
  return (
    <>
    <div className='container'>

      <div className="containerForm">
        <h2>Formulario reseña</h2>
        <form>
            <fieldset>
              <label htmlFor="idProducto">Nombre del producto</label>
              <input type="text" id='idProducto' required />  
            </fieldset>          
            <fieldset>
              <label htmlFor="idUsuario">usuario</label>
              <input type="text" id='idUsuario' required />
            </fieldset>
            <fieldset>
              <label htmlFor="calificacion">calificacion</label>
              <input type="text" id='calificacion' required />
            </fieldset>
            <fieldset>
              <label htmlFor="comentario">comentario</label>
              <input type="text" id='comentario' required />
            </fieldset>
            <button type='submit' onClick={cargarButton}>Cargar</button>
        </form>
      </div>
    </div>
    </>
  )
}

export default Formresenia