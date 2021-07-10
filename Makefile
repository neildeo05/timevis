frontend: main.py
	streamlit run main.py 21339392

prp: preprocess.py
	python preprocess.py

backend: backend.py
	python backend.py



clean:
	rm -rf data
	mkdir data

