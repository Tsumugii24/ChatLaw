<div align="center"><h1>Themis</h1></div>

</div>

<div align="center"><h2>Description</h2></div>

&emsp;&emsp;Powered by LLM, `ChatLaw` is able to analysis your query and give you accurate advice in law region.

</div>

<div align="center"><h2>Demonstration</h2></div>

&emsp;&emsp;You can easily and directly experience the project demo online on `HuggingFace` now. Click here for Online Experience 👉 [Lesion-Cells DET - a Hugging Face Space by Tsumugii](https://huggingface.co/spaces/Tsumugii/lesion-cells-det) (just for placeholding right now)

</div>

<div align="center"><h2>ToDo</h2></div>

- [ ] Add a gif demonstration
- [ ] Deploy the demo on `HuggingFace`
- [x] Finish the LLMs interface and prompt design
- [ ] Finetune OpenSource models for more powerful data analysis
- [ ] Try multimodal LLM such as `LLava`, `GPT-4-turbo`





</div>

<div align="center"><h2>Quick Start</h2></div>

<details open>
    <summary><h4>Installation</h4></summary>

&emsp;&emsp;First of all, please make sure that you have already installed `conda` as Python runtime environment. And `miniconda` is strongly recommended.

&emsp;&emsp;1. create a virtual `conda` environment for the demo 😆

```bash
$ conda create -n law python==3.10 # law is the name of your environment
$ conda activate law
```

&emsp;&emsp;2. Install essential `requirements` by run the following command in the `CLI` 😊

```bash
$ git clone https://github.com/Tsumugii24/ChatLaw && cd ChatLaw
$ pip install -r requirements.txt
```

<details open>
    <summary><h4>Preparation</h4></summary>

&emsp;&emsp;1. open `.env.example` and fill your own `api keys` in the **corresponding place** if you want to use certain LLM, then **rename** the file to `.env`

```
# 智谱AI https://open.bigmodel.cn/usercenter/apikeys
ZHIPU_API_KEY = 

# 阿里灵积平台 https://dashscope.console.aliyun.com/apiKey
DASHSCOPE_API_KEY = 

# 讯飞星火 https://console.xfyun.cn/services/bm35
SPARKCHAT_APPID = 
SPARKCHAT_APISECRET = 
SPARKCHAT_APIKEY = 

# 百度千帆 https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
BAIDU_API_KEY = 
BAIDU_SECRET_KEY = 
BAIDU_ACCESS_TOKEN = 

# OpenAI https://platform.openai.com/api-keys
OPENAI_API_KEY = 

# Anthropic https://www.anthropic.com/api
CLAUDE_API_KEY = 
```

&emsp;&emsp;2. Open Source LLM

- [ ] planning to support ChatGLM, Baichuan, Qwen, LLama, InterLM... Coming soon~😄



<details open>
    <summary><h4>Run</h4></summary>

```
```





</div>

<div align="center"><h2>References</h2></div>

1. [Gradio](https://www.gradio.app/)
2. Labor Law





</div>

<div align="center"><h2>Acknowledgements</h2></div>

&emsp;&emsp;***I would like to express my sincere gratitude to Dr. Hua Cheng for his invaluable guidance and supports throughout the development of this project. His expertise and insightful feedback played a crucial role in shaping the direction of the project.***



</div>

<div align="center"><h2>Contact</h2></div>

Feel free to open GitHub issues or directly send me a mail if you have any questions about the project. 👻

