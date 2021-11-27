
function validacion() {
    var nombre_empleado, apellido_empleado, email_empleado, rol_id_rol;

    nombre = document.getElementById("nombre_empleado").value;
    apellido = document.getElementById("apellido_empleado").value;
    email = document.getElementById("email_empleado").value;
    rol = document.getElementById("rol_id_rol").selectedIndex;

    expresion = /\w+@\w+\.+[a-z]/;

    if (nombre == "" || apellido == "" || email == "" || rol == 0) {
        alert("Todos los campos son obligatorios");
        return false;
    } else if (nombre.length > 30) {
        alert("El campo Nombre es muy largo");
        return false;
    } else if (apellido.length > 30) {
        alert("El campo Apellido es muy largo");
        return false;
    } else if (email.length > 30) {
        alert("El campo Email es muy largo");
        return false;
    } else if (!expresion.test(email)) {
        alert("Formato de email incorrecto");
        return false;
    }

    alert("Registro de empleado Exitoso!")
    form.submit();
}