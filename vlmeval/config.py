from .vlm import *
from .api import GPT4V, GPT4V_Internal, GeminiProVision, QwenVLAPI
from functools import partial

PandaGPT_ROOT = None
MiniGPT4_ROOT = None
TransCore_ROOT = None
Yi_ROOT = None

api_models = {
    'GPT4V': partial(GPT4V, model='gpt-4-vision-preview', temperature=0, img_size=512, img_detail='low', retry=10),
    'GPT4V_INT': partial(GPT4V_Internal, model='gpt-4-vision-preview', temperature=0, img_size=512, img_detail='low', retry=10),
    'GPT4V_SHORT': partial(
        GPT4V, model='gpt-4-vision-preview', temperature=0, img_size=512, img_detail='low', retry=10, 
        system_prompt="Please respond to the following task in a short reply. "),
    'GPT4V_SHORT_INT': partial(
        GPT4V_Internal, model='gpt-4-vision-preview', temperature=0, img_size=512, img_detail='low', retry=10,
        system_prompt="Please respond to the following task in a short reply. "),
    'GeminiProVision': partial(GeminiProVision, temperature=0, retry=10),
    'QwenVLPlus': partial(QwenVLAPI, model='qwen-vl-plus', temperature=0, retry=10),
    'QwenVLMax': partial(QwenVLAPI, model='qwen-vl-max', temperature=0, retry=10),
}

models = {
    'hpt-air-mmmu': partial(HPT),
    'hpt-air-mmbench': partial(HPT, vis_scale=392, is_crop=False),
    'hpt-air-seed': partial(HPT, is_crop=False),
    'hpt-air-demo': partial(HPT, vis_scale=392, is_crop=False),
    'hpt-air-demo-local': partial(HPT, vis_scale=392, is_crop=False, global_model_path='../HPT_AIR_HF/'),
    'hpt-air-1-5': partial(HPT1_5, global_model_path='HyperGAI/HPT1_5-Air-Llama-3-8B-Instruct-multimoda', vis_scale=448, prompt_template='llama3_chat'),
    'hpt-edge-1-5': partial(HPT1_5, global_model_path='HyperGAI/HPT1_5-Edge', vis_scale=490, prompt_template='phi3_chat'),
}

supported_VLM = {}
for model_set in [models, api_models]:
    supported_VLM.update(model_set)