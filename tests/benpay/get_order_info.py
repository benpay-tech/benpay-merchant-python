import config
import sys

sys.path.append("../../")
from benpay_merchant_api_sdk.client import BenpayMerchantClient
import benpay_merchant_api_sdk.param.benpay_merchant_param as benpay_param

client = BenpayMerchantClient(
    api_key=config.API_KEY,
    server=config.SERVER,
    merchant_private_key_string=config.MERCHANT_PRIVATE_KEY_STRING,
    platform_public_key_string=config.PLATFORM_PUBLIC_KEY_STRING
)

param = benpay_param.GetPayOrderInfoParam()
param.payment_id = "82bbea8c2ec048bc8339ba64c046f7cc"


resp = client.get_order_info(param)

if resp.status_code == 200:
    print(resp.json())
else:
    print(resp.text)