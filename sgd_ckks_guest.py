#
# Copyright 2020 BE-GAIA. All Rights Reserved.
#
import gaia
import torch as th
from gaia.core.tensors.interpreters.ckks import CKKSTensor
hook = gaia.GaiaHook(th)

def fit(self, data_instances, testing_data_instance=None):
    """
    """
   
    self.context, self.secret_key = gaia.key_gen("ckks")
    self.transfer.public_key.remote(self.context.serialize(), role='HOST', idx=-1,
                                                    suffix=self.suffix_('pub_key'))


    # iteration
    while (self.n_iter_ < self.max_iter):

        y_host = self.transfer.y_host.get(idx=-1, suffix=f"y_host_{self.n_iter}")
        
        delta_y = compute_delta_y(labels, y_host, y_guest)
        cipher_delta_y = th.Tensor(delta_y)
        cipher_delta_y = cipher_delta_y.encrypt("ckks", public_key=self.context)
    
        gradient_guest = self.operation_modules_three(delta_y=delta_y, x)
            
        theta_guest = self.operation_modules_four(theta_guest=theta_guest, gradient_guest=gradient_guest,
                lr=updated_learning_rate, penalty=self.penalty, alpha=self.alpha)

        mask_gradient_host_noises = self.transfer.mask_gradient_host_noise.get(idx=-1, suffix=("mask_gradient_host_noise"))

        der_mask_gradient_host_noises = CKKSTensor.deserialize(mask_gradient_host_noises, self.context)
        gradient_host_noise = der_mask_gradient_host_noises.decrypt(secret_key=self.secret_key).numpy()
        gradient_host_noise = gradient_host_noise / batch_len
        self.transfer.gradient_host_noise.remote(gradient_host_noise, role=consts.HOST, idx=_idx,
                                                        suffix=f"gradient_host_noise{self.n_iter}")
                
        self.n_iter_ += 1