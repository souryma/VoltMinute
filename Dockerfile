FROM python:3.9-slim

WORKDIR /home

#RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

COPY streamlit_app.py requirements.txt /home/

# Assurez-vous que le dossier `.streamlit/` existe, puis ajoutez le fichier secrets.toml
COPY .streamlit/secrets.toml /home/.streamlit/secrets.toml

# Copier les images dans un dossier "static"
COPY img/ /home/img/

COPY pages/ /home/pages/

RUN pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]
