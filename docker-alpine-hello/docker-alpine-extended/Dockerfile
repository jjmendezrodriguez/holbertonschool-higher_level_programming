# Especificar la imagen base
FROM alpine

# Instalar el paquete curl usando el gestor de paquetes apk de Alpine
RUN apk add --no-cache curl

# Copiar el archivo config.txt al directorio /app en el contenedor
COPY config.txt /app/config.txt

# Especificar un volumen en /data
VOLUME /data

# Comando por defecto que se ejecutará al iniciar el contenedor
CMD ["echo", "Hello, World!"]
