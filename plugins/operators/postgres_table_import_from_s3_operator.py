from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class ImportTableFromS3Operator(BaseOperator):
    template_fields = ('sql',)
    template_ext = ('.sql',)
    ui_color = '#ededed'

    @apply_defaults
    def __init__(
            self,
            bucket,
            file_path,
            table,
            columns,
            postgres_conn_id='postgres_default',
            autocommit=True,
            schema=None,
            delimiter=',',
            region='us-east-2',
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sql = f"""
        CREATE EXTENSION IF NOT EXISTS aws_s3 CASCADE;
        SELECT aws_s3.table_import_from_s3(
                                       '{table}',
                                       '{','.join(columns)}',
                                        'DELIMITER ''{delimiter}''',
                                       aws_commons.create_s3_uri('{bucket}', '{file_path}', '{region}')
                                        ); """
        self.postgres_conn_id = postgres_conn_id
        self.autocommit = autocommit
        self.schema = schema

    def execute(self, context):
        self.log.info('Executing: %s', self.sql)
        self.hook = PostgresHook(postgres_conn_id=self.postgres_conn_id,
                                 schema=self.schema)
        self.hook.run(self.sql, self.autocommit)
        for output in self.hook.conn.notices:
            self.log.info(output)
