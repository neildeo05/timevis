frontend: main.py
	streamlit run main.py

prp: preprocess.py
	python preprocess.py

backend: backend.py
	python backend.py



clean:
	rm -rf data
	mkdir data

