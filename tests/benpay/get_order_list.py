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


param = benpay_param.GetPayOrderListParam()
param.page = 1
param.limit = 10
param.offset = 1
param.order_by = ""
param.created_at_begin = 0
param.created_at_end = 0
param.payment_id = ""
param.out_trade_no = ""

resp = client.get_order_list(param)

if resp.status_code == 200:
    print(resp.json())
else:
    print(resp.text)

