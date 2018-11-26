X = (1 : 50)';
Y = X .^ 3;

lssvm_type = 'function estimation';
lssvm_kernel = 'RBF_kernel';

lssvm_model = initlssvm(X, Y, lssvm_type, [], [], lssvm_kernel, 'o');

%optimize
costfun = 'crossvalidatelssvm';
costfun_args = {10, 'mse'};
optfun = 'gridsearch';
lssvm_model = tunelssvm(lssvm_model, optfun, costfun, costfun_args);

lssvm_model = trainlssvm(lssvm_model);

ci = cilssvm(lssvm_model);

X = (1 : 100)';
Y_predict = simlssvm(lssvm_model, X);

Y = X .^ 3;

figure;
plot(X, Y, 'r-x', X, Y_predict, 'b-o');
hold on
X = (1 : 50)';
fill([X;flipud(X)],[ci(:,1);flipud(ci(:,2))],'c','FaceAlpha',0.5,'EdgeAlpha',1,'EdgeColor','k');