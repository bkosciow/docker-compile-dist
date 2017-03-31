### docker-compile

Used in internal projects. Copy Dockerfile.dist to Dockerfile setting username and group, matching localhost ones. 
  
  
## Dockerfile.dist
  
    FROM bkosciow/compass-full
    
    RUN groupadd -r -g $uid$ $user$ && useradd -r -u $uid$ -g $user$ $user$
    USER $user$
    
    CMD ["php-fpm"]


## compile
Take parameter:

    docker-compile myuser myid

Use .env:
    
    docker-compile