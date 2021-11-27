function validar(){
    var id,nombre_receta, detalle_receta, imagen_receta, valor_receta, expresion;

    id = document.getElementById("id").value;
    nombre_receta = document.getElementById("nombre_receta").value;
    detalle_receta = document.getElementById("detalle_receta").value;
    imagen_receta = document.getElementById("imagen_receta").value;
    valor_receta= document.getElementById("valor_receta").value;
    

   


    if(id === "" || nombre_receta === "" || detalle_receta=== "" || imagen_receta === "" || valor_receta === "" ){
        alert("Todos los campos son obligatorios");
        return false;
    }
    else if (id.length>10){
        alert("La id de la receta es demasiado largo");
        return false;

    }
    else if (nombre_receta.length>60){
        alert("El nombre de la receta es demasiado largo");
        return false;

    }
    else if (detalle_receta.length>120){
        alert("El detalle de la receta es demasiado largo");
        return false;

    }
  
    else if (valor_receta.length>10){
        alert("El valor de la receta es demasiado largo");
        return false;

    }
    else if (isNaN(valor_receta)){
        alert("El valor debe ser un número");
        return false;


    }
}