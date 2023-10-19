import init
import openai
class Gpt():
    # 使用代码嵌入的RAM用户的访问密钥配置访问凭证。
    def init(self):
        json_data = init.read_json_file("conf.json")
        gpt = json_data["gpt"]
        openai.api_key = gpt[0]

    def ask_question(self,question):
        response = openai.Completion.create(
            engine="text-davinci-003",  # 使用ChatGPT模型
            prompt=f"请简要回答以下问题，保证答案的正确性，并且这些答案是可以使用谷歌查到的：{question}\n答案：",
            max_tokens=3000  # 最大生成的标记数，可以根据需要调整
        )
        return response.choices[0].text.strip()

# if __name__ == '__main__':
#     Gpt().init()
#     answer =Gpt().ask_question("3.签名可以解决的鉴别问题有?第三方冒充接收方篡改接收方伪造发送者否认")
#     print(answer)
