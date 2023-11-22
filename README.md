# docker_scraping_seleniun_basic
repositorio completo funcionando ....
docker con una imagen de python 
donde se instala dentro de la imagen selenium y google chrome  para poder hacer scrapping o automatizar
esta es la estructura que deberia quedar en el docker  ojo el docker file por algun motivo me copia el main.py dentro de app y despues no encuentra 
a  el archivo de selenium, por mas vueltas que di no pude ejecutar y que sea en el mimsmo directorio

![proy3](https://github.com/marcosfacundoperini1979/docker_scraping_seleniun_basic/assets/125610561/06483441-ef6b-4728-8fe8-5ca4e2e3ead1)

una vez copiado el repo... es necesario ejecutar la instalacion  previamente teniendo instalado docker.io   en el caso de kali linux
usando el comando  build 
sudo docker build -t proyecto_docker_selenium .


con esto creamos la imagen 

luego 
con el id del contenedor        
sudo start <id contenedor o nombre>

sudo docker ps

verificiamos que este corriendo  no exited, el docker 

luego ingresamos al bash usando ele  siguiente comando

sudo docker exec -it <nommbre o id del container> /bin/bash

 a veces es necesario darle permisos 
 dentro del contenedor a chromedriver

 chmod +x /app/chromedriver


ejecutamos python3 main.py dentro del bash del contenedor   y listo  
 ![proy1](https://github.com/marcosfacundoperini1979/docker_scraping_seleniun_basic/assets/125610561/ca07eb77-17ba-431f-a0e7-ec8729f367c9)

 verificamos el screenshot que realizo  y guardo dentro del docker..... lo dificil fue la configuracion por eso dejo los repo del chrome driver y selenium
que funcionan el resto queda a vuestra imaginacion saludos!!!


![proy2](https://github.com/marcosfacundoperini1979/docker_scraping_seleniun_basic/assets/125610561/1160da99-9122-4d7a-ba1b-69c9c706177e)

