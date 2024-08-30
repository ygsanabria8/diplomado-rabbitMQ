## Caso: Registro de Usuario y envio de email de registrado

1. Se crea un productor que envia un mensaje de un json de un usuario con correo electronico
2. Se crea consumidor donde se lee el mensaje recibido y envia el correo electronico
3. La cola se llama user created para tener topicos diferentes acorde a cada necesidad