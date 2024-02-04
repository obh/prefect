###Activate conda
```source .venv/bin/activate```

###Start Server
```prefect server start```

###Run Deployment
```prefect deployment run 'get-repo-info/my-first-deployment'```


##mysql
 CREATE TABLE IF NOT EXISTS clients (
                id INT AUTO_INCREMENT PRIMARY KEY,
                provider VARCHAR(50) NOT NULL,
                client_id VARCHAR(100) NOT NULL,
                credentials JSON DEFAULT NULL,
                status VARCHAR(255),
                added_on DATETIME,
                updated_on DATETIME 
            )