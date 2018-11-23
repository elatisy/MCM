load('data.mat'); % value: data

Xtrain = (1 : 30)';
Ytrain = (data(2, 1 : 30))';

Xtest = (31 : 36)';
Ytest = (data(2, 31 : 36))';

% Xpredict = (43 : 48)';

Xpredict = (1 : 48)';

Xorigin = (1 : 36)';
Yorigin = (data(2, 1 : 36))';

gam = 100;
sig2 = 0.3;
lssvm_type = 'function estimation';
lssvm_kernel = 'RBF_kernel';

lssvm_model = initlssvm(Xorigin, Yorigin, lssvm_type, gam, sig2, lssvm_kernel);

%optimize
costfun = 'crossvalidatelssvm';
costfun_args = {10, 'mse'};
optfun = 'gridsearch';
lssvm_model = tunelssvm(lssvm_model, optfun, costfun, costfun_args);

%train
lssvm_model = trainlssvm(lssvm_model);

%predict
Ypredict = simlssvm(lssvm_model, Xpredict);

figure;
plot(Xpredict, Ypredict, 'r-x');
hold on;
plot(Xorigin, Yorigin, 'r-o');