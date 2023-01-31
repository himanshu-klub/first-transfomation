import json
from typing import List, Tuple

from airbyte_protocol import AirbyteMessage, AirbyteLogger, AirbyteRecord
def transform(logger: AirbyteLogger, message: AirbyteMessage) -> Tuple[List[AirbyteRecord], List[AirbyteMessage]]:
    records = message.records
    for record in records:
        record.fields["new_field"] = "new_value"
    return records, []
