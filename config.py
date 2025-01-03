import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim.lr_scheduler import ReduceLROnPlateau
from datetime import datetime
import pytz

config = {

  'files': {
    'data_mode' : 'imagefolder',
    'data_dir': 'D:/Data',
    'choice_data': 'D:/Data/Winding/Winding1 (1).bmp',
  },

  'output': {
    'prompt' : ["Make more Winding pad"], # prompt
    'choice_prompt' : ["Good"], # prompt
    'image_height' : 512, # default height of Stable Diffusion
    'image_width' : 512, # default width of Stable Diffusion
    'num_inference_steps' : 20, # Number of denoising steps
    'guidance_scale' : 7.5, # Scale for classifier-free guidance
    'lora_scale' : 0.9,
    'output_model_path' : "./lora_finetuning_save",
    'output_weights_path' : "./lora_finetuning_weights",
    'output_log': datetime.now().strftime("%d%H%M%S"),
  },

  'preprocess_params': {
    'IMG_SIZE': 128, 
    'CENTER_CROP': True, 
    'RANDOM_FLIP': True, 
  },

  'model': 'model/stable-diffusion-v1-5',
  'model_params': {
    'weight_dtype': torch.float16, # half precision or torch.float32
    'Lora_rank' : 4,
    'init_lora_weights' : "gaussian",
  },

  'train_params': {
    'trn_data_loader_params': {
      'batch_size': 4,
      'num_workers' : 0,
      'shuffle': True,
      'use_amp' : True,
      'prediction_type' : 'epsilon', # 'None' or 'epsilon'  or 'v_prediction'
    },
    'tst_data_loader_params': {
      'batch_size': 'auto',
      'shuffle': False,
    },
    'loss_fn': F.mse_loss,
    'optim': torch.optim.AdamW,
    'optim_params': {
      'lr': 1e-04,
      'weight_decay': 0 # default 0.01
    },
    'lr_scheduler': ReduceLROnPlateau,
    'scheduler_params': {
      'mode': 'min',
      'factor': 0.1,
      'patience': 5,
      'verbose':False
    },

    'device': "cuda" if torch.cuda.is_available() else "cpu",
    'epochs': 30,
  },
}