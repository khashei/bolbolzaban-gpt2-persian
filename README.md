# Introduction
This repo includes starter code to finetune [bolbolzaban gpt2 persian](https://huggingface.co/bolbolzaban/gpt2-persian). Please do not hesitate to send pull requests to improve this code.

# BolbolZaban GPT2-Persian
bolbolzaban/gpt2-persian is gpt2 language model that is trained with hyper parameters similar to standard gpt2-medium with following differences:
1. The context size is reduced from 1024 to 256 sub words in order to make the training affordable 
2. Instead of BPE, google sentence piece tokenizor is used for tokenization.
3. The training dataset only include Persian text. All non-persian characters are replaced with especial tokens (e.g [LAT], [URL], [NUM])

Please refer to this [blog post](https://medium.com/@khashei/a-not-so-dangerous-ai-in-the-persian-language-39172a641c84) for further detail. 
Also try the model [here](https://huggingface.co/bolbolzaban/gpt2-persian?text=%D8%AF%D8%B1+%DB%8C%DA%A9+%D8%A7%D8%AA%D9%81%D8%A7%D9%82+%D8%B4%DA%AF%D9%81%D8%AA+%D8%A7%D9%86%DA%AF%DB%8C%D8%B2%D8%8C+%D9%BE%DA%98%D9%88%D9%87%D8%B4%DA%AF%D8%B1%D8%A7%D9%86) or on [Bolbolzaban.com](http://www.bolbolzaban.com/text).

## Special Tokens
gpt-persian is trained for the purpose of research on Persian poetry. Because of that all english words and numbers are replaced with special tokens and only standard Persian alphabet is used as part of input text. Here is one example:

Original text: اگر آیفون یا آیپد شما دارای سیستم عامل iOS 14.3 یا iPadOS 14.3 یا نسخه‌های جدیدتر باشد

Text used in training: اگر آیفون یا آیپد شما دارای سیستم عامل [LAT] [NUM] یا [LAT] [NUM] یا نسخه‌های جدیدتر باشد

Please consider normalizing your input text using [Hazm](https://github.com/sobhe/hazm) or similar libraries and ensure only Persian characters are provided as input.

If you want to use classical Persian poetry as input use [BOM] (begining of mesra) at the beginning of each verse (مصرع) followed by [EOS] (end of statement) at the end of each couplet (بیت). 

See following links for example:

[[BOM] توانا بود](https://huggingface.co/bolbolzaban/gpt2-persian?text=%5BBOM%5D+%D8%AA%D9%88%D8%A7%D9%86%D8%A7+%D8%A8%D9%88%D8%AF)

[[BOM] توانا بود هر که دانا بود [BOM]](https://huggingface.co/bolbolzaban/gpt2-persian?text=%5BBOM%5D+%D8%AA%D9%88%D8%A7%D9%86%D8%A7+%D8%A8%D9%88%D8%AF+%D9%87%D8%B1+%DA%A9%D9%87+%D8%AF%D8%A7%D9%86%D8%A7+%D8%A8%D9%88%D8%AF+%5BBOM%5D)

[[BOM] توانا بود هر که دانا بود [BOM] ز دانش دل پیر](https://huggingface.co/bolbolzaban/gpt2-persian?text=%5BBOM%5D+%D8%AA%D9%88%D8%A7%D9%86%D8%A7+%D8%A8%D9%88%D8%AF+%D9%87%D8%B1+%DA%A9%D9%87+%D8%AF%D8%A7%D9%86%D8%A7+%D8%A8%D9%88%D8%AF+%5BBOM%5D+%D8%B2+%D8%AF%D8%A7%D9%86%D8%B4+%D8%AF%D9%84+%D9%BE%DB%8C%D8%B1)

[[BOM] توانا بود هر که دانا بود [BOM] ز دانش دل پیربرنا بود  [EOS]](https://huggingface.co/bolbolzaban/gpt2-persian?text=%5BBOM%5D+%D8%AA%D9%88%D8%A7%D9%86%D8%A7+%D8%A8%D9%88%D8%AF+%D9%87%D8%B1+%DA%A9%D9%87+%D8%AF%D8%A7%D9%86%D8%A7+%D8%A8%D9%88%D8%AF+%5BBOM%5D+%D8%B2+%D8%AF%D8%A7%D9%86%D8%B4+%D8%AF%D9%84+%D9%BE%DB%8C%D8%B1%D8%A8%D8%B1%D9%86%D8%A7+%D8%A8%D9%88%D8%AF++%5BEOS%5D)

If you like to know about structure of classical Persian poetry refer to these [blog posts](https://medium.com/@khashei).
## Acknowledgment
This project is supported by Cloud TPUs from Google’s TensorFlow Research Cloud (TFRC).
## Citation and Reference
Please reference "bolbolzaban.com" website if you are using gpt2-persian in your research or commertial application.
## Contacts
Please reachout on [Linkedin](https://www.linkedin.com/in/khashei/) or [Telegram](https://t.me/khasheia) if you have any question or need any help to use the model.

Follow [Bolbolzaban](http://bolbolzaban.com/about) on [Twitter](https://twitter.com/bolbol_zaban), [Telegram](https://t.me/bolbol_zaban) or [Instagram](https://www.instagram.com/bolbolzaban/)
