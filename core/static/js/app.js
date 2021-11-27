function validar(){
    var nombre_producto,detalle_producto,cantidad_disponible,
    fecha_compra,valor_unitario,id_empleado, expresion;

    nombre_producto = document.getElementById("nombre_producto").value;
    detalle_producto = document.getElementById("detalle_producto").value;
    cantidad_disponible = document.getElementById("cantidad_disponible").value;
    fecha_compra = document.getElementById("fecha_compra").value;
    valor_unitario = document.getElementById("valor_unitario").value;
    id_empleado = document.getElementById("id_empleado").value;

    expresion = /(^(((0[1-9]|1[0-9]|2[0-8])[-](0[1-9]|1[012]))|((29|30|31)[-](0[13578]|1[02]))|((29|30)[-](0[4,6,9]|11)))[-](19|[2-9][0-9])\d\d$)|(^29[-]02[-](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)/;


    if(nombre_producto === "" || detalle_producto === "" || cantidad_disponible === "" || cantidad_disponible === "" || fecha_compra === "" || valor_unitario === "" || id_empleado === ""){
        alert("Todos los campos son obligatorios");
        return false;
    }
    else if (nombre_producto.length>30){
        alert("El nombre del producto es demasiado largo");
        return false;

    }
    else if (detalle_producto.length>120){
        alert("El detalle del producto es demasiado largo");
        return false;

    }
    else if (cantidad_disponible.length>10){
        alert("La cantidad del producto es demasiado largo");
        return false;

    }
    else if (isNaN(cantidad_disponible)){
        alert("La cantidad debe ser un número");
        return false;

    }
    //fecha_compra
    


    else if (valor_unitario.length>10){
        alert("El valor unitario es demasiado largo");
        return false;

    }
    else if (isNaN(valor_unitario)){
        alert("El valor debe ser un número");
        return false;

    }

    
    
}