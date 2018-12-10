FROM python:3.7.1

ENV kafka_bootstrap_servers ""
ENV kafka_topic ""
ENV kafka_group ""
ENV kafka_max_poll_records 10
ENV influxdb_host ""
ENV influxdb_port ""
ENV influxdb_dbname ""
ENV influxdb_retention_policy ""
ENV influxdb_time_precision "ms"
ENV influxdb_batch_size 10
ENV influxdb_protocol "line"

RUN pip install --upgrade pip && pip install kafka-python && pip install influxdb

ADD connector.py /bin

CMD python /bin/connector.py \
    --kafka_bootstrap_servers $kafka_bootstrap_servers \
    --kafka_topic $kafka_topic \
    --kafka_group $kafka_group \
    --kafka_max_poll_records $kafka_max_poll_records \
    --influxdb_host $influxdb_host \
    --influxdb_port $influxdb_port \
    --influxdb_dbname $influxdb_dbname \
    --influxdb_retention_policy $influxdb_retention_policy \
    --influxdb_time_precision $influxdb_time_precision \
    --influxdb_batch_size $influxdb_batch_size \
    --influxdb_protocol $influxdb_protocol
