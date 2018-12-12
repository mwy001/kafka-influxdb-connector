import argparse
import logging
from kafka import KafkaConsumer
from influxdb import InfluxDBClient

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument("-kbs", "--kafka_bootstrap_servers", default="localhost:9092")
    parser.add_argument("-kt", "--kafka_topic", default="")
    parser.add_argument("-kg", "--kafka_group", default="")
    parser.add_argument("-kmpr", "--kafka_max_poll_records", default=10, type=int)

    parser.add_argument("-ih", "--influxdb_host", default="localhost")
    parser.add_argument("-ip", "--influxdb_port", default=8086, type=int)
    parser.add_argument("-id", "--influxdb_dbname", default="")
    parser.add_argument("-irp", "--influxdb_retention_policy", default="autogen")
    parser.add_argument("-itp", "--influxdb_time_precision", default="ms")
    parser.add_argument("-ids", "--influxdb_batch_size", default=10, type=int)
    parser.add_argument("-ipt", "--influxdb_protocol", default="line")

    args = parser.parse_args()

    kafkaConsumer = KafkaConsumer(group_id=args.kafka_group,
        bootstrap_servers=args.kafka_bootstrap_servers,
        max_poll_records=args.kafka_max_poll_records)
    kafkaConsumer.subscribe(args.kafka_topic)

    influxClient = InfluxDBClient(args.influxdb_host,
        port=args.influxdb_port,
        database=args.influxdb_dbname)

    influx_buf = []

    for msg in kafkaConsumer:
        try:
            payload = msg.value.decode('utf-8')

            influx_buf.append(payload)

            if len(influx_buf) == args.influxdb_batch_size:
                influxClient.write_points(points=influx_buf,
                    time_precision=args.influxdb_time_precision,
                    retention_policy=args.influxdb_retention_policy,
                    batch_size=args.influxdb_batch_size,
                    protocol=args.influxdb_protocol)
                influx_buf.clear()

        except Exception as e:
            # print(e)
            pass
