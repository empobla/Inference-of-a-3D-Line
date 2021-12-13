import numpy as np
from scipy.stats import multivariate_normal
from random import uniform
N=50000
def run_task1():
    prior_mean = [0,0,4]
    prior_cov =  6*np.identity(3)
    prior_rv = multivariate_normal(prior_mean, prior_cov)
    cur_pi, cur_pf = prior_rv.rvs(2)

    accepted_pi = [0]*N
    accepted_pf = [0]*N

    proposal_cov = 0.3 * np.identity(3)

    for i in range(N):
        proposed_pi = multivariate_normal(cur_pi, proposal_cov).rvs()
        proposed_pf = multivariate_normal(cur_pf, proposal_cov).rvs()

        log_cur_pi_pf_joint_pdf = prior_rv.logpdf(cur_pi) + prior_rv.logpdf(cur_pf)
        log_proposed_pi_pf_joint_pdf = prior_rv.logpdf(proposed_pi)+ prior_rv.logpdf(proposed_pf)

        current_dist_log_likelihood = calculate_log_likelihood(CAMERA1, camera1_rs, cur_pi, cur_pf)
        proposed_dist_log_likelihood = calculate_log_likelihood(CAMERA1, camera1_rs, proposed_pi, proposed_pf)

        current_posterior = log_cur_pi_pf_joint_pdf + current_dist_log_likelihood
        proposed_posterior = log_proposed_pi_pf_joint_pdf +  proposed_dist_log_likelihood
        
        r = np.exp(proposed_posterior - current_posterior)
        step_probability = min(r,1)

        if step_probability == 1:
            random_draw = uniform().rvs()

            if(random_draw <= step_probability):
                cur_pi, cur_pf = proposed_pi, proposed_pf

        accepted_pi[i] = cur_pi
        accepted_pf[i] = cur_pf

    print(accepted_pi)
    print(accepted_pf)



