FROM	python:3.10-slim

RUN	apt update && apt install -yqq git && apt clean

WORKDIR	/src

COPY	requirements.txt	.

RUN	pip install -r requirements.txt

COPY	.	.

ENTRYPOINT	["/usr/local/bin/python3", "generate_match_summaries_from_folder.py"]

CMD ["/replays"]
