from .models.data import get_data_config
from .models.vae_dmp_2D import VAE_DMP_2D

vae_dmp_joint_chendb_5D = VAE_DMP_2D()
vae_dmp_joint_chendb_5D.DATA_PARAMS = get_data_config(["jointAngle"], "ChenDB")

vae_dmp_joint_chendb_5D.VTSFE_PARAMS["vae_architecture"]["n_z"] = 5
