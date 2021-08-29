FROM python:3.8-buster

RUN pip install streamlit==0.87.0

COPY . .

CMD streamlit run app.py