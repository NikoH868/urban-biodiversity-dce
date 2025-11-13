data {
int<lower=0> N;      //total number of people
int<lower=0> T;      // total number of observations
int<lower=0> M;      //number of choice sets
int<lower=0> K;      //number of attributes, including the price and SQ
array[T] int<lower=0> ids; //group id
array[T] int y;       //the choices
array[M,T] row_vector[K] x;  // the attributes matrix


real alpha_mean;           //Priors for the mean log of the price coefficient
real<lower=0> alpha_sigma; //Priors for the standard devation of the log of price coefficient

array[K-2] real beta_mean;      //Priors for the mean of beta
array[K-2] real<lower=0> beta_sigma; //Priors for standard deviation of beta

real theta_mean;           //Priors for the mean of the last coefficient
real<lower=0> theta_sigma; //Piors for the standard deviation of the last coefficient

array[K-2] real<lower=0> a;     //Gamma Priors for the beta coefficients, 1st param
array[K-2] real<lower=0> b;     //Gamma Priors for the beta coefficients, 2nd param

real<lower=0> a_alpha;    //Gamma Priors for the price coefficient, 1st param
real<lower=0> b_alpha;    //Gamma Priors for the price coefficient, 2nd param

real<lower=0> a_theta;    //Gamma Priors for the ASC, last variable in data set, 1st param
real<lower=0> b_theta;    //Gamma Priors for the ASC, last variable in data set, 2nd param

real lower_precision_beta_ivar;
real lower_precision_alpha_ivar;
real lower_precision_theta_ivar;

real lower_beta_bound;
real upper_beta_bound;
real lower_theta_bound;
real upper_theta_bound;
}

 
parameters {

array[N] vector<lower=lower_beta_bound, upper=upper_beta_bound>[K-2] beta;            // N K-vectors
vector[K-2] beta_mu;                                                                  // means for beta
vector<lower=lower_precision_beta_ivar>[K-2] beta_ivar;                               // var parameters for beta

array[N] real alpha;
real alpha_mu;
real<lower=lower_precision_alpha_ivar> alpha_ivar;  

array[N] real <lower=lower_theta_bound, upper=upper_theta_bound> theta;
real theta_mu;
real<lower=lower_precision_theta_ivar> theta_ivar;  
}


transformed parameters 
{   array[T] vector[M] mu;
    array[N] vector[K] coef;
    array[K-2] real beta_std;
    real alpha_std;
    real theta_std;
    
    alpha_std=1/sqrt(alpha_ivar);
    theta_std=1/sqrt(theta_ivar);
    
    for(k in 1:K-2) {beta_std[k]=1/sqrt(beta_ivar[k]);}
    
    for(n in 1:N)
       {
        coef[n,1]=exp(alpha[n]);
        coef[n,2:K-1]=exp(alpha[n])*beta[n];
        coef[n,K]=exp(alpha[n])*theta[n];
        }
        
    for(t in 1:T) 
    {
        for(m in 1:M) {
            mu[t,m]=x[m,t]*coef[ids[t]];
                      }
    }    
    
}

model 
{ 
alpha_mu ~   normal(alpha_mean,alpha_sigma);
alpha_ivar ~ gamma(a_alpha,b_alpha);
theta_mu ~   normal(theta_mean,theta_sigma);
theta_ivar ~ gamma(a_theta,b_theta);

for(k in 1:K-2)
{
    beta_mu[k] ~ normal(beta_mean[k],beta_sigma[k]);
    beta_ivar[k] ~ gamma(a[k],b[k]);
}

for(n in 1:N) 

{  alpha[n]  ~ normal(alpha_mu, alpha_std);
   theta[n]  ~ normal(theta_mu, theta_std);

   for(k in 1:K-2) {beta[n,k] ~ normal(beta_mu[k], beta_std[k]);} 
        
}
 
    for(t in 1:T) {
        y[t] ~ categorical_logit(mu[t]);
    }
} 

generated quantities { vector[T] log_lik;
for (t in 1:T){log_lik[t]=log_softmax(mu[t])[y[t]];}

} 
