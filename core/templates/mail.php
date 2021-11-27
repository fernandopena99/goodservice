<?php
if (isset($_POST['enviar'])){
    if (!empty($_POST['form_name']) && !empty($_POST['email']) && !empty($_POST['phone']) && !empty($_POST['num_persons']) && !empty($_POST['date_picker']) && !empty($_POST['time_picker']) && !empty($_POST['preferred_food']) && !empty($_POST['occasion'])){
        
        $nombre = $_POST["form_name"];
        $email = $_POST["email"];
        $phone = $_POST["phone"];
        $num_persons = $_POST["num_persons"];
        $date_picker = $_POST["date_picker"];
        $time_picker = $_POST["time_picker"];
        $preferred_food = $_POST["preferred_food"];
        $occasion = $_POST["occasion"];
        $asunto = "Confirmacion de reserva";
        $body = "Correo de confirmacion de reserva para: " . $nombre . "\n\n".
        "Nombre: " . $nombre ."\n" .
        "Correo: " . $email ."\n" .
        "Telefono: " . $phone ."\n".
        "Numero de Personas: " . $num_persons ."\n".
        "Fecha: " . $date_picker ."\n".
        "Hora: " . $time_picker ."\n".
        "Comida Preferida: " . $preferred_food ."\n".
        "Ocasion: " . $occasion;
        $header = "From: noreplyexample.com" . "\n";
        $header.= "Reply-To: noreply@example.com" . "\n";
        $header.= "X-Mailer: PHP/". phpversion();
        $mail = mail($email,$asunto,$body,$header);
        if ($mail){
            echo '<script language="javascript">alert("mensaje enviado!");</script>';
            echo '<script> window.history.go(-1)</script>';
        }
    }
}

