import config
import sys
import json
sys.path.append("../../")
from benpay_merchant_api_sdk.client import BenpayMerchantClient
import requests

client = BenpayMerchantClient(
    api_key=config.API_KEY,
    server=config.SERVER,
    merchant_private_key_string=config.MERCHANT_PRIVATE_KEY_STRING,
    platform_public_key_string=config.PLATFORM_PUBLIC_KEY_STRING
)

res = requests.Response()
res.headers['benpay-signature'] = 'HrJmV+39NeUmw89xN5fTfmZWod7Q9kJe2taf23Nqd4NajkPL0HVMaxCK3Gu7yiopeoqaw9fL6A7wUTClOk8h6zRUTWfDwTcFcPLsjEc0g1r/iHWAhvybL1iRAj5PvlZdxPMzhld8ZO54O91D245Bi77a+IKQZIGgVbQ9QymOtTgjii/Eb+FFkWtPSbil9SnDCiyTXPyewPBBP5p+7K3KDsOnmN4eonSCQVVI3SQOQNQStrqLhfbcuQykC44iacBZkPDJV2PDkjjaWsYca5dC4xSvvi5JZQQFT23hs/PJdVfeUMOmdYdYOte8Av587DknX9AO8hlu/jLgtnT6ILQlJw=='
res.headers['benpay-nonce'] = 'cd6789c736de43ad9a9ba21116394698'
res.headers['benpay-timestamp'] = 1726718302368
body = '{"notify_data":{"payment_id":"73e97cae1eef4ef383806359eda1c7d7","chain":"Benfen","mechant_id":"2929175458ff4cdbaa8af4720a45f90e","out_trade_no":"9778fhd-6839a-4bb7-bc03-58bdc81e6e2a","coin":"Benfen","coin_amount":"0.15","status":"PAID","transaction_hash":"Etg9EzH9ekF5skrD9JpCsCeXeFzZqwZsDQTbeEV3PVVs"},"notify_id":"90e83b8648fb487680ad6506a8ef3c55","notify_type":"PAY"}'
res._content = body.encode('utf-8')

re = client.handler_webhook(res)
if re.status_code == 200:
    print(re.json())
else:
    print(re.text)