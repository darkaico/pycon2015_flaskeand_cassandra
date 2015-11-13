import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class BeerometerModel(Model):
    uuid = columns.UUID(primary_key=True, default=uuid.uuid4)
    brand = columns.Text(required=False)
    created_at = columns.DateTime()

    def to_dict(self):
        result = {}

        result['id'] = str(self.uuid)
        result['brand'] = self.brand
        result['created_at'] = self.created_at.strftime('%Y-%m-%d %H:%M:%S')

        return result
