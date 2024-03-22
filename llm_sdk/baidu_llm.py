from langchain.llms.base import LLM
from typing import Any, List, Mapping, Optional, Dict, Union, Tuple
from pydantic import Field
from llm_sdk.self_llm import Self_LLM
import json
import requests
from langchain.callbacks.manager import CallbackManagerForLLMRun


# 获取文心access_token的函数 get_access_token()
def get_access_token(baidu_api_key: str, baidu_secret_key: str):
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={baidu_api_key}&client_secret={baidu_secret_key}"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json().get("access_token")


class Baidu_LLM(Self_LLM):
    # 百度文心大模型的自定义 LLM
    # URL
    url: str = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token={}"
    # api_key 继承自Self_LLM
    # Secret_Key
    secret_key: str = None
    # access_token
    access_token: str = None

    def init_access_token(self):
        if self.api_key != None and self.secret_key != None:
            # 两个 Key 均非空才可以获取 access_token
            try:
                self.access_token = get_access_token(self.api_key, self.secret_key)
            except Exception as e:
                print(e)
                print("获取 access_token 失败，请检查 Key")
        else:
            print("API_Key 或 Secret_Key 为空，请检查 Key")

    def _call(self, prompt: str, stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None,
              **kwargs: Any):
        # 如果 access_token 为空，初始化 access_token
        if self.access_token == None:
            self.init_access_token()
        # API 调用 url
        url = self.url.format(self.access_token)
        # 配置 POST 参数
        payload = json.dumps({
            "system": "你是一位精通中华人民共和国劳动法且经验丰富的律师。",  # system message
            "messages": [
                {
                    "role": "user",  # user prompt
                    "content": "{}".format(prompt)  # 输入的 prompt
                }
            ],
            'temperature': self.temperature
        })
        headers = {
            'Content-Type': 'application/json'
        }
        # 发起请求
        response = requests.request("POST", url, headers=headers, data=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            # 返回的是一个 Json 字符串
            js = json.loads(response.text)
            # print(js)
            return js["result"]
        else:
            return "请求失败"

    @property
    def _llm_type(self) -> str:
        return "Baidu"
