# T-DAT-901

### Install and Launch

Copy to the folder `Project_data` from [Drive](https://drive.google.com/drive/folders/1VBhMUqNjBsU9W719EIS9eXOvlr1cH8iX?usp=sharing)

Docker:
```bash
docker-compose up --build -d
```

Install in command line:
```bash
# Install back
conda install --file Api/requirements.txt
# Or
pip install -r Api/requirements.txt

# Install front
npm install --prefix Front
```

Run in command line:
```bash
# Run the api
python Api/app.py

# Run the front
npm run --prefix Front start
```



### Documentation

[Postman](https://documenter.getpostman.com/view/12914728/VVBZR4tw)

### Github

[Github](https://github.com/lucasbodin/T-DAT-901)

### Launch recommender

run recommender_cluster.py