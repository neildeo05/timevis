frontend: main.py
	streamlit run main.py 21339392

preprocess: preprocess.py
	python preprocess.py data.csv

backend: backend.py
	python backend.py

install: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf data
	mkdir data

