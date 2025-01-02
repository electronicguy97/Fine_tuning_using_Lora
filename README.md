# Lora_finetuning
로라를 활용한 diffusion 모델 finetuning

환경
|OS|Grapic|Pyhon|torch|tarnsformers|datasets|diffusers|peft|
|---|---|---|---|---|---|---|---|
|Window|3060(12G, GDDR6)|3.10.16|2.5.1|4.47.1|3.2.0|0.33.0.dev0|0.14.1.dev0|

그래픽 1개 및 APM을 사용하여 학습 시 30 Epochs 기준 1Epoch당 1m30s 가량 소요 총 45분 소요

1. Lora를 활용하여 Unet을 FineTuning하고 해당 모델을 통해 Text to Image 출력
2. CLIP를 활용하여 Image + Text로 필요한 이미지를 출력

---
[참고 Github](https://github.com/metamath1/pytorch-stable-diffusion-fine-tuning/blob/main/02-sd_lora_finetuning.ipynb)
