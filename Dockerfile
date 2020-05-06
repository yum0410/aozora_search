FROM docker.elastic.co/elasticsearch/elasticsearch:7.6.0
COPY es-data/elasticsearch.yml /usr/share/elasticsearch/config/
COPY es-data/mapping.json /usr/share/elasticsearch/data/
RUN elasticsearch-plugin install analysis-kuromoji
RUN elasticsearch-plugin install analysis-icu