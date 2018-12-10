Kafka -> Influxdb sync toolkit based on kafka & influxdb python driver. Suggested to run in docker.

Usage:
  cd kafka-influxdb-connector
  docker build -t <your-tag-name> .
  docker run <your-tag-name>

Override these environment variables:
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
