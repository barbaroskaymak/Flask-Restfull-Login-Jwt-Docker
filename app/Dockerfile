FROM ubuntu:20.04 AS builder-image

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3.9 -m venv /home/restapi/venv
ENV PATH="/home/restapi/venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

FROM ubuntu:20.04 AS runner-image
RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3-venv && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home restapi
COPY --from=builder-image /home/restapi/venv /home/restapi/venv

USER restapi
RUN mkdir /home/restapi/code
WORKDIR /home/restapi/code/app
COPY . .

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

# activate virtual environment
ENV VIRTUAL_ENV=/home/restapi/venv
ENV PATH="/home/restapi/venv/bin:$PATH"
ENV FLASK_APP='app'
ENV FLASK_ENV="development"
ENV FLASK_DEBUG=1

CMD ["flask", "run","--host=0.0.0.0"]
