#
# Copyright 2020 BE-GAIA. All Rights Reserved.
#
import numpy as np

import pyckks as ckks
import torch as th
import gaia as gaia
from gaia.core.tensors.interpreters.ckks import CKKSTensor

hook = gaia.GaiaHook(th)


    def fit(self, X, y=None):
        """
        """

        context_buf = self.transfer.public_key.get(idx=0, suffix='pub_key')
        
        l, n_features_in_ = X.shape

        self.context = ckks.context_from(context_buf)
        
        w_host = np.zeros(n_features_in_)

        while(self.n_epoch_ < self.max_iter):
    
            y_host = self.operation_modules_one(X, w_host)
              
            self.transfer.y_host.remote(y_host, role='GUEST', idx=0, suffix=self.suffix_("y_host"))
            
    
            mask_delta_y = self.transfer.cipher_delta_y.get(idx=0, suffix=self.suffix_("cipher_delta_y"))

            mask_gradient_host_noises, noises = self.operation_modules_two(mask_delta_y=mask_delta_y)

            self.transfer.mask_gradient_host_noise.remote(mask_gradient_host_noises, role="GUEST",
                                                                        idx=0, suffix=f"mask_gradient_host_noise_{self.n_iter}")


            gradient_host_noises = self.transfer.gradient_host_noise.get(idx=0, suffix=f"{self.n_iter}_gradient_host_noise")
            
            gradient_host_noises = np.array(gradient_host_noises).squeeze()
            gradient_host = gradient_host_noises - noises
            
            w_host = self.operation_modules_three(w_host=w_host, gradient_host=gradient_host)

            
            self.n_epoch_ += 1

        return w_host



    def operation_modules_two(self, mask_delta_y, _x_host):
        

        noises = [[np.random.normal(0, 1) for _x_host]
        noises = np.array(noises)
        if self.low_band_mode:
            _noises = noises * batch_len
        else:
            _noises = noises

        works = []
        for i in range(max_threads):
            works.append((batch_x_host, mini_dim_host[i], mask_delta_y, _noises[i]))

        works = list(self.pool.map(lambda actor, val: actor.ckks_mul_and_add.remote(*val), works))

        if self.low_band_mode:
            cipher_gradient_host = [CKKSTensor.deserialize(_gradient_host, self.context) for work in works for _gradient_host in work]
            cipher_gradient_host = CKKSTensor.concat(cipher_gradient_host)
            cipher_gradient_host = CKKSTensor.serialize(cipher_gradient_host)
        else:
            cipher_gradient_host = []
            for now_gradient_host in works:
                cipher_gradient_host.extend(now_gradient_host)

        return cipher_gradient_host, np.concatenate(noises)
